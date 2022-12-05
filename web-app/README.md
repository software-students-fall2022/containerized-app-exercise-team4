## Web App Setup

### Activate Virtual Environment

1. Change directory to web-app
    ```
    cd web-app
    ```

    You should be inside web-app folder to run following:

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



### Run Web-App Tests
If you want to run web app tests, do the following:
1. change directory to web-app
    ```
    cd web-app 
    ``` 
    You should be inside web-app folder to run the following:

2. Run 
    ```
    python -m pytest
    ```