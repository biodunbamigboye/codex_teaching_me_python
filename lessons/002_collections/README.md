# Lesson 002: Lists, Dictionaries, And Loops

Status: Accepted

Phase: Phase 1 - Python Foundations

Primary file: `learning_inventory.py`

Run command:

```bash
python3 lessons/002_collections/learning_inventory.py
```

## Goal

Track a learning inventory using Python dictionaries, a list of dictionaries, loops, `len`, `join`, and a simple `if` statement.

## Concepts Practiced

- Dictionaries for structured learner data
- Lists of dictionaries for topic records
- Dictionary key access
- `for` loops
- `enumerate(..., start=1)`
- `len`
- `join`
- Conditional logic with `if` and `else`

## PHP And JavaScript Bridges

- Python dictionaries feel close to PHP associative arrays and JavaScript objects.
- Python lists feel close to JavaScript arrays and PHP arrays for beginner usage.
- Python dictionary access uses bracket syntax like `learner["daily_minutes"]`; JavaScript dot access does not transfer directly.

## Assignment

Create a script that tracks Biodun's learning inventory.

Requirements included:

- Define a `learner` dictionary with `full_name`, `daily_minutes`, `current_phase`, and `primary_goal`.
- Define a `topics` list.
- Make each topic a dictionary with `name`, `status`, and `difficulty`.
- Include at least four topics.
- Print the learner profile using f-strings.
- Print the number of topics using `len(topics)`.
- Loop through topics and print them as a numbered list.
- Use `join` to print all topic names in one sentence.
- Use an `if` statement to judge study pace.
- Include three comments comparing Python lists and dictionaries with PHP or JavaScript.
- Do not use classes, imports, or user input.

## Submission Evidence

Command run:

```bash
python3 lessons/002_collections/learning_inventory.py
```

Result:

```text
Learner: Biodun Bamigboye, Learning Duration per Day: 45, Learning Phase: Lesson 2, Primary Goal: Master Python Programming Language
Total Topics: 5
Topic 1 is Introduction
Topic 2 is Variables
Topic 3 is Lists
Topic 4 is Loops
Topic 5 is Logical Operations
My Learning topics for my Python course are Introduction, Variables, Lists, Loops, Logical Operations.
Your daily pace is strong
```

## Attempt History

| Attempt | Result | Teacher note |
| --- | --- | --- |
| First attempt | Cleanup required | The script ran and recovered from a `join` issue, but learner output was raw, `daily_minutes` was duplicated, and reflection was missing. |
| Second attempt | One-line fix required | Output improved and reflection was strong, but `len(topics)` was printed as literal text instead of being evaluated. |
| Accepted attempt | Accepted | The script correctly used a learner dictionary, list of topic dictionaries, `enumerate`, `len`, `join`, and `if`. |

## Accepted Version

Accepted file: `learning_inventory.py`

Teacher score: `93 / 100`

Key reasons it passed:

- `learner` and `topics` used the required data structures.
- The loop printed all topics clearly.
- `len`, `join`, and `if` were used correctly.
- The reflection showed good comparison between Python dictionaries, JavaScript objects, and PHP associative arrays.

Polish notes to remember:

- Split dense output into multiple lines when readability would improve.
- Keep spacing around dictionary colons consistent.
- Avoid duplicate state when a value already lives inside a dictionary.

## Reflection

Familiar:

- Lists and dictionaries are conceptually close to arrays and objects from PHP and JavaScript.

Strange:

- Python dictionary access needs bracket syntax for keys, even when the structure looks object-like.

## Next Step

Lesson 003 moves repeated script logic into functions that accept arguments and return useful values.
