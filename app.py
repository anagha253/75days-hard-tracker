import streamlit as st
from datetime import datetime, timedelta, date
import json

# ---------------- CONFIG ---------------- #

FILE_NAME = "challenge_progress.json"

tasks = [
    "Follow a diet (No cheat meals / alcohol)",
    "Two 45-minute workouts",
    "Drink 3L water",
    "Read 10 pages",
    "Take progress picture"
]

# ---------------- FUNCTIONS ---------------- #

def set_challenge():
    start_day = datetime.now().date()
    end_day = start_day + timedelta(days=75)
    return start_day, end_day

def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return {}

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# ---------------- UI ---------------- #

st.set_page_config(
    page_title="75 Hard Tracker",
    page_icon="🔥",
    layout="centered"
)

st.title("🔥 75 Hard Challenge Tracker")

start_day, end_day = set_challenge()

st.write(f"### Start Date: {start_day}")
st.write(f"### End Date: {end_day}")

today = str(date.today())

data = load_data()

if today not in data:
    data[today] = {}

st.divider()

st.subheader(f"Today's Checklist — {today}")

for task in tasks:
    checked = st.checkbox(
        task,
        value=data[today].get(task, False)
    )

    data[today][task] = checked

# ---------------- SAVE BUTTON ---------------- #

if st.button("Save Today's Progress"):
    save_data(data)

    completed = sum(data[today].values())

    st.success("Progress Saved Successfully!")

    st.metric(
        label="Tasks Completed Today",
        value=f"{completed}/5"
    )

# ---------------- HISTORY ---------------- #

st.divider()

st.subheader("📅 Previous Progress")

for day, progress in reversed(data.items()):
    st.write(f"### {day}")

    for task, done in progress.items():
        status = "✅" if done else "❌"
        st.write(f"{status} {task}")