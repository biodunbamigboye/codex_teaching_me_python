# Lesson 004: Modules And Imports

Status: Accepted

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
My Daily minutes is 45
My Weekly work time is 315
Here is a formatted version of a topic: 1. introduction - done - beginner
Here is a formatted version of a topic: 2. Variables - done - beginner
Here is a formatted version of a topic: 3. functions - in_progress - beginner
Here is a formatted version of a topic: 4. loops - pending - intermediate
Here is a formatted version of a topic: 5. logical gate - pending - intermediate
We have 2 topics that is already completed
We have 2 topics that is yet to be done
Your daily pace is strong
```

## Attempt History

| Attempt | Result | Teacher note |
| --- | --- | --- |
| First attempt | Cleanup required | The module split and imports work. Remove unrelated geometry code, use one import style, fix spacing, and replace inaccurate comparison comments. |
| Second attempt | Final polish required | Import cleanup, scope cleanup, comments, and reflection are correct. Apply standard Python spacing in both files before acceptance. |
| Accepted attempt | Accepted | Both files run and compile, imports and module boundaries are correct, and whitespace/style corrections are complete. |

## Accepted Version

Accepted files: `main.py` and `study_helpers.py`

Teacher score: 97 / 100

Key reasons it passed:

- Reusable functions live in `study_helpers.py`.
- `main.py` imports and calls the helpers without duplicating their logic.
- Topic numbering, status counting, and output are correct.
- Module comparison comments and reflection are accurate for this stage.

## Reflection

Familiar:

- Python modules feel similar to JavaScript ES modules because a specific function can be imported from another file.

Strange:

- PHP commonly organizes reusable code through namespaces, autoloading, `include`, or `require`, which feels different from Python's module imports.

## Next Step

Move to Lesson 005: Default Arguments, Scope, And The Standard Library.
