# Things to CSV

A Python3 tool to export your Things 3 database to a CSV, using the [Things Python API](https://github.com/thingsapi/things.py).

### Notes

- Each of the Things database entities (Tasks, Projects, Areas, Tags) are exported separately, hence separate files for each.

- If a task or project has not been modified since it's completion (e.g., by adding extra notes post-hoc), then one may take the `modified` property of `completed` tasks and projects as the completion date and time.

## Getting Your Data

Install the [Things Python API](https://github.com/thingsapi/things.py) from `requirements.txt`:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Assuming you have downloaded the files and are in the `things_to_csv` directory, to get all of your Things data in a single CSV, run `python3 things_to_csv.py True True`.
The first Boolean parameter represents the inclusion of completed tasks, and the second canceled tasks.

If you would only like to include incomplete tasks and projects, simply run `python3 things_to_csv.py`

#### Limit to a Year

`things_to_csv.py`, `tasks_to_csv.py` and `projects_to_csv.py` accept an optional `--year` flag that keeps only items created in that year:
`python3 things_to_csv.py True --year 2026`

The output filename gets a `_created<year>` suffix. Tags and areas have no creation date, so `things_to_csv.py` always includes them.

#### Get Your Tasks

Run `python3 tasks_to_csv` to get all incomplete tasks as a CSV in this directory.

If you'd like to include completed and canceled tasks, run this program passing the optional parameters:
`python3 tasks_to_csv.py True True`
(where the first parameter represents the inclusion of completed tasks, and the second canceled tasks.)

#### Get Your Projects (very similar to tasks)

Run `python3 projects_to_csv` to get all incomplete projects as a CSV in this directory.

If you'd like to include completed and canceled projects, run this program passing the optional parameters:
`python3 projects_to_csv.py True True`
(where the first parameter represents the inclusion of completed projects, and the second canceled projects.)

### Get Your Tags or Areas

Run `python3 tags_to_csv` or `python3 tags_to_csv`.

_The outputs of these scripts will include extraneous columns, used for inter-operability with the CSV outputs of the other scripts._
