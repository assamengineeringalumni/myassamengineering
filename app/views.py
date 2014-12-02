from app import app
from flask import render_template, flash, redirect, g, session, url_for
from .forms import LoginForm
from .entries import dataentry
from .searching import search_form
from datetime import datetime
from app import db , models
from sqlalchemy.sql import text
import string
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='AEC Alumni Database',
                           )

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.openid.data == 'aecalumni' and form.password.data == 'aecalumni1':
            return redirect('/databaseentry')
        else:
            flash('User id and Password entered is wrong')
    return render_template('login.html',
                           title='Get started',
                           form=form)


@app.route('/databaseentry' , methods = ['GET','POST'])
def databaseentry():
    form = dataentry()
    record = models.User(username=form.name.data,branch=form.branch.data,passyear=form.passyear.data,hostel=form.hostel.data,phone=form.phone.data,emailid=form.email.data)
    if form.validate_on_submit():
        db.session.add(record)
        db.session.commit()
        flash('Your data has been successfully entered')
    return render_template('dataentry.html',
                           title='Dataentry Page',
                           form=form)


@app.route('/search', methods = ['GET','POST'])
def search():
    form = search_form()
    username1 = form.name.data
    branch1 = form.branch.data
    passyear1 = form.passyear.data
    Sql=text('select * from User where username = \'%s\' and  branch = \'%s\'  and passyear = \'%s\' '%(username1,branch1,passyear1))
    results=db.engine.execute(Sql)
    return render_template('search_form.html',
                           title='Search Page',
                           results=results,
                           form=form)
@app.route('/logout')
def logout():
    return redirect('/index')
           


    

    
    

