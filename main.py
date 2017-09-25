from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['username']
    return render_template('welcome.html', username=username)

@app.route("/")
def index():
    return render_template('user_signup.html', title="Sign Up Page")

app.run()