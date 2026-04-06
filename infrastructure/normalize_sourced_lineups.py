import csv
from pathlib import Path
from urllib.parse import urlparse


SRC = Path(__file__).resolve().parent / "Data" / "Golf Comparison - Sourced Model Lineups 2020-2025.csv"

OFFICIAL_DOMAINS = {
    "taylormadegolf.com",
    "www.taylormadegolf.com",
    "callawaygolf.com",
    "www.callawaygolf.com",
    "titleist.com",
    "www.titleist.com",
    "ping.com",
    "www.ping.com",
    "ca.ping.com",
}

# Targeted URL upgrades discovered during web research.
URL_UPGRADES = {
    ("Driver", "TaylorMade", "2022", "Stealth"): "https://www.taylormadegolf.com/Stealth-Driver/DW-TA026.html?lang=en_US",
    ("Driver", "TaylorMade", "2022", "Stealth Plus"): "https://www.taylormadegolf.com/clubhouse/265430-driver-comparison-stealth-plus-vs-stealth-vs-stealth-hd.html?lang=en_US",
    ("Driver", "TaylorMade", "2022", "Stealth HD"): "https://www.taylormadegolf.com/clubhouse/265430-driver-comparison-stealth-plus-vs-stealth-vs-stealth-hd.html?lang=en_US",
    ("Driver", "TaylorMade", "2025", "Qi35"): "https://www.taylormadegolf.com/Qi35-Driver/M1449209.html?lang=en_US",
    ("Driver", "TaylorMade", "2025", "Qi35 LS"): "https://www.taylormadegolf.com/clubhouse/888776-taylormade-golf-announces-qi35-family-of-drivers.html?lang=en_US",
    ("Driver", "TaylorMade", "2025", "Qi35 Max"): "https://www.taylormadegolf.com/clubhouse/888776-taylormade-golf-announces-qi35-family-of-drivers.html?lang=en_US",
    ("Driver", "TaylorMade", "2025", "Qi35 Max Lite"): "https://www.taylormadegolf.com/clubhouse/888776-taylormade-golf-announces-qi35-family-of-drivers.html?lang=en_US",
    ("Driver", "Callaway", "2023", "Paradym"): "https://www.callawaygolf.com/paradym-family",
    ("Driver", "Callaway", "2023", "Paradym X"): "https://www.callawaygolf.com/paradym-family",
    ("Driver", "Callaway", "2023", "Paradym Triple Diamond"): "https://www.callawaygolf.com/paradym-family",
    ("Driver", "Callaway", "2022", "Rogue ST Max"): "https://www.callawaygolf.com/rogue-st-family/rogue-st-drivers",
    ("Driver", "Callaway", "2022", "Rogue ST Max D"): "https://www.callawaygolf.com/rogue-st-family/rogue-st-drivers",
    ("Driver", "Callaway", "2022", "Rogue ST Max LS"): "https://www.callawaygolf.com/rogue-st-family/rogue-st-drivers",
}


def source_type(url: str) -> str:
    host = urlparse(url).netloc.lower()
    return "official" if host in OFFICIAL_DOMAINS else "secondary"


def main() -> None:
    with SRC.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
        headers = list(rows[0].keys())

    if "Source Type" not in headers:
        headers.append("Source Type")

    for r in rows:
        key = (r.get("Category", ""), r.get("Manufacturer", ""), r.get("Year", ""), r.get("Model", ""))
        if key in URL_UPGRADES:
            r["Source URL"] = URL_UPGRADES[key]
        r["Source Type"] = source_type(r.get("Source URL", ""))

    with SRC.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=headers)
        w.writeheader()
        w.writerows(rows)

    print("Normalized sourced lineup URLs and source types.")


if __name__ == "__main__":
    main()
