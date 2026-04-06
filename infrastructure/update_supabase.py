import argparse
import os
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Apply setup_supabase.sql to Supabase using Supabase CLI."
    )
    parser.add_argument(
        "--sql-file",
        default="setup_supabase.sql",
        help="Path to SQL file to execute (default: setup_supabase.sql)",
    )
    parser.add_argument(
        "--linked",
        action="store_true",
        help="Use linked Supabase project database (supabase link required).",
    )
    parser.add_argument(
        "--db-url",
        default=os.getenv("SUPABASE_DB_URL", ""),
        help="Postgres connection string. Defaults to SUPABASE_DB_URL env var.",
    )
    parser.add_argument(
        "--supabase-bin",
        default="supabase.exe" if os.name == "nt" else "supabase",
        help="Supabase CLI binary path/name.",
    )
    args = parser.parse_args()

    sql_file = Path(args.sql_file).resolve()
    if not sql_file.exists():
        print(f"SQL file not found: {sql_file}")
        return 1

    if not args.linked and not args.db_url:
        print("Provide either --linked or --db-url (or SUPABASE_DB_URL env var).")
        return 1

    cmd = [args.supabase_bin, "db", "query", "--file", str(sql_file), "--output", "json"]
    if args.linked:
        cmd.append("--linked")
    else:
        cmd.extend(["--db-url", args.db_url])

    print("Running:", " ".join(cmd[:-1] + ["***" if "--db-url" in cmd else cmd[-1]]))

    try:
        result = subprocess.run(cmd, check=False, capture_output=True, text=True)
    except FileNotFoundError:
        print(f"Supabase CLI not found: {args.supabase_bin}")
        return 1

    if result.stdout:
        print(result.stdout.strip())
    if result.stderr:
        print(result.stderr.strip(), file=sys.stderr)

    if result.returncode != 0:
        print(f"Update failed with exit code {result.returncode}")
        return result.returncode

    print("Supabase update completed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
