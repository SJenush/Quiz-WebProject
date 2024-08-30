# Quiz Web Application

## Overview

This is a web application built using Django that allows users to create quizzes, attend quizzes, and view submissions. It is designed to be user-friendly and supports various functionalities to make quiz management and participation seamless.

## Features

- **Quiz Creation**: Users can create quizzes with multiple questions. Each question can have multiple options, with one or more correct answers.
- **Quiz Participation**: Users can attend quizzes by selecting the appropriate answers. The quiz is timed, and submissions are automatically evaluated upon completion.
- **View Submissions**: After attending a quiz, users can view their submissions, including the score and the correct answers.

## Installation

### Prerequisites

- Python 3.x
- Django 4.x
- SQLite (default database)
- A web browser (for accessing the application)

### Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/SJenush/Quiz-WebProject.git
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

6. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

1. **Create a Quiz**:
   - Navigate to the "Create Quiz" section.
   - Fill in the quiz details, add questions, and set the correct answers.
   - Save the quiz for users to attempt.

2. **Attend a Quiz**:
   - Browse available quizzes and select one to attend.
   - Answer the questions within the allotted time.
   - Submit the quiz to see your score and correct answers.

3. **View Submissions**:
   - After submitting a quiz, view your previous submissions to review your performance.
   - Check your score, the correct answers, and any mistakes you made.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

- Django - The web framework used to build this application.
- Bootstrap - For the responsive front-end design.
