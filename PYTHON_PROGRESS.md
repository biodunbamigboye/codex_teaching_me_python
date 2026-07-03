# Python Progress

Started: 2026-07-03

Learner: Biodun Bamigboye

Teacher: Codex

Repository: https://github.com/biodunbamigboye/codex_teaching_me_python

## Current Status

- Current phase: Phase 1 - Python Foundations
- Current lesson: Lesson 002 - Lists, Dictionaries, And Loops
- Current assignment: `lessons/002_collections/learning_inventory.py`
- Submission status: assigned

## Learning Defaults

- Pace: daily 45 minutes
- Web path: FastAPI first, Django after FastAPI confidence
- Feedback style: teacher strict

## Strengths Observed

- Strong PHP background
- Strong JavaScript background
- Backend learning goal is clear
- Willing to learn publicly and iteratively

## Concepts To Watch

- Python indentation rules
- `snake_case` naming
- `None` vs `null`
- Lists vs arrays
- Dictionaries vs PHP associative arrays and JS objects
- Avoiding unnecessary classes too early

## Progress Log

| Date | Event | Evidence | Teacher Notes |
| --- | --- | --- | --- |
| 2026-07-03 | Learning repo initialized | README, instructions, progress tracker | Start small, write code daily, and do not skip running tasks locally. |
| 2026-07-03 | Lesson 001 first attempt submitted | `python3 lessons/001_foundations/profile_card.py` exited successfully, but the file had 0 lines and printed nothing. | Running the command was good, but an empty script does not meet the assignment. Rewrite required. |
| 2026-07-03 | Lesson 001 second attempt submitted | Script runs and prints six lines using f-strings. | Good improvement. Cleanup required: use `weekly_minutes` in the output, improve wording/capitalization, and submit the short reflection. |
| 2026-07-03 | Lesson 001 third attempt submitted | Script runs, prints `weekly_minutes`, uses required variables, list, f-strings, and comparison comments. | Python requirements mostly met. Final polish required: improve two output sentences and submit the short reflection. |
| 2026-07-03 | Lesson 001 accepted | Script runs and includes required variables, list usage, calculation, f-strings, comments, and reflection. | Accepted with polish notes. Next time, send reflection in the chat unless the task asks for it inside the script. |

## Evaluations

### 2026-07-03 - Lesson 001 First Attempt

Score: 5 / 100

- Correctness: 0 / 40 - no required variables, calculation, or output were implemented.
- Readability: 0 / 20 - there is no code to read yet.
- Pythonic style: 0 / 20 - there is no Python syntax to evaluate yet.
- Edge cases: 0 / 10 - not applicable until the script exists.
- Reflection and explanation: 5 / 10 - the run command was reported, but the submission did not include whether it worked, any error output, or what felt familiar/strange.

Teacher decision: rewrite required.

### 2026-07-03 - Lesson 001 Second Attempt

Score: 73 / 100

- Correctness: 33 / 40 - required variables exist, `language_strengths` is a list, `weekly_minutes` is calculated, and the script prints clear f-string lines. `weekly_minutes` is calculated but not shown in the output.
- Readability: 14 / 20 - output is understandable, but some wording needs cleanup: "I would learn python for 45 daily" should be clearer, and capitalization should be consistent.
- Pythonic style: 16 / 20 - good use of `snake_case`, f-strings, booleans, and `', '.join(language_strengths)`.
- Edge cases: 7 / 10 - this is a simple script, but the output should include units like "years" and "minutes" clearly.
- Reflection and explanation: 3 / 10 - the command and output were shared, but the familiar/strange reflection was not included.

Teacher decision: cleanup required before Lesson 002.

### 2026-07-03 - Lesson 001 Third Attempt

Score: 86 / 100

- Correctness: 39 / 40 - all required variables are defined, `language_strengths` is a list, `weekly_minutes` is calculated and printed, and the script runs successfully.
- Readability: 16 / 20 - output is clear enough, but "I would learn Python for 45 daily" should be rewritten with units, and capitalization should be consistent.
- Pythonic style: 18 / 20 - good use of `snake_case`, f-strings, booleans, and `', '.join(language_strengths)`.
- Edge cases: 8 / 10 - the script is simple and appropriate; output still has a trailing space after the language strengths sentence.
- Reflection and explanation: 5 / 10 - the command and output were shared, but the required familiar/strange reflection is still missing.

Teacher decision: final polish required before Lesson 002.

### 2026-07-03 - Lesson 001 Accepted

Score: 91 / 100

- Correctness: 40 / 40 - the script defines the required variables, uses a list, calculates and prints `weekly_minutes`, and runs successfully.
- Readability: 17 / 20 - output is clear, with minor wording issues such as "45 daily" instead of "45 minutes daily".
- Pythonic style: 18 / 20 - strong beginner use of `snake_case`, f-strings, booleans, and `join`.
- Edge cases: 8 / 10 - appropriate for the assignment; watch trailing spaces in output.
- Reflection and explanation: 8 / 10 - useful reflections were submitted. They were printed by the script, which is acceptable here, but future reflections should be sent in the chat unless requested in code.

Teacher decision: Lesson 001 accepted. Move to Lesson 002.

## Current Assignment

Lesson 002 is assigned in `PYTHON_LEARNING_INSTRUCTIONS.md`.

Expected file:

```text
lessons/
  002_collections/
    learning_inventory.py
```

The next task focuses on Python lists, dictionaries, loops, `len`, `join`, and simple `if` logic.

## Next Teacher Action

After the learner submits Lesson 002, Codex should:

- run or inspect the submitted script
- evaluate it using the rubric
- update this progress file with the result
- assign corrections or Lesson 003
