from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DecimalField, IntegerField
from wtforms.fields.core import DateField, TimeField
from wtforms.validators import DataRequired, Email, EqualTo, URL, Length, AnyOf


class ComposeSMS(FlaskForm):
    text = StringField('Text', validators=None)
    submit = SubmitField()

    