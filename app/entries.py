from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SelectField, IntegerField
from wtforms.validators import DataRequired

class dataentry(Form):
    name = StringField('name', validators=[DataRequired()])
    branch = SelectField('branch', choices=[('Compscience','Computer Science'),('EnT', 'Electronics and Telecommunication'),('Electrical','Electrical'),('Mechanical','Mechanical'),('Chemical','Chemical'),('Industrial & Production','Industrial and Production'),('Instrumentation','Instrumentation')])
    passyear = StringField('passyear', validators=[DataRequired()])
    hostel  = SelectField('hostel', choices=[('Hostel-1','Hostel-1'),('Hostel-2','Hostel-2'),('Hostel-3','Hostel-3'),('Hostel-4','Hostel-4'),('Hostel-5','Hostel-5'),('Hostel-6','Hostel-6'),('Hostel-7','Hostel-7'),('Hostel-8','Hostel-8')])
    phone= StringField('phone', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])


