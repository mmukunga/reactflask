# reactflask
# install gunicorn in your virtual environment

# pip install gunicorn
# then update your requirements.txt file

# pip freeze > requirements.txt

# After checking that gunicorn is in requirements.txt run:

# pip install -r requirements.txt

# Tutorial: https://code.visualstudio.com/docs/python/tutorial-flask
# Create a project environment for the Flask tutorial
# Windows
# python -m venv env
# In VS Code, open the Command Palette (View > Command Palette or (Ctrl+Shift+P)). 
#   Then select the Python: 
#   Select Interpreter command:
#   correct version of python.exe
# Update pip in the virtual environment by running the following command in the VS Code Terminal:
#   python -m pip install --upgrade pip
# Install Flask in the virtual environment by running the following command in the VS Code Terminal:
#   python -m pip install flask
# Create and run a minimal Flask app
#   (env) D:\py\\hello_flask>

# app.py
# from flask import Flask
# app = Flask(__name__)
# @app.route("/")
# def home():
#    return "Hello, Flask!"
# (env) D:\py\\hello_flask>python -m flask run

# Tutorial: https://gist.github.com/Reine0017
#
cd D:\Temps\ReactFlask\frontend
del /q /s "D:\Temps\ReactFlask\frontend\build"
npm run build
cd D:\Temps\ReactFlask

git status
git add .
git commit -m "first commit"
# git commit --allow-empty -m "Purge cache"
git branch -M main
git push -u origin main

heroku logs --tail --app reactflask-smb

heroku builds:cache:purge -a reactflask-smb  --confirm reactflask-smb
