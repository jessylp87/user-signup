from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def display_signup_form():
    return render_template('signup.html', title = 'Sign up!')

@app.route('/', methods=['POST'])
def signup():

    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    verify_password = request.form['verify_password']

    username_error = ''
    if len(username) == 0:
        username_error = "Please enter a valid username."
    elif username.strip() == 0:
        username_error = "Please enter a valid username."
    elif ' ' in username:
        username_error = "Please create a username with no spaces."
    elif len(username) < 3 or len(username) > 20:
        username_error = "Please create a username of length between 3 and 20 characters."
    else: username_error = ''

    password_error = ''
    if len(password) < 3 or len(password) > 20:
        password_error = "Please enter a password of length between 3 and 20 characters."
    elif password != verify_password:
        password_error = "Passwords do not match."
    else:
        password_error = ''

    email_error = ''
    if email:
        if '@' not in email or '.' not in email:
            email_error = 'Please enter a valid email address.'
        elif ' ' in email:
            email_error = 'Please enter a valid email address.'
        elif len(email) < 3 or len(email) > 20:
            email_error = 'Please enter an email address of length between 3 and 20 characters.'
    else:
        email_error = ''

    if not username_error and not password_error and not email_error:
        return render_template('welcome.html', title='Welcome, ' + username + '!', username=username)

    return render_template('signup.html', title = "Sign Up!", username_error = username_error, password_error = password_error, email_error = email_error, username = username, email = email)

app.run()
