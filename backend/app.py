from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "PrepMentor AI Backend Running 🚀"


@app.route("/generate-plan", methods=["POST"])
def generate_plan():
    try:
        data = request.json

        name = data.get("name")
        goal = data.get("goal")
        hours = int(data.get("hours"))
        weak_subjects = data.get("weakSubjects")
        mood = data.get("mood")

        # Mood-based study adjustment
        burnout_message = ""

        if mood == "Tired":
            hours = max(2, hours - 2)
            burnout_message = "😞 Light study day to avoid burnout."

        elif mood == "Stressed":
            hours = max(2, hours - 3)
            burnout_message = "😫 Recovery mode activated."

        elif mood == "Focused":
            hours += 2
            burnout_message = "🔥 High intensity study mode."

        elif mood == "Motivated":
            hours += 1
            burnout_message = "😊 Productivity boost mode."

        else:
            burnout_message = "😐 Balanced study mode."

        # GATE PLAN
        if goal == "GATE":
            study_plan = f"""
🚀 GATE Study Plan for {name}

Mood Today: {mood}
Daily Hours: {hours}
Weak Subject: {weak_subjects}

{burnout_message}

Day 1:
- {weak_subjects}
- Data Structures
- Aptitude

Day 2:
- DBMS
- Operating Systems
- PYQs

Day 3:
- Computer Networks
- Mock Test

Day 4:
- TOC + Compiler Design

Day 5:
- Revision

Day 6:
- Mock Test + Analysis

Day 7:
- Full Revision
"""

        # PLACEMENT PLAN
        elif goal == "Placements":
            study_plan = f"""
💼 Placement Plan for {name}

Mood Today: {mood}
Daily Hours: {hours}
Weak Subject: {weak_subjects}

{burnout_message}

Day 1:
- Aptitude
- {weak_subjects}

Day 2:
- DSA Practice

Day 3:
- SQL + DBMS

Day 4:
- React / Web Dev

Day 5:
- Mock Interview

Day 6:
- Resume Improvement

Day 7:
- Company Preparation
"""

        # BOTH PLAN
        else:
            study_plan = f"""
🔥 Combined GATE + Placement Plan for {name}

Mood Today: {mood}
Daily Hours: {hours}
Weak Subject: {weak_subjects}

{burnout_message}

Day 1:
- GATE Subject
- Aptitude

Day 2:
- DSA + Coding

Day 3:
- DBMS + Resume

Day 4:
- Mock Test

Day 5:
- OS + Interview Prep

Day 6:
- Weak Subject Revision

Day 7:
- Final Revision
"""

        return jsonify({
            "studyPlan": study_plan
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)