# Python Progress

Started: 2026-07-03

Learner: Biodun Bamigboye

Teacher: Codex

Repository: https://github.com/biodunbamigboye/codex_teaching_me_python

## Current Status

- Current phase: Phase 2 - Functions And Modules
- Current lesson: Lesson 004 - Modules And Imports
- Current assignment: `lessons/004_modules/main.py`
- Current lesson notes: `lessons/004_modules/README.md`
- Submission status: assigned

## Learning Defaults

- Pace: daily 45 minutes
- Web path: FastAPI first, Django after FastAPI confidence
- Long-term path: AI, ML, Data Science, RAG, and LLM orchestration after Python and backend fundamentals
- Feedback style: teacher strict

## Strengths Observed

- Strong PHP background
- Strong JavaScript background
- Backend learning goal is clear
- Long-term AI/ML/Data Science/RAG goal is now explicit
- Willing to learn publicly and iteratively

## Concepts To Watch

- Python indentation rules
- `snake_case` naming
- `None` vs `null`
- Lists vs arrays
- Dictionaries vs PHP associative arrays and JS objects
- Avoiding unnecessary classes too early
- Avoiding advanced AI tooling before Python foundations are strong

## Progress Log

| Date | Event | Evidence | Teacher Notes |
| --- | --- | --- | --- |
| 2026-07-03 | Learning repo initialized | README, instructions, progress tracker | Start small, write code daily, and do not skip running tasks locally. |
| 2026-07-03 | Lesson 001 first attempt submitted | `python3 lessons/001_foundations/profile_card.py` exited successfully, but the file had 0 lines and printed nothing. | Running the command was good, but an empty script does not meet the assignment. Rewrite required. |
| 2026-07-03 | Lesson 001 second attempt submitted | Script runs and prints six lines using f-strings. | Good improvement. Cleanup required: use `weekly_minutes` in the output, improve wording/capitalization, and submit the short reflection. |
| 2026-07-03 | Lesson 001 third attempt submitted | Script runs, prints `weekly_minutes`, uses required variables, list, f-strings, and comparison comments. | Python requirements mostly met. Final polish required: improve two output sentences and submit the short reflection. |
| 2026-07-03 | Lesson 001 accepted | Script runs and includes required variables, list usage, calculation, f-strings, comments, and reflection. | Accepted with polish notes. Next time, send reflection in the chat unless the task asks for it inside the script. |
| 2026-07-03 | Long-term AI path added | Roadmap expanded to include Data Science, Machine Learning, AI applications, and LLM orchestration. | Good ambition. We will not skip foundations; the AI path comes after Python and backend confidence. |
| 2026-07-03 | RAG path added | Roadmap expanded to include Retrieval-Augmented Generation as its own future phase. | RAG will come after AI application basics, with focus on retrieval quality, grounding, and source-aware answers. |
| 2026-07-03 | Lesson 002 first attempt submitted | Script runs and prints learner data, five topics, joined topic names, and pace status. | Good recovery from the `join` error. Cleanup required: print the learner profile more readably, remove duplicated `daily_minutes`, fix style spacing, and submit reflection. |
| 2026-07-03 | Lesson 002 second attempt submitted | Script runs, learner profile is more readable, `if` now reads from `learner["daily_minutes"]`, and reflection was submitted. | Near pass. One required fix: `len(topics)` is being printed as literal text instead of evaluated. |
| 2026-07-03 | Lesson 002 accepted | Script runs and correctly uses a learner dictionary, list of topic dictionaries, `enumerate`, `len`, `join`, and `if`. | Accepted with polish notes. Next focus: functions that return values instead of doing everything at top level. |
| 2026-07-03 | Lesson documentation standard added | `docs/LESSON_TEMPLATE.md`, lesson READMEs for Lessons 001-003 | Each lesson should now carry its own assignment, run evidence, attempt history, accepted version, reflection, and next step. |
| 2026-07-05 | Lesson 003 first attempt submitted | Script runs and uses four functions with return values, a topics loop, status counting, and pace messaging. | Strong first attempt. Cleanup required: number topics from 1, use `snake_case`, remove the semicolon, and correct the comment about Python typing. |
| 2026-07-05 | Lesson 003 second attempt submitted | Script runs and fixes `snake_case`, semicolon usage, and the typing comment. | Near pass. One bug remains: `index - 1` makes the displayed topic numbers start at 0 again. |
| 2026-07-05 | Lesson 003 accepted | Script runs and correctly uses functions, arguments, return values, status counting, pace messaging, and human-friendly numbering. | Accepted with polish notes. Next focus: split reusable functions into modules and import them. |

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

### 2026-07-03 - Lesson 002 First Attempt

Score: 82 / 100

- Correctness: 35 / 40 - `learner` is a dictionary, `topics` is a list of dictionaries, the loop prints numbered topics, `len`, `join`, and `if` are used, and the script runs successfully.
- Readability: 15 / 20 - output works, but `print(f"{learner}")` and `print(len(topics))` are too raw for a user-facing script.
- Pythonic style: 16 / 20 - good beginner fix using `topic_names.append(topic["name"])`; improve spacing around dictionary colons and keyword arguments.
- Edge cases: 8 / 10 - the `if` should read from `learner["daily_minutes"]` instead of creating a second `daily_minutes` variable.
- Reflection and explanation: 8 / 10 - the output was submitted, but the required familiar/strange reflection was not included.

Teacher decision: cleanup required before Lesson 002 can be accepted.

### 2026-07-03 - Lesson 002 Second Attempt

Score: 90 / 100

- Correctness: 37 / 40 - the script runs, uses the required dictionary/list structures, loops through topics, joins topic names, and uses `if` correctly. `len(topics)` is currently printed as literal text.
- Readability: 17 / 20 - learner output is clearer, though it is a bit dense as one long line.
- Pythonic style: 18 / 20 - good use of dictionary key access and `enumerate(..., start=1)`.
- Edge cases: 8 / 10 - the script now avoids duplicating `daily_minutes`; one output line still does not evaluate the count.
- Reflection and explanation: 10 / 10 - strong reflection on dictionary access versus JavaScript dot notation and PHP associative arrays.

Teacher decision: one-line fix required before acceptance.

### 2026-07-03 - Lesson 002 Accepted

Score: 93 / 100

- Correctness: 40 / 40 - the script runs successfully and uses the required dictionary, list of dictionaries, loop, `len`, `join`, and `if` logic.
- Readability: 17 / 20 - output is understandable; the learner profile line is still dense and could be split across multiple lines.
- Pythonic style: 17 / 20 - good use of `enumerate(..., start=1)` and dictionary key access; improve spacing around dictionary colons in future work.
- Edge cases: 9 / 10 - the code reads `daily_minutes` from `learner`, which avoids duplicate state.
- Reflection and explanation: 10 / 10 - strong reflection on Python dictionary access versus JavaScript dot notation and PHP associative arrays.

Teacher decision: Lesson 002 accepted. Move to Lesson 003.

### 2026-07-05 - Lesson 003 First Attempt

Score: 86 / 100

- Correctness: 36 / 40 - the script runs, defines the required functions, returns values, counts statuses, and calls the functions from the main script. The topic numbering starts at 0 instead of 1.
- Readability: 17 / 20 - output is understandable, though `done beginner` should be formatted more clearly as `done - beginner`.
- Pythonic style: 15 / 20 - function names are good, but `dailyMinutes` should be `daily_minutes`, `count+=1` should be spaced as `count += 1`, and `return count;` should not use a semicolon.
- Edge cases: 8 / 10 - the status counter works for matching statuses; the display number should be human-friendly.
- Reflection and explanation: 10 / 10 - strong comparison of `return` across PHP, JavaScript, and Python, plus a useful question about scope and reading outside variables.

Teacher decision: cleanup required before Lesson 003 can be accepted.

### 2026-07-05 - Lesson 003 Second Attempt

Score: 91 / 100

- Correctness: 38 / 40 - the script runs and the function structure works. The topic display still starts at 0 because `format_topic(index - 1, topic)` subtracts from the human-friendly index.
- Readability: 17 / 20 - output is understandable; topic formatting should include a separator between status and difficulty.
- Pythonic style: 17 / 20 - `daily_minutes` and semicolon cleanup are fixed. Keep improving spacing: `count += 1`, `for index, topic`, and `print(...)`.
- Edge cases: 9 / 10 - status counting and pace logic are working.
- Reflection and explanation: 10 / 10 - previous reflection remains strong and relevant.

Teacher decision: one-line fix required before acceptance.

### 2026-07-05 - Lesson 003 Accepted

Score: 95 / 100

- Correctness: 40 / 40 - the script runs and meets the required function, argument, return value, loop, counting, and pace-message behavior.
- Readability: 18 / 20 - output is clear and topic formatting is improved.
- Pythonic style: 18 / 20 - `snake_case`, `return`, and spacing are much improved; keep tightening spacing around commas and function calls.
- Edge cases: 9 / 10 - status counting works for the statuses used.
- Reflection and explanation: 10 / 10 - strong reflection on function returns and variable scope compared with PHP and JavaScript.

Teacher decision: Lesson 003 accepted. Move to Lesson 004.

## Current Assignment

Lesson 004 is assigned in `PYTHON_LEARNING_INSTRUCTIONS.md`.

Expected file:

```text
lessons/
  004_modules/
    main.py
```

The next task focuses on moving reusable functions into another file and importing them into a main script.

## Next Teacher Action

After the learner submits Lesson 004, Codex should:

- run or inspect the submitted script
- evaluate it using the rubric
- update this progress file with the result
- assign corrections or Lesson 005
