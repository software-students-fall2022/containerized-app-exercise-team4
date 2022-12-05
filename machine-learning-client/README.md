## Machine Learning Client Setup

### Set Up Virtual Environment

1. Change directory to machine-learning-client
    ```
    cd machine-learning-client
    ```
    You should be inside machine-learning-client folder to run following:

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
    You should be inside machine-learning-client folder to run following:

2. Activate virtual environment
    ```
    source .venv/Scripts/activate
    ```
3. Run the project
    ```
    flask run
    ```

### Run Machine Learning Client Tests
If you want to run machine learning client tests, do the following:
1. change directory to machine-learning-client
    ```
    cd machine-learning-client 
    ```
    You should be inside machine-learning-client folder to run the following: 
2. Run 
    ```
    python -m pytest
    ```
