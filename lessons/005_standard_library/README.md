# Lesson 005: Default Arguments, Scope, And The Standard Library

Status: Accepted

Phase: Phase 2 - Functions And Modules

Primary file: `study_planner.py`

Run command:

```bash
python3 lessons/005_standard_library/study_planner.py
```

## Goal

Use default and keyword arguments, understand local versus module scope, work with dates from Python's standard library, and give a script an explicit entry point.

## Concepts To Practice

- Default function arguments
- Keyword arguments
- Module-level constants and local scope
- `date` and `timedelta` from `datetime`
- A `main()` function
- The `if __name__ == "__main__":` entry-point guard

## PHP And JavaScript Bridges

- Default arguments exist in all three languages, but Python keyword arguments make call sites especially readable.
- A Python module-level name resembles a JavaScript module variable or a PHP name declared outside a function.
- Python's standard library provides date tools without installing an external package.

## Assignment

Create `study_planner.py`.

Requirements:

- Import `date` and `timedelta` from `datetime`.
- Define `DEFAULT_DAILY_MINUTES = 45` at module level.
- Define `calculate_total_minutes(study_days, daily_minutes=DEFAULT_DAILY_MINUTES)`.
- Define `build_study_message(topic, daily_minutes=DEFAULT_DAILY_MINUTES)`.
- Define `get_target_date(days_from_today=7)` using `date.today()` and `timedelta`.
- Define `main()` and keep all print calls inside it.
- Demonstrate a default argument and a keyword argument such as `daily_minutes=60`.
- Print a seven-day total and a fourteen-day target date.
- Call `main()` through `if __name__ == "__main__":`.
- Read, but do not modify, `DEFAULT_DAILY_MINUTES` inside functions.
- Include three short PHP or JavaScript comparison comments.
- Do not use classes, external packages, or user input.

## Submission Evidence

Command run:

```bash
python3 lessons/005_standard_library/study_planner.py
```

Result:

```text
Total minutes for daily study is 350
Seven days total minutes is 315
I would be studying How to learn python leveraging codex daily for 45
Fourteen days target date is: 2026-07-29
```

## Attempt History

| Attempt | Result | Teacher note |
| --- | --- | --- |
| First attempt | Cleanup required | All required behavior works. Clean whitespace and import formatting, use the conventional entry-point syntax, improve output units, correct the comparison comments, and submit the reflection. |
| Accepted attempt | Accepted | Defaults, keyword arguments, scope, date arithmetic, `main()`, the entry-point guard, comments, reflection, and whitespace all meet the requirements. |

## Accepted Version

Accepted file: `study_planner.py`

Teacher score: 96 / 100

Key reasons it passed:

- Default and keyword arguments are demonstrated correctly.
- The module constant is used without being modified.
- `date` and `timedelta` calculate the target date correctly.
- Printing is contained in `main()` and the entry-point guard works.

## Reflection

Familiar:

- Python's `print()` feels similar to JavaScript's `console.log()` because both display values while a program runs.

Strange:

- Leaving two blank lines between top-level Python functions feels unusual compared with familiar PHP and JavaScript formatting.

## Next Step

Move to Lesson 006: Reading And Writing JSON Files.
