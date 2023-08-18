from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, URLField,DecimalField
# from wtforms.fields 
# from wtforms.widgets
from wtforms.validators import InputRequired, NumberRange, Optional, URL,DataRequired


class AddCupcake(FlaskForm):
    flavor = StringField("Flavor", validators=[InputRequired()])
    rating = DecimalField("Rating", places=2,validators=[DataRequired(),NumberRange(min=0.0, max=10.0)])
    size = StringField("Size", validators=[InputRequired()])
    image = URLField("Image URL", validators=[URL(),Optional()])
