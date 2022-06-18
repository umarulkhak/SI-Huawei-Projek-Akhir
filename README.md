# SI-Huawei-Projek-Akhir (Sentiment Analysis EDOM) 

A `LSTM` Recurrent Neural Network based Flask Web App that classifies the sentiment of EDOM.
# Getting Started

To get the app working locally:
1. Clone or download the repository locally.
2. Within the SI-Huawei-Projek-Akhir directory, create a virtual Python environment with the Terminal command `python -m venv flaskapp` where `flaskapp` is the name of your environment. You can choose any name.
3. Activate the virtual environment with the command        `
    ```bash                 
    flaskapp\scripts\activate.bat
    ```
4. Then run the command `pip install -r requirements.txt` (In case of error in Windows at this point, you need to set the LongPathsEnabled Registry value to 1. [See here](https://stackoverflow.com/questions/54778630/could-not-install-packages-due-to-an-environmenterror-errno-2-no-such-file-or/55189256#55189256))
5. Next, set the FLASK_APP variable to app.py and FLASK_ENV to development by running the following command (for windows) 
   ```bash
    set FLASK_APP=app.py
    ```
6. Also, set the FLASK_ENV to `development` by running the following command (for windows)
    ```bash
    set FLASK_ENV=development
    ```
7. And finally, run the command `python -m flask run` to start the app
8. The terminal will output the local web address and port where the app is running. As an example, this might be `http://127.0.0.1:5000/`. Now, open a web browser and go to that web address.

# Prerequisites

You will need [Python3 installed](https://www.python.org/downloads/) on your local machine.
