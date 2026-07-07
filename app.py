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

Your task is to select courses for a student.

Rules:
- Recommend exactly 3 courses only.
- Use only the provided course catalogue.
- Output only course names and reasons.
- Each reason must be one short sentence.
- Do not explain the student's background.
- Do not mention existing skills.
- Do not add introductions.
- Do not add conclusions.
- Do not add extra recommendations.

Required Output Format:

1. Course:
Reason:

2. Course:
Reason:

3. Course:
Reason:
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
