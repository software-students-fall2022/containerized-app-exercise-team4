[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9334554&assignment_repo_type=AssignmentRepo)
<br />
![ML Tests](https://github.com/software-students-fall2022/containerized-app-exercise-team4/actions/workflows/ml-tests.yaml/badge.svg)
![Web App Tests](https://github.com/software-students-fall2022/containerized-app-exercise-team4/actions/workflows/web-app-tests.yaml/badge.svg)
# Containerized App Exercise

## Project Description

**Machine Learning Client** - A game where a user is prompted to draw an object on a canvas. When the user submits their drawing, the model predicts what they drew and the user gets points based on the model's confidence output.

**Web App** - A dashboard that displays analytics, including leaderboard for highest scores, most active users, and the average score for each object.

**Database** - Stores each user's username and password, as well as their scores on each of the possible objects that the user is prompted to draw.

## Docker Setup
### WEBAPP + MONGODB Database Setup within Docker (using docker-compose)

1. Docker Desktop: 
Make sure Docker Desktop is installed, if not,

    check [here](https://docs.docker.com/desktop/install/windows-install/) for windows

    check
    [here](https://docs.docker.com/desktop/install/mac-install/) for mac

2. Once the docker desktop is installed, make sure you go to the top right corner and click on bug sign to navigate to **RESET TO FACTORY DEFAULTS**. This will reset the docker and prompt the docker to restart. Please make sure you do this step before running the files from github repository because the docker does not create right images sometimes.

3. Go to the root folder (containerized-app-exercise-team4) and run the following command
    ```
    docker-compose up
    ```

4. This will install all the required dependencies and the web app starts running at port **127.0.0.1:3000**. Make sure you go to **127.0.0.1:3000** port instead of 5000 because the docker outputs the web-app at **127.0.0.1:3000** port. 

## Machine Learning Client Setup

**Note:** One of the modules we used for the machine learning client is not supported by Apple Silicon, so you won't be able to run it on Macs with M1 and M2 chips unless you install a virtual machine on your device.

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
    ```

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

The player draws an image on canvas and gets results as **PERFECT, EXCELLENT, VERY GOOD, GOOD, AVERAGE and FAILED** which are mapped to **50, 40, 30, 20, 10, 0** respectively.  

## Web App Setup (If you want to run webapp without using docker-compose)

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

    #### For Windows: 
    ```
    .venv\Scripts\activate.bat
    ```

    #### For mac: 
    ```
    source .venv/bin/activate
    ```

4. Install the packages: 
    ```
    pip install -r requirements.txt
    ```

5. Define two environment variables from the command line:
    #### On Windows, use 
    ```
    set FLASK_APP=app.py and set FLASK_ENV=development
    ```
        
    #### On Mac, use  
    ```
    export FLASK_APP=app.py and export FLASK_ENV=development
    ```
   
6. Start flask with 
    ```
    flask run
    ```

    This will output an address at which the app is running locally, e.g. https://127.0.0.1:5000. Visit that address in a web browser.


## Run Tests

#### Run Machine Learning Client Tests
If you want to run machine learning client tests, do the following:
1. change directory to machine-learning-client
    ```
    cd machine-learning-client 
    ``` 
2. Run 
    ```
    python -m pytest
    ```

#### Run Web-App Tests
If you want to run web app tests, do the following:
1. change directory to web-app
    ```
    cd web-app 
    ``` 
2. Run 
    ```
    python -m pytest
    ```


## Team Members

[Kevin Gong](https://github.com/kxg202)

[Dixit Timilsina](https://github.com/dt1930)

[Maaz Ahmed](https://github.com/maazahmedd)

[Sanjaya Bhatta](https://github.com/itSanjaya)

[Fatema Nassar](https://github.com/maazahmedd)

[Elyazya Al Kobaisi](https://github.com/elyazya)
