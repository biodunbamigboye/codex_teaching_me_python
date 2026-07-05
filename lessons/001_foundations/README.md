# Lesson 001: Python From PHP/JS Eyes

Status: Accepted

Phase: Phase 1 - Python Foundations

Primary file: `profile_card.py`

Run command:

```bash
python3 lessons/001_foundations/profile_card.py
```

## Goal

Introduce the learner with simple Python variables, strings, numbers, booleans, a list, basic calculation, f-strings, and beginner comparison notes from PHP and JavaScript.

## Concepts Practiced

- Variables with `snake_case` names
- Strings, numbers, booleans, and lists
- Basic arithmetic
- f-string output
- `join` for readable list output
- Beginner Python comments

## PHP And JavaScript Bridges

- Python variables do not use `$`, `let`, or `const`.
- Python does not require semicolons at the end of statements.
- Python f-strings fill the interpolation role that PHP and JavaScript handle with different string syntax.

## Assignment

Create a Python script that introduces Biodun as a learner.

Requirements included:

- Define `full_name`, `language_strengths`, `years_with_php`, `years_with_js`, `learning_goal`, `is_committed`, and `daily_minutes`.
- Make `language_strengths` a list.
- Calculate `weekly_minutes`.
- Print at least five clear f-string lines.
- Print language strengths as one readable sentence.
- Include three short comments comparing Python with PHP or JavaScript.
- Do not use classes or semicolons.

## Submission Evidence

Command run:

```bash
python3 lessons/001_foundations/profile_card.py
```

Result:

```text
My Weekly learning minutes is 315 minutes
My name is Biodun Bamigboye
I have been working with PHP for 10 years.
I learned Javascript 5 years ago.
I will study Python for 45 daily.
My learning goal is to Create APIs and full-stack Python Apps, leverage Python for AI, Machine Learning, Data Science and LLMs
My Language strengths are PHP, JavaScript
Familiar: String data type are defined the same way in Python, PHP and Javascript
Strange: using f to precede a string to be able to interpolate variable seems magical because in PHP and Javascript except for concatenation symbol, there is no magical letter to enable interpolation
```

## Attempt History

| Attempt | Result | Teacher note |
| --- | --- | --- |
| First attempt | Rewrite required | The command ran, but the script was empty and printed nothing. |
| Second attempt | Cleanup required | Required variables and f-strings were added, but `weekly_minutes` was calculated without being shown and reflection was missing. |
| Third attempt | Final polish required | Requirements were mostly met, but output wording and reflection still needed cleanup. |
| Accepted attempt | Accepted | The script ran and included the required variables, list usage, calculation, f-strings, comments, and reflection. |

## Accepted Version

Accepted file: `profile_card.py`

Teacher score: `91 / 100`

Key reasons it passed:

- Required variables were present and named with `snake_case`.
- `weekly_minutes` was calculated from `daily_minutes`.
- f-strings and `join` were used successfully.
- The script stayed simple and beginner-appropriate.

Polish notes to remember:

- Prefer `45 minutes daily` over `45 daily`.
- Avoid trailing spaces in output.
- Submit reflections in chat unless a lesson asks for them inside the script.

## Reflection

Familiar:

- String data types feel familiar across Python, PHP, and JavaScript.

Strange:

- Prefixing a string with `f` for interpolation felt unusual compared with PHP and JavaScript habits.

## Next Step

Lesson 002 moves from simple variables into lists, dictionaries, and loops.
