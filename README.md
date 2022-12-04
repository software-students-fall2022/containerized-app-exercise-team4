[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9334554&assignment_repo_type=AssignmentRepo)
![ML Tests](https://github.com/software-students-fall2022/containerized-app-exercise-team4/actions/workflows/ml-tests.yaml/badge.svg)
![Web App Tests](https://github.com/software-students-fall2022/containerized-app-exercise-team4/actions/workflows/web-app-tests.yaml/badge.svg)
# Containerized App Exercise

## Project Description

Machine Learning Client - A game where a user is prompted to draw an object on a canvas. When the user submits their drawing, the model predicts what they drew and the user gets points based on the model's confidence output.

Web App - A dashboard that displays analytics, including leaderboard for highest scores, most active users, and the average score for each object.

Database - Stores each user's username and password, as well as their scores on each of the possible objects that the user is prompted to draw.

## Machine Learning Client Setup

### Set Up Virtual Environment

1. Change directory to machine-learning-client
    ```
    cd machine-learning-client
    ```
2. Create python virtual environment
    ```
    python -m venv .venv
    ```
3. Activate virtual environment on bash
    ```
    source .venv/Scripts/activate
    ```
4. Download dependencies
    ```
    pip install -r requirements.txt

### Run Machine Learning Client

1. Change directory to machine-learning-client
    ```
    cd machine-learning-client
    ```
2. Activate virtual environment
    ```
    source .venv/Scripts/activate
    ```
3. Run the project
    ```
    flask run
    ```

## Web App Setup

### Activate Virtual Environment

1. Change directory to web-app
    ```
    cd web-app
    ```
2. Create virtual environment
    ```
    python -m venv .venv
    ```
3. Activate virtual environment
    **If you ran the Machine Learning client in a virtual environment called .venv, pick a different name for the virtual environment when running the web app. If picking a different name, make sure to replace .venv in all the following commands with the new name of your virtual environment.**
    windows: `.venv\Scripts\activate.bat`
    mac: `source .venv/bin/activate`
4. Install packages: `pip install -r requirements.txt`.
5. define two environment variables from the command line:
   on Mac, use the commands: `export FLASK_APP=app.py` and `export FLASK_ENV=development`.
   on Windows, use `set FLASK_APP=app.py` and `set FLASK_ENV=development`.
6. start flask with `flask run` - this will output an address at which the app is running locally, e.g. https://127.0.0.1:5000. Visit that address in a web browser.

## Docker Setup

To be written


## Run Tests

To run machine-learning-client tests, change directory to machine-learning-client `cd machine-learning-client` and run `python -m pytest`.
To run web-app tests, change directory to web-app `cd web-app` and run `python -m pytest`.

## Team Members

[Kevin Gong](https://github.com/kxg202)

[Dixit Timilsina](https://github.com/dt1930)

[Maaz Ahmed](https://github.com/maazahmedd)

[Sanjaya Bhatta](https://github.com/itSanjaya)

[Fatema Nassar](https://github.com/maazahmedd)

[Elyazya Al Kobaisi](https://github.com/elyazya)

Build a containerized app that uses machine learning. See [instructions](./instructions.md) for details.
