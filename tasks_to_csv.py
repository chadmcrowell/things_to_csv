import things
import csv
from datetime import datetime

from common import created_in, parse_args, year_suffix

includeCompleted, includeCanceled, year = parse_args("Export Things to-dos to CSV.")


def getTasks(includeCompleted, includeCanceled):
    completed = []
    canceled = []

    if includeCompleted:
        completed = things.todos(status="completed", include_items=True)
    if includeCanceled:
        canceled = things.todos(status="canceled", include_items=True)

    tasks = things.todos(include_items=True)
    tasks = tasks + completed + canceled

    return tasks


usersTasks = created_in(getTasks(includeCompleted, includeCanceled), year)

# format string for output
completed = "_completed" if includeCompleted else ""
canceled = "_canceled" if includeCanceled else ""
now = datetime.now()


filename = f"things_tasks_{now.year}-{now.month}-{now.day}_{now.hour}-{now.minute}_incomplete{completed}{canceled}{year_suffix(year)}.csv"


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
    dict_writer.writerows(usersTasks)
