# Lesson 003: Functions And Return Values

Status: Accepted

Phase: Phase 2 - Functions And Modules

Primary file: `study_calculator.py`

Run command:

```bash
python3 lessons/003_functions/study_calculator.py
```

## Goal

Move repeated top-level script logic into functions that accept arguments, return values, and keep printing in the main script area.

## Concepts To Practice

- Defining functions with `def`
- Passing arguments
- Returning values with `return`
- Calling functions from top-level script code
- Keeping calculation and formatting logic reusable
- Avoiding unnecessary classes

## PHP And JavaScript Bridges

- Python functions are reusable like PHP and JavaScript functions.
- Python uses `def function_name(...):` instead of `function`, arrow functions, or PHP method syntax.
- Python functions should return useful values when the caller needs the result; printing inside every function makes code harder to reuse.

## Assignment

Create `study_calculator.py`.

Requirements:

- Define a `learner` dictionary with `full_name`, `daily_minutes`, `current_lesson`, and `primary_goal`.
- Define a `topics` list.
- Make each item in `topics` a dictionary with `name`, `status`, and `difficulty`.
- Include at least five topics.
- Define `calculate_weekly_minutes(daily_minutes)`.
- Define `format_topic(index, topic)`.
- Define `count_topics_by_status(topics, status)`.
- Define `get_pace_message(daily_minutes)`.
- Call each function from the main script area and print the returned results.
- Make at least two functions use `return`.
- Use a loop to print formatted topics by calling `format_topic`.
- Use `count_topics_by_status` at least twice with different statuses.
- Include three short comments comparing Python functions with PHP or JavaScript functions.
- Do not use classes, imports, or user input.

## Submission Evidence

Command run:

```bash
python3 lessons/003_functions/study_calculator.py
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
| First attempt | Cleanup required | Strong return-value work. Fix human numbering, Python naming style, semicolon usage, and the typing comment. |
| Second attempt | Cleanup required | Most cleanup landed, but `index - 1` made numbering start at 0 again. |
| Accepted attempt | Accepted | Functions return values correctly, topic numbering starts at 1, and status counting works. |

## Accepted Version

Accepted file: `lessons/003_functions/study_calculator.py`

Teacher score: 95 / 100

Key reasons it passed:

- Functions are defined with `def` and return useful values.
- Arguments are passed correctly from the main script area.
- The loop calls `format_topic` and prints human-friendly topic numbers.
- `count_topics_by_status` works for multiple statuses.

## Reflection

Familiar:

- `return` is a consistent way to return values from a function across JavaScript, PHP, and Python.

Strange:

- JavaScript arrow functions and PHP closures can read outside variables in familiar ways; Python's equivalent has not been explored yet.

## Next Step

Move to Lesson 004: Modules And Imports.
