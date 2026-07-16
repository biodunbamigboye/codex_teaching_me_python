from datetime import date, timedelta

DEFAULT_DAILY_MINUTES = 45


def calculate_total_minutes(study_days, daily_minutes=DEFAULT_DAILY_MINUTES):
    return study_days * daily_minutes


def build_study_message(topic, daily_minutes=DEFAULT_DAILY_MINUTES):
    return f"I will study {topic} for {daily_minutes} minutes daily."


def get_target_date(days_from_today=7):
    return date.today() + timedelta(days=days_from_today)


def main():
    print(f"Total minutes for daily study is {calculate_total_minutes(study_days=7, daily_minutes=50)}")
    print(f"Seven days total minutes is {calculate_total_minutes(study_days=7)}")
    print(build_study_message("How to learn python leveraging codex"))
    print(f"Fourteen days target date is: {get_target_date(days_from_today=14)}")


if __name__ == "__main__":
    main()


# JavaScript has no native named arguments; object destructuring can imitate them.
# Python keyword arguments use name=value when calling a function.
# JavaScript and PHP have const; Python uses uppercase naming by convention.

