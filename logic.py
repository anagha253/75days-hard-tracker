from datetime import datetime, timedelta, date
import calendar
import json


def set_challenge():
    start_day = datetime.now().date()
    end_day = start_day + timedelta(days=75)
    return f"75 days hard challenge starts today:{start_day}  and ends: {end_day} "

tasks = ["1. Follow a diet. No cheat meals and no alcohol.",
         "2. Two 45-minute workouts per day. One must be outside.",
         "3. Drink 3L of water per day.",
         "4. Read 10 pages of a non-fiction book every day.",
         "5. Take a progress picture every day."]

FILE_NAME = "challenge_progress.json"

def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return {}

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def daily_progress():
    today = str(date.today())

    data = load_data()

    if today not in data:
        data[today] = {}

    print(f"\n75 HARD CHECKLIST — {today}\n")

    for task in tasks:
        answer = input(f"Did you complete {task}? (y/n): ").lower()

        data[today][task] = answer == "y"

    save_data(data)

    print("\nSaved Successfully!")
    print(data[today])



print(set_challenge())