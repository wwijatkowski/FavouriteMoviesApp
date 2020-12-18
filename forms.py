from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length


class SearchField(FlaskForm):
    title = StringField('Podaj nazwę filmu, który chcesz wyszukać:', validators=[DataRequired()])
    year = IntegerField('Podaj rok produkcji')
    submit = SubmitField('Wyszukaj')
