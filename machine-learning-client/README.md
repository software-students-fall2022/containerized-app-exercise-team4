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

The player draws an image on canvas and gets results as **PERFECT, EXCELLENT, VERY GOOD, GOOD, AVERAGE and FAILED** which are mapped to **50, 40, 30, 20, 10, 0** respectively.  
