import json
import os


def test_courses_file_exists():
    assert os.path.exists("courses.json")


def test_students_file_exists():
    assert os.path.exists("students.json")


def test_courses_data_not_empty():
    with open("courses.json", "r") as file:
        data = json.load(file)

    assert len(data) > 0


def test_student_data_not_empty():
    with open("students.json", "r") as file:
        data = json.load(file)

    assert len(data) > 0


def test_recommendation_keyword():
    course = "Artificial Intelligence"
    assert "Artificial" in course