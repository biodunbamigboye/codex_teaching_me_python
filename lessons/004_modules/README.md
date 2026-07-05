# Lesson 004: Modules And Imports

Status: Assigned

Phase: Phase 2 - Functions And Modules

Primary files:

- `main.py`
- `study_helpers.py`

Run command:

```bash
python3 lessons/004_modules/main.py
```

## Goal

Learn how to move reusable functions into a separate Python file and import them into a main script.

## Concepts To Practice

- Creating a module
- Importing functions from another file
- Keeping data and script output in `main.py`
- Keeping reusable logic in `study_helpers.py`
- Avoiding copy-paste logic

## PHP And JavaScript Bridges

- Python modules are plain `.py` files that can be imported.
- This is closer to JavaScript `import` than PHP `include`, because you usually import named functions or modules.
- Python imports depend on where you run the script from and how files are arranged.

## Assignment

Create `main.py` and `study_helpers.py`.

Requirements:

- Put helper functions in `study_helpers.py`.
- Put learner data, topics data, loops, and print calls in `main.py`.
- Import helper functions from `study_helpers.py`.
- Use `enumerate(topics, start=1)` for human-friendly numbering.
- Use `count_topics_by_status` at least twice.
- Include three short comments comparing Python imports/modules with PHP or JavaScript.
- Do not use classes, external packages, or user input.

## Submission Evidence

Command run:

```bash
python3 lessons/004_modules/main.py
```

Result:

```text
Pending submission.
```

## Attempt History

| Attempt | Result | Teacher note |
| --- | --- | --- |
| First attempt | Pending | Submit the script after running it locally. |

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

Write `study_helpers.py` and `main.py`, run the command, then submit the output and reflection for review.
