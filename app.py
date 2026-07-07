import json
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

with open("courses.json", "r") as file:
    courses = json.load(file)

print("===== AI Course Recommendation Agent =====")

name = input("Enter Student Name: ")
background = input("Enter Background: ")
skills = input("Enter Current Skills: ")
goal = input("Enter Career Goal: ")


course_data = ""

for course in courses:
    course_data += f"""
Course Name: {course['course_name']}
Career Goal: {course['career_goal']}
Required Skills: {course['required_skills']}
Reason: {course['reason']}
"""


system_prompt = """
You are an AI Course Recommendation Agent.

Analyze the student's background, skills, and career goal.

Recommend an ordered learning path from the course catalogue.

Explain why every course is selected.
"""


user_prompt = f"""

Student:
Name: {name}
Background: {background}
Skills: {skills}
Career Goal: {goal}

Available Courses:
{course_data}

Give personalized course recommendations.
"""


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


print("\nRecommended Learning Path:\n")
print(response.choices[0].message.content)
