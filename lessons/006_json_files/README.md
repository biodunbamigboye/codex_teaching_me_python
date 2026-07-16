# Lesson 006: Reading And Writing JSON Files

Status: Assigned

Phase: Phase 3 - Files, Errors, And Data

Primary files:

- `study_report.py`
- `study_sessions.json`

Generated file: `study_summary.json`

Run command:

```bash
python3 lessons/006_json_files/study_report.py
```

## Goal

Read structured data from a JSON file, process it with Python, and write a calculated summary to another JSON file.

## Concepts To Practice

- JSON arrays and objects
- `json.load()` and `json.dump()`
- Opening files with a context manager
- Paths relative to the current Python file
- Calculating totals with `sum()`
- Separating loading, processing, saving, and printing

## PHP And JavaScript Bridges

- JSON objects become Python dictionaries, much like decoded associative arrays in PHP or objects in JavaScript.
- `json.load()` reads JSON from an open file; `json.loads()` parses JSON from a string.
- Python's `with` block closes a file automatically after the block finishes.

## Assignment

Create `study_report.py` and `study_sessions.json`.

Requirements:

- Import `json` and `Path` from `pathlib`.
- Put at least three session objects in the input JSON file.
- Give each session `topic`, `minutes`, and `completed` fields.
- Build input and output paths with `Path(__file__).with_name(...)`.
- Implement `load_sessions(file_path)` using a context manager and `json.load()`.
- Implement `calculate_total_minutes(sessions)` using `sum()`.
- Implement `build_summary(sessions)` returning `session_count`, `completed_count`, and `total_minutes`.
- Implement `save_summary(file_path, summary)` using a context manager and `json.dump(..., indent=2)`.
- In `main()`, print the sessions and summary, then save `study_summary.json`.
- Call `main()` through the standard entry-point guard.
- Include three PHP or JavaScript comparison comments.
- Do not use classes, external packages, user input, or `try`/`except` yet.

## Submission Evidence

Command run:

```bash
python3 lessons/006_json_files/study_report.py
```

Result:

```text
Pending submission.
```

## Attempt History

| Attempt | Result | Teacher note |
| --- | --- | --- |
| First attempt | Pending | Create the JSON input and report script, run them, then submit the output and reflection. |

## Accepted Version

Accepted files: pending

Teacher score: pending

Key reasons it passed:

- Pending evaluation.

## Reflection

Familiar:

- Pending submission.

Strange:

- Pending submission.

## Next Step

Create both assignment files, run the report, and submit its output and reflection for review.
