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
    
def circumference_of_circle(radius):
    return 2 * 3.1742 * radius

def perimeter_of_rectangle(l, b):
    return 2 * l *b

if __name__ == "__main__":
    print(perimeter_of_rectangle(5,10))