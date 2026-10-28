import argparse


def parse_args(description):
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("includeCompleted", nargs="?", default=False)
    parser.add_argument("includeCanceled", nargs="?", default=False)
    parser.add_argument("--year", type=int, help="only items created in YEAR")
    args = parser.parse_args()
    return args.includeCompleted, args.includeCanceled, args.year


def created_in(items, year):
    if year is None:
        return items
    return [i for i in items if str(i.get("created", "")).startswith(str(year))]


def year_suffix(year):
    return f"_created{year}" if year is not None else ""
