learner = {
    "full_name" : "Biodun Bamigboye",
    "daily_minutes" : 45,
    "current_phase" : "Lesson 2",
    "primary_goal" : "Master Python Programming Language"
}

topics = [
    {"name" : "Introduction", "status" : "completed", "difficulty": "beginner" },
    {"name" : "Variables", "status" : "completed", "difficulty" : "beginner"},
    {"name" : "Lists", "status": "in_progress", "difficulty": "beginner"},
    {"name" : "Loops", "status" : "pending", "difficulty": "intermediate"},
    {"name" : "Logical Operations" , "status" : "pending", "difficulty" : "intermediate"}
]

print(f"Learner: {learner['full_name']}, Learning Duration per Day: {learner['daily_minutes']}, Learning Phase: {learner['current_phase']}, Primary Goal: {learner['primary_goal']}")
print(f"Total Topics: {len(topics)}")

for index, topic in enumerate(topics, start=1):
    print(f"Topic {index} is {topic['name']}")
    
topic_names = []

for topic in topics:
    topic_names.append(topic['name'])
    
print(f"My Learning topics for my Python course are {', '.join(topic_names)}.")


if learner['daily_minutes'] >= 45:
    print("Your daily pace is strong")
else:
    print("The Daily pace needs more time")
    
# Python Dictionary looks like a combination of PHP associative array and Javascript Objects, it takes Object syntax from Javascript and  string key from PHP
# Python List is the same as Javascript Array and PHP Array, i assume there may be some differences in their internal implementation
# Python List of Objects is closer to Javascript implementation of the same concept"
