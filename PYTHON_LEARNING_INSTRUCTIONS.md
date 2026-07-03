# Python Learning Instructions

## Teaching Contract

Codex will teach Python like a real teacher, using your PHP and JavaScript background as leverage.

The style is teacher strict:

- Correctness matters.
- Clear naming matters.
- Pythonic style matters.
- You may be asked to rewrite work when the lesson has not landed yet.
- Mistakes will be treated as useful signals, not failure.

The goal is not to memorize Python syntax. The goal is to become fluent enough to build real backend projects with FastAPI, then Django.

## Study Rhythm

Default pace: daily 45 minutes.

Suggested session shape:

1. 5 minutes: review the previous lesson.
2. 15 minutes: learn one new concept.
3. 20 minutes: complete a practical task.
4. 5 minutes: record what was learned or where you got stuck.

If a task is not finished in one session, continue the next day. Do not rush through confusion.

## How To Use This Repo

Each practical task should eventually live in its own lesson folder:

```text
lessons/
  001_foundations/
    profile_card.py
```

For each submitted task:

- Run the code before asking for evaluation.
- Tell Codex what command you ran.
- Share any error message exactly as it appeared.
- Expect feedback on correctness, readability, Python style, and whether the solution matches the assignment.

Do not hide mistakes. The public record of fixes is part of the learning value.

## Roadmap

### Phase 0: Setup And Orientation

Goal: make the workspace ready and learn how Python code is run.

Topics:

- Python files and the interpreter
- Running scripts from the terminal
- Reading tracebacks
- Repo organization
- How Python differs from PHP and JavaScript at first glance

### Phase 1: Python Foundations

Goal: write simple Python scripts confidently.

Topics:

- Variables and naming
- Strings and f-strings
- Numbers and booleans
- `None` compared with `null`
- Lists, tuples, dictionaries, and sets
- `if`, `for`, and `while`
- Basic input and output

PHP/JS comparisons:

- Python uses indentation for blocks.
- Python variables do not use `$`, `let`, or `const`.
- Python lists are close to JS arrays, but dictionaries are closer to plain JS objects and PHP associative arrays.
- Python truthiness is familiar, but details differ.

### Phase 2: Functions And Modules

Goal: structure code into reusable pieces.

Topics:

- Defining functions
- Parameters and return values
- Default arguments
- Scope
- Imports
- Standard library basics
- Splitting code across files

PHP/JS comparisons:

- Python functions are first-class like JavaScript functions.
- Python imports are module-based and file-path-sensitive.
- Python has no arrow-function syntax.

### Phase 3: Files, Errors, And Data

Goal: work with real input and handle failure carefully.

Topics:

- Reading and writing files
- JSON
- CSV
- Exceptions
- `try` and `except`
- Custom error messages
- Small data-processing scripts

### Phase 4: Object-Oriented Python And Types

Goal: understand Python classes without overusing them.

Topics:

- Classes and instances
- Methods and `self`
- Dataclasses
- Type hints
- Simple domain modeling
- When not to use a class

PHP/JS comparisons:

- Python uses `self` explicitly in instance methods.
- Python classes are often lighter than PHP service-style classes.
- Dataclasses can replace a lot of boilerplate constructor code.

### Phase 5: Testing, Tooling, And Project Hygiene

Goal: build Python code that is easy to trust.

Topics:

- Virtual environments
- `pip`
- `pyproject.toml`
- `pytest`
- Assertions
- Formatting and linting basics
- Environment variables
- `.gitignore` discipline

### Phase 6: FastAPI

Goal: build useful APIs with Python.

Topics:

- FastAPI project structure
- Routes
- Request and response models
- Pydantic validation
- Path and query parameters
- Error responses
- Dependency injection basics
- SQLite-backed APIs
- Authentication basics
- Testing API endpoints

PHP/JS comparisons:

- FastAPI route handlers feel close to Express handlers, but type hints and validation do more work.
- Request validation is usually model-first instead of manual array/object checking.
- Async exists in Python, but it should be used intentionally.

### Phase 7: Django

Goal: understand the batteries-included Python web framework.

Topics:

- Projects and apps
- Models
- Migrations
- Views and URLs
- Templates
- Forms
- Admin
- Authentication
- Django REST Framework introduction

PHP/JS comparisons:

- Django is closer to Laravel than to Express.
- Django conventions are strong; fighting them usually creates unnecessary pain.
- The admin is a major productivity feature, not an afterthought.

## Lesson Format

Each lesson should include:

- Concept explanation
- PHP and JavaScript comparison
- Small Python examples
- Practical task
- Submission instructions
- Evaluation rubric
- Optional resource links
- Correction or rewrite instructions when needed

## Evaluation Rubric

Each practical task is evaluated out of 100:

- Correctness: 40
- Readability: 20
- Pythonic style: 20
- Edge cases: 10
- Reflection and explanation: 10

Strict feedback means:

- Code that works but is awkward will be accepted only with notes or a rewrite request.
- Code that copies PHP/JS habits into Python will be corrected.
- Over-engineering small tasks will be called out.
- Missing error output or missing run commands will count against the submission.

## Core References

- Python Tutorial: https://docs.python.org/3/tutorial/
- Python virtual environments: https://docs.python.org/3/tutorial/venv.html
- Python style guide: https://peps.python.org/pep-0008/
- FastAPI tutorial: https://fastapi.tiangolo.com/tutorial/
- Django tutorial: https://docs.djangoproject.com/en/5.2/intro/tutorial01/

Video resources should be used as supplements, not the main course. For each hard topic, prefer one targeted video search rather than a long playlist binge. Good searches include:

- `Python f-strings for beginners`
- `Python lists dictionaries tuples explained`
- `Python functions for JavaScript developers`
- `FastAPI crash course request validation`
- `Django for Laravel developers`

## First Practical Task

### Lesson 001: Python From PHP/JS Eyes

Create this folder and file:

```text
lessons/
  001_foundations/
    profile_card.py
```

Write a Python script that introduces you as a learner.

Requirements:

- Define variables for:
  - `full_name`
  - `language_strengths`
  - `years_with_php`
  - `years_with_js`
  - `learning_goal`
  - `is_committed`
  - `daily_minutes`
- `language_strengths` must be a list.
- Calculate `weekly_minutes` from `daily_minutes`.
- Print at least five clear lines using f-strings.
- Print your language strengths as one readable sentence.
- Include three short comments explaining Python differences you noticed compared with PHP or JavaScript.
- Do not use classes.
- Do not use semicolons.

Example command to run it:

```bash
python3 lessons/001_foundations/profile_card.py
```

When you submit, tell Codex:

- the command you ran
- whether it worked
- any error message if it failed
- one thing that felt familiar from PHP or JavaScript
- one thing that felt strange in Python

Evaluation focus:

- Script runs without errors.
- Variable names use `snake_case`.
- Output is readable.
- f-strings are used correctly.
- A list is used for language strengths.
- The solution stays simple.
