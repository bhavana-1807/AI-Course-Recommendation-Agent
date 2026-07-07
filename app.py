import json

# Load course catalogue
with open("courses.json", "r") as file:
    courses = json.load(file)

print("===== AI Course Recommendation Agent =====")

name = input("Enter Student Name: ")
background = input("Enter Background: ")
skills = input("Enter Current Skills (comma separated): ").lower()
goal = input("Enter Career Goal: ")

print("\nPersonalized Learning Path for", name)
print("--------------------------------")

rank = 1

for course in courses:
    if course["career_goal"].lower() == goal.lower():

        missing = []

        for skill in course["required_skills"]:
            if skill.lower() not in skills:
                missing.append(skill)

        if missing:
            print(rank, ".", course["course_name"])
            print("Reason:", course["reason"])
            print()
            rank += 1

if rank == 1:
    print("You already have the recommended skills.")
