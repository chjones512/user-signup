from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True



@app.route("/welcome", methods=['POST'])
def welcome():
    username_error = ''
    password_error = ''
    verifypass_error = ''
    email_error = ''
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    if username is None:
        username_error += 'This is a required field.'
    if password is None:
        password_error += 'This is a required field.'
    if verify is None:
        verifypass_error += 'This is a required field.'
    
    
    if len(username) < 3 or len(username) > 20 or username.count(' ') >= 1:
        username_error += 'This entry is not valid.'
    
    
    if len(password) < 3 or len(password) > 20:
        password_error += 'This entry is not valid.'
    

    if verify != password:
        verifypass_error += 'This does not match.'
    

    if email is not "" and len(email) < 3 or len(email) > 20:
        email_error += 'This entry is not valid.'
    
    
    if email is not "" and " " in email:
        email_error += 'This entry is not valid.'
    
    if email is not "" and email.count("@") != 1:
        email_error += 'This entry is not valid.'

    if email is not "" and email.count(".") != 1:
        email_error += 'This entry is not valid.'
    
    if len(email_error) > 1 or len(verifypass_error) > 1 or len(password_error) > 1 or len(username_error) > 1:
        return render_template("user_signup.html", username = username, email = email, email_error=email_error, password_error=password_error, verifypass_error=verifypass_error, username_error=username_error)
    else:
        return render_template('welcome.html', username=username)

@app.route("/")
def index():
    return render_template('user_signup.html', title="Sign Up Page")

app.run()