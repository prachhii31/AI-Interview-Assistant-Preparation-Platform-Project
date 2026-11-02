# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/questions')
# def questions():
#     return render_template('questions.html')

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():

    email = request.form['email']
    password = request.form['password']

    if email == "admin@gmail.com" and password == "1234":
        return redirect('/dashboard')

    return "Invalid Login"

@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

@app.route('/questions')
def questions():
    return render_template('questions.html')

if __name__ == '__main__':
    app.run(debug=True)