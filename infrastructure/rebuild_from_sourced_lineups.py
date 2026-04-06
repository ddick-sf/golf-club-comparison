import csv
from pathlib import Path


BASE = Path(__file__).resolve().parent
DATA = BASE / "Data"

SOURCED = DATA / "Golf Comparison - Sourced Model Lineups 2020-2025.csv"
DRIVERS = DATA / "Golf Comparison - Drivers.csv"
FAIRWAYS = DATA / "Golf Comparison - Fairway.csv"
IRONS = DATA / "Golf Comparison - Irons.csv"
ROW_SOURCES = DATA / "Golf Comparison - Row Sources.csv"


def read_csv(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, headers: list[str], rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=headers)
        w.writeheader()
        for r in rows:
            w.writerow({h: r.get(h, "") for h in headers})


def in_scope(row: dict, year_field: str) -> bool:
    y = row.get(year_field, "")
    if not y.isdigit():
        return False
    yi = int(y)
    return 2020 <= yi <= 2025


def main() -> None:
    sourced = read_csv(SOURCED)

    d_rows = read_csv(DRIVERS)
    f_rows = read_csv(FAIRWAYS)
    i_rows = read_csv(IRONS)

    d_headers = list(d_rows[0].keys())
    f_headers = list(f_rows[0].keys())
    i_headers = list(i_rows[0].keys())

    sourced_mfrs = {r["Manufacturer"] for r in sourced}

    # Remove existing 2020-2025 rows for sourced manufacturers.
    d_keep = [r for r in d_rows if not (r.get("Manufacturer") in sourced_mfrs and in_scope(r, "Release Year"))]
    f_keep = [r for r in f_rows if not (r.get("Manufacturer") in sourced_mfrs and in_scope(r, "Release Year"))]
    i_keep = [r for r in i_rows if not (r.get("Manufacturer") in sourced_mfrs and in_scope(r, "Year"))]

    out_sources = []

    for s in sourced:
        cat = s["Category"]
        mfr = s["Manufacturer"]
        year = s["Year"]
        model = s["Model"]
        src = s["Source URL"]
        src_type = s.get("Source Type", "")

        if not year.isdigit() or not (2020 <= int(year) <= 2025):
            continue

        if cat == "Driver":
            row = {h: "" for h in d_headers}
            row["Manufacturer"] = mfr
            row["Release Year"] = year
            row["Model Name"] = model
            d_keep.append(row)
        elif cat == "Fairway":
            row = {h: "" for h in f_headers}
            row["Manufacturer"] = mfr
            row["Year"] = year
            row["Release Year"] = year
            row["Model Name"] = model
            f_keep.append(row)
        elif cat == "Iron":
            row = {h: "" for h in i_headers}
            row["Manufacturer"] = mfr
            row["Year"] = year
            row["Model"] = model
            i_keep.append(row)
        else:
            continue

        out_sources.append(
            {
                "Category": cat,
                "Manufacturer": mfr,
                "Year": year,
                "Model": model,
                "Source URL": src,
                "Source Type": src_type,
            }
        )

    # Sort with latest year first.
    d_keep.sort(key=lambda r: (int(r["Release Year"]) if r.get("Release Year", "").isdigit() else -1, r.get("Manufacturer", ""), r.get("Model Name", "")), reverse=True)
    f_keep.sort(key=lambda r: (int(r["Release Year"]) if r.get("Release Year", "").isdigit() else -1, r.get("Manufacturer", ""), r.get("Model Name", "")), reverse=True)
    i_keep.sort(key=lambda r: (int(r["Year"]) if r.get("Year", "").isdigit() else -1, r.get("Manufacturer", ""), r.get("Model", "")), reverse=True)

    write_csv(DRIVERS, d_headers, d_keep)
    write_csv(FAIRWAYS, f_headers, f_keep)
    write_csv(IRONS, i_headers, i_keep)

    src_headers = ["Category", "Manufacturer", "Year", "Model", "Source URL", "Source Type"]
    out_sources.sort(key=lambda r: (r["Category"], r["Manufacturer"], r["Year"], r["Model"]))
    write_csv(ROW_SOURCES, src_headers, out_sources)

    print("Rebuilt Drivers/Fairway/Irons from sourced model lineups.")
    print(f"Wrote source mapping: {ROW_SOURCES.name}")


if __name__ == "__main__":
    main()
