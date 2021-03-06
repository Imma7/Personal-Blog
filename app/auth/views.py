from flask import render_template,redirect,request,url_for,flash
from flask_login import login_user,login_required,logout_user
from . import auth
from .. import db
from ..models import Writer
from .forms import RegistrationForm,LoginForm



@auth.route('/login',methods=['GET','POST'])
def login():
    '''
    Function that checks if the form is validated
    '''
    # if current_writer.is_authenticated:
    #     return redirect(url_for('main.index'))

    login_form = LoginForm()
    if login_form.validate_on_submit():
        # writer = Writer(email=login_form.email.data)
        writer = Writer.query.filter_by(email=login_form.email.data).first()
        if writer is not None and writer.verify_password(login_form.password.data):
            login_user(writer,login_form.remember.data)
            return redirect(request.args.get('next')or url_for('main.index'))

        flash('invalid username or password')

    return render_template('auth/login.html',login_form=login_form)


@auth.route('/reqister',methods=['GET','POST'])
def register():
    '''
    Registration function
    '''
    # if current_writer.is_authenticated:
    #     return redirect(url_for('main.index'))
    form =RegistrationForm()
    if form.validate_on_submit():
        writer =Writer(email=form.email.data,name=form.username.data,password=form.password.data)
        db.session.add(writer)
        db.session.commit()

        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',registration_form=form)

#logout function
@auth.route('/logout') #authenticated route logout that calls the flask_login's logout_userfunction
@login_required 
def logout(): 
    logout_user()
    return redirect(url_for('main.index'))# redirects user to the main page of the app after successful logout
