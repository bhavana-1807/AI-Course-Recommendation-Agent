# AI-Course-Recommendation-Agent

An AI agent that recommends personalized learning paths based on student skills, goals, and background.


## Project Overview

AI Course Recommendation Agent is an intelligent AI-powered system that suggests personalized learning paths for students based on their background, existing skills, and career goals.

The agent analyzes user input, checks the available course catalogue, and uses a Large Language Model (LLM) to generate suitable course recommendations with clear reasoning.

This project was developed for the Junior AI Research Associate - AI Agent Challenge.


---

## Agent Objective

My agent takes:

- Student background
- Current skills
- Career goal

and produces:

- Personalized course recommendations
- Ordered learning path
- Short explanation for every recommended course


---

## Features

- Accepts student profile as input
- Supports multiple career domains
- Uses LLM-based reasoning
- Reads course data from JSON catalogue
- Generates personalized recommendations
- Provides reasons for each selected course
- Command-line based execution


---

## Supported Domains

The course catalogue includes multiple fields such as:

- Artificial Intelligence
- Data Science
- Software Development
- Cyber Security
- Web Development
- Banking and Finance
- Business Management
- Teaching
- Law
- Healthcare
- Writing and Literature
- Design
- Hospitality


---

## Technology Stack

| Component               | Technology |
|-------------------------|------------|
| Programming Language    |     Python |
| AI Model                | Llama 3.1 8B Instant |
| LLM Provider            | Groq API |
| Data Storage            | JSON |
| Interface               | Command Line Interface (CLI) |


---

## How the Agent Works

Workflow:

User Input

↓

Load Course Catalogue (courses.json)

↓

Create Prompt with Student Details + Course Data

↓

Send Request to Llama LLM using Groq API

↓

Generate Course Recommendations

↓

Display Personalized Learning Path


---

## AI Model Integration

This project uses Groq API to access the Llama 3.1 8B Instant language model.

The LLM helps the agent understand:

- Student goals
- Existing skills
- Suitable learning paths


Model used:
`lama-3.1-8b-instant`



---

## System Prompt Design

The system prompt defines the role and rules of the agent.

The model is instructed to:

- Act as an AI Course Recommendation Agent
- Analyze student details
- Recommend relevant courses
- Avoid unrelated recommendations
- Provide short explanations


---

## Project Structure
AI-Course-Recommendation-Agent/

│
├── app.py
├── courses.json
├── students.json
├── requirements.txt
├── sample_outputs.txt
├── README.md
└── .gitignore


---

## Installation Steps

### 1. Clone Repository

```bash
git clone https://github.com/bhavana-1807/AI-Course-Recommendation-Agent.git
```
Move into project folder:
```bash
cd AI-Course-Recommendation-Agent
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. API Key Setup

Create a .env file inside the project folder.

Add your Groq API key:
GROQ_API_KEY=api_key

### 4. Run the Agent

Execute:
```bash
python app.py
```

### 5. Enter student details:

Example:

  Enter Student Name: Bhavana
  Enter Background: MCA
  Enter Current Skills: Python, SQL
  Enter Career Goal: Data Scientist

Output:

  1. Course: Data Analysis with Python
  Reason: Helps analyze datasets using Python libraries.

  2. Course: Machine Learning
  Reason: Helps build intelligent systems using data.

  3. Course: SQL Database Management
  Reason: Helps manage structured data.

### Sample Outputs

Multiple test cases are available in:

```bash
sample_outputs.txt
```

The agent was tested with different domains including:
 - Data Scientist
- Bank Manager
- Teacher
-  Cyber Crime Officer
   Writer


## Design Choices
- Python was selected because it provides simple AI integration.
- Groq API was used for fast LLM responses.
- Llama model was selected for natural language understanding.
- JSON was used as lightweight storage for the course catalogue.
- CLI interface was used to keep the agent simple and easy to run.

### Limitations and Future Improvements

Current Limitations:

 -- Course recommendations depend on available catalogue data.
-- More career fields require adding more courses.

Future Improvements:

-- Add a web interface.
-- Store user history in a database.
-- Expand the course catalogue.
-- Add user feedback-based recommendations.


### Conclusion

This AI Course Recommendation Agent demonstrates an end-to-end AI workflow:

Input → Context Retrieval → LLM Reasoning → Recommendation Output

The system provides personalized learning guidance using Python, JSON storage, Groq API, and Llama LLM.


