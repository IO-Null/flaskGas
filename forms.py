from flask_wtf import FlaskForm, RecaptchaField
from wtforms import IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired

class GasCalculator(FlaskForm):
    price = FloatField(
        'Price Per Gallon',
        [DataRequired()]
    )
    mpg = IntegerField(
        'MPG',
        [DataRequired()]
    )
    distance_roundtrip = IntegerField(
        'Distance Round Trip',
        [DataRequired()]
    )
    hourly_wage = FloatField(
        'Hourly Wage',
        [DataRequired()]
    )
    hours_worked = IntegerField(
        'Average hours worked daily',
        [DataRequired()]
    )
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')