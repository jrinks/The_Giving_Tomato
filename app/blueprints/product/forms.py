from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DecimalField, IntegerField
from wtforms.fields.core import DateField, TimeField
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired, URL, Length, AnyOf


class ProductInfoForm(FlaskForm):
    plant_name = StringField('Plant Name', validators=[InputRequired('Plant Name is required')])
    plant_description = StringField('Plant Descripiton', validators=[InputRequired('Plant Description is required')])
    is_heirloom = BooleanField('Check here if plant type is Heirloom', validators=None)
    price = DecimalField('Item Price', validators=[InputRequired('Price is required')])
    img_url = StringField('image url', validators=[URL(message='Please enter a valid URL')]) 
    category_id = IntegerField(validators=None)
    submit = SubmitField()

class DeleteProductForm(FlaskForm):
    submit = SubmitField()