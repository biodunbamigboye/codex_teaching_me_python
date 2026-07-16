from study_helpers import (
    calculate_weekly_minutes,
    format_topic,
    count_topics_by_status,
    get_pace_message,
)


learner = {
    'full_name': 'Biodun Bamigboye',
    'daily_minutes': 45,
    'current_lesson': 'Modules and Imports',
    'primary_goal': 'Understand Imports and Modules in Python'
}

topics = [
    {'name': 'introduction', 'status': 'done', 'difficulty': 'beginner'},
    {'name': 'Variables', 'status': 'done', 'difficulty': 'beginner'},
    {'name': 'functions', 'status': 'in_progress', 'difficulty': 'beginner'},
    {'name': 'loops', 'status': 'pending', 'difficulty': 'intermediate'},
    {'name': 'logical gate', 'status': 'pending', 'difficulty': 'intermediate'}
]

print(f"My Daily minutes is {learner['daily_minutes']}")

print(f"My Weekly work time is {calculate_weekly_minutes(learner['daily_minutes'])}")

for index, topic in enumerate(topics, start=1):
    print(f"Here is a formatted version of a topic: {format_topic(index, topic)}")


print(f"We have {count_topics_by_status(topics, 'done')} topics that is already completed")
print(f"We have {count_topics_by_status(topics, 'pending')} topics that is yet to be done")

print(get_pace_message(learner['daily_minutes']))

# Python modules are reusable files, similar to JavaScript ES modules.
# Python's "from module import name" resembles a JavaScript named import.
# Python executes a module on its first import and then caches it.
