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

Your task is to recommend suitable courses for students from different career domains based on their background, skills, and career goal.

Rules:
- Analyze the student's career goal carefully.
- Recommend exactly 3 most relevant courses from the provided course catalogue.
- Do not recommend courses unrelated to the student's goal.
- Use only the available course catalogue.
- Give one short reason for each recommendation.
- Do not write introductions, phases, conclusions, or extra advice.

Output format:

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


Give only the final answer in the required format. Maximum 3 courses only.
"""


# Send request to Llama model through Groq API
response = client.chat.completions.create(

    model="llama-3.1-8b-instant",
    temperature=0.2,
    max_tokens=250,

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
