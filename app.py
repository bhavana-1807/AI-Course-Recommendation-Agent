import json
import os
from groq import Groq
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

# Connect Groq LLM
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Load course catalogue from JSON file
with open("courses.json", "r") as file:
    courses = json.load(file)


print("===== AI Course Recommendation Agent =====")

# Take student details as input
name = input("Enter Student Name: ")
background = input("Enter Background: ")
skills = input("Enter Current Skills: ")
goal = input("Enter Career Goal: ")


# Prepare course catalogue information
course_data = ""

for course in courses:
    course_data += f"""
Course Name: {course['course_name']}
Career Goal: {course['career_goal']}
Required Skills: {course['required_skills']}
Reason: {course['reason']}

"""


# Agent instructions (System Prompt)
system_prompt = """
You are an AI Course Recommendation Agent.

Your job is to suggest the best learning path for students based on their background, current skills, and career goals.

Rules:
1. Recommend only suitable 3-4 courses from the given course catalogue.
2. Display output only in this format:

Course 1:
Reason:

Course 2:
Reason:

Course 3:
Reason:

3. Each reason must be only one sentence.
4. Do not add phases, percentages, extra advice, or additional recommendations.
5. Keep the answer short and simple.
"""


# User prompt with student details and courses
user_prompt = f"""

Student Details:

Name: {name}
Background: {background}
Current Skills: {skills}
Career Goal: {goal}


Available Course Catalogue:

{course_data}


Generate a personalized learning path recommendation.
"""


# Send request to Llama model through Groq API
response = client.chat.completions.create(

    model="llama-3.1-8b-instant",

    messages=[

        {
            "role": "system",
            "content": system_prompt
        },

        {
            "role": "user",
            "content": user_prompt
        }

    ]

)


# Display AI generated recommendation
print("\n===== Recommended Learning Path =====\n")

print(response.choices[0].message.content)
