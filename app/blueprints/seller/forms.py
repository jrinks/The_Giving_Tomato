from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.core import DateField, TimeField
from wtforms.validators import DataRequired, Email, EqualTo, URL, Length, AnyOf


class SellerInfoForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password_hash = PasswordField('Password', validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    company_name = StringField('Company Name', validators=None)
    phone = StringField('10 digit phone number', validators=[Length(min=10, max=10, message='Please enter a valid 10 digit phone number'), AnyOf(values=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], message="Please enter a valid 10 digit phone number")])
    submit = SubmitField()

class PickupInfoForm(FlaskForm):
    pickup_date = DateField('pickup date', format='%m/%d/%Y', validators=None)
    pickup_time = TimeField('pickup time', validators=None)
    pickup_address = StringField('pickup address', validators=None)
    pickup_city = StringField('pickup city', validators=None)
    pickup_state = StringField('pickup state', validators=None)
    pickup_instructions = StringField('pickup instructions', validators=None)
    submit = SubmitField()


class CharityInfoForm(FlaskForm):
    org_name = StringField('org name', validators=[DataRequired()])
    org_mission = StringField('mission', validators=[DataRequired()]) 
    org_description = StringField('mission', validators=None) 
    org_city = StringField('city', validators=None)
    org_state = StringField('state abbreviation', validators=[Length(min=2, max=2, message='Please enter a two-letter state abbreviation')])
    org_url = StringField('website url', validators=[DataRequired(), URL(message='Please enter a valid url')])
    submit = SubmitField()

