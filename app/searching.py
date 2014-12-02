from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SelectField, IntegerField
from wtforms.validators import DataRequired

class search_form(Form):
    name = StringField('name', validators=[DataRequired()])
    branch = SelectField('branch', choices=[('Compscience','Computer Science'),('EnT', 'Electronics and Telecommunication'),('Electrical','Electrical'),('Mechanical','Mechanical'),('Chemical','Chemical'),('Industrial & Production','Industrial and Production'),('Instrumentation','Instrumentation')])
    passyear = StringField('passyear', validators=[DataRequired()])
