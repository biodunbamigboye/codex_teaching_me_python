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

def calculate_weekly_minutes(daily_minutes): 
    return daily_minutes * 7

def format_topic(index, topic):
    return f"{index}. {topic['name']} - {topic['status']} - {topic['difficulty']}"

def count_topics_by_status(topics, status):
    count = 0
    
    for topic in topics:
        if topic['status'] == status:
            count += 1
            
    return count

def get_pace_message(daily_minutes):
    if daily_minutes >= 45:
        return "Your daily pace is strong"
    else:
        return "Your daily pace is weak"
    
print(f"My Daily minutes is {learner['daily_minutes']}")

print(f"My Weekly work time is {calculate_weekly_minutes(learner['daily_minutes'])}")

for index,topic in enumerate(topics, start=1):
    print (f"Here is a formatted version of a topic: {format_topic(index, topic)}")


print (f"We have {count_topics_by_status(topics,'done')} topics that is already completed")
print (f"We have {count_topics_by_status(topics,'pending')} topics that is yet to be done")

print (get_pace_message(learner['daily_minutes']))

# PHP and Python are dynamically typed, and Python can also use optional type hints.
# Return is a consistent way of returning values across, Javascript, PHP and Python
# In the past I believed Indentation is a bad Idea due to my experience in PHP and Javascript, Python makes me know it now aids clean code and reduce braces a lot.