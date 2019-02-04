#get form to display
#get POST endpoint working
#deal with validation
    #redirect, accept
#helper functions
#build base.html /welcomepage
#build form.html / homepage
#web app to display form.html

from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/signup')
def display_user_signup_form():
    return render_template('base.html')

# functions for validations
def empty_val(x):
    if x:
        return True
    else:
        return False

def char_length(x):
    if len(x) > 2 and len(x) < 21:
        return True
    else:
        return False

def email_at_symbol(x):
    if x.count('@') >= 1:
        return True
    else:
        return False

def email_at_symbol_more_than_one(x):
    if x.count('@') <= 1:
        return True
    else:
        return False

def email_period(x):
    if x.count('.') >= 1:
        return True
    else:
        return False

def email_period_more_than_one(x):
    if x.count('.') <= 1:
        return True
    else:
        return False

# route to process and validate form
@app.route("/signup", methods=['POST'])
def user_signup_complete():

    # creates variables from form inputs
    username = request.form['username']
    password = request.form['password']
    password_validate = request.form['password_validate']
    email = request.form['email']

    # creates empty strings for error message
    username_error = ""
    password_error = ""
    password_validate_error = ""
    email_error = ""

    # error messages that occur more than once
    err_required = "Required field"
    err_reenter_pw = "Please re-enter password"
    err_char_count = "must be between 3 and 20 characters"
    err_no_spaces = "must not contain spaces"

    # password validation
    if not empty_val(password):
        password_error = err_required
        password = ''
        password_validate = ''
    elif not char_length(password):
        password_error = "Password " + err_char_count
        password = ''
        password_validate = ''
        password_validate_error = err_reenter_pw
    else:
        if " " in password:
            password_error = "Password " + err_no_spaces
            password = ''
            password_validate = ''
            password_validate_error = err_reenter_pw

    # second password validation
    if password_validate != password:
        password_validate_error = "Passwords must match"
        password = ''
        password_validate = ''
        password_error = 'Passwords must match'
            
    # username validation
    if not empty_val(username):
        username_error = err_required
        password = ''
        password_validate = ''
        password_error = err_reenter_pw
        password_validate_error = err_reenter_pw
    elif not char_length(username):
        username_error = "Username " + err_char_count
        password = ''
        password_validate = ''
        password_error = err_reenter_pw
        password_validate_error = err_reenter_pw
    else:
        if " " in username:
            username_error = "Username " + err_no_spaces
            password = ''
            password_validate = ''
            password_error = err_reenter_pw
            password_validate_error = err_reenter_pw

    # email validation

    # checks to see if email contains text prior to running validations
    #if provide email (not necessary)
        #must have @, a single ., no spaces, between 3-20 char
    if empty_val(email):
        if not char_length(email):
            email_error = "Email " + err_char_count
            password = ''
            password_validate = ''
            password_error = err_reenter_pw
            password_validate_error = err_reenter_pw
        elif not email_at_symbol(email):
            email_error = "Email must contain the @ symbol"
            password = ''
            password_validate = ''
            password_error = err_reenter_pw
            password_validate_error = err_reenter_pw
        elif not email_at_symbol_more_than_one(email):
            email_error = "Email must contain only one @ symbol"
            password = ''
            password_validate = ''
            password_error = err_reenter_pw
            password_validate_error = err_reenter_pw
        elif not email_period(email):
            email_error = "Email must contain ."
            password = ''
            password_validate = ''
            password_error = err_reenter_pw
            password_validate_error = err_reenter_pw
        elif not email_period_more_than_one(email):
            email_error = "Email must contain only one ."
            password = ''
            password_validate = ''
            password_error = err_reenter_pw
            password_validate_error = err_reenter_pw
        else:
            if " " in email:
                email_error = "Email " + err_no_spaces
                password = ''
                password_validate = ''
                password_error = err_reenter_pw
                password_validate_error = err_reenter_pw

    #if input valid
    #show welcome page with username

    if not username_error and not password_error and not password_validate_error and not email_error:
        username = username
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('main.html', username_error=username_error, username=username, password_error=password_error, password=password, password_validate_error=password_validate_error, password_validate=password_validate, email_error=email_error, email=email)

@app.route('/welcome')
def valid_signup():
    username = request.args.get('username')
    return render_template('welcomepage.html', username=username)

app.run()
