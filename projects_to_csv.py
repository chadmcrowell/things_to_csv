import things
import csv
from datetime import datetime

from common import created_in, parse_args, year_suffix

includeCompleted, includeCanceled, year = parse_args("Export Things projects to CSV.")


def getProjects(includeCompleted, includeCanceled):
    completed = []
    canceled = []

    if includeCompleted:
        completed = things.projects(status="completed", include_items=True)
    if includeCanceled:
        canceled = things.projects(status="canceled", include_items=True)

    projects = things.projects(include_items=True)
    projects = projects + completed + canceled

    return projects


usersProjects = created_in(getProjects(includeCompleted, includeCanceled), year)

# format string for output
completed = "_completed" if includeCompleted else ""
canceled = "_canceled" if includeCanceled else ""
now = datetime.now()


filename = f"things_projects_{now.year}-{now.month}-{now.day}_{now.hour}-{now.minute}_incomplete{completed}{canceled}{year_suffix(year)}.csv"


keys = [
    "uuid",
    "type",
    "title",
    "shortcut",
    "status",
    "start",
    "area",
    "area_title",
    "project",
    "project_title",
    "heading",
    "heading_title",
    "notes",
    "items",
    "tags",
    "start_date",
    "deadline",
    "reminder_time",
    "checklist",
    "stop_date",
    "created",
    "modified",
    "index",
    "today_index",
]

with open(filename, "w", encoding="utf-8-sig", newline="") as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(usersProjects)
