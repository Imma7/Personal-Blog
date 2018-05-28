from flask import render_template
from . import auth

@auth.route('/login')
def login():
    '''
    Function that checks if the form is validated
    '''
    return render_template('auth/login.html',login_form=login_form)


#logout function
@auth.route('/logout') #authenticated route logout that calls the flask_login's logout_userfunction
@login_required 
def logout(): 
    logout_user()
    return redirect(url_for('main.index'))# redirects user to the main page of the app after successful logout
