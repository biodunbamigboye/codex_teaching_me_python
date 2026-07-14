
from study_helpers import calculate_weekly_minutes
from study_helpers import format_topic
from study_helpers import count_topics_by_status
from study_helpers import get_pace_message
from study_helpers import circumference_of_circle
from study_helpers import perimeter_of_rectangle
import study_helpers


learner = {
    'full_name': 'Biodun Bamigboye',
    'daily_minutes': 45,
    'current_lesson' : 'Functions and Return Values',
    'primary_goal' : 'Understand How Python and Return Function Works in Python'
}

topics = [
    {'name': 'introduction', 'status': 'done', 'difficulty' : 'beginner'},
    {'name': 'Variables', 'status': 'done', 'difficulty': 'beginner'},
    {'name': 'functions', 'status': 'in_progress', 'difficulty': 'beginner'},
    {'name': 'loops', 'status': 'pending', 'difficulty': 'intermediate'},
    {'name': 'logical gate', 'status': 'pending', 'difficulty': 'intermediate'}
]

print(f"My Daily minutes is {learner['daily_minutes']}")

print(f"My Weekly work time is {calculate_weekly_minutes(learner['daily_minutes'])}")

for index,topic in enumerate(topics, start=1):
    print (f"Here is a formatted version of a topic: {format_topic(index, topic)}")


print (f"We have {count_topics_by_status(topics,'done')} topics that is already completed")
print (f"We have {count_topics_by_status(topics,'pending')} topics that is yet to be done")

print (get_pace_message(learner['daily_minutes']))

# Python Import starts with from and not import keyword like Javascript
# Php supports separating multiple methods by comma in Import, I am not sure if python supports it
# Php include requires file extension, python already recognize the file like a module

print(f"The Circumference of a circle with radius 21 is {circumference_of_circle(21)}")
print(f"The perimeter of rectangle with Length of 4 and bread of 5 is {perimeter_of_rectangle(4,5)}")
print(f"The perimeter of rectangle with Length of 4 and bread of 5 is {study_helpers.perimeter_of_rectangle(4,5)}")