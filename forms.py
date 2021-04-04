from flask_wtf import FlaskForm 
from wtforms import IntegerField, StringField, BooleanField, SelectField, RadioField
from wtforms.validators import InputRequired, AnyOf, URL, Optional, NumberRange

valid_pets = ['cat', 'dog', 'porcupine']
class PetForm(FlaskForm):
    """ Form for adding new pet """

    name = StringField("Name: ", validators=[InputRequired(message="Pet Name Required")])
    species = SelectField("Species: ", choices=valid_pets, validators=[InputRequired(message="Pet Species Required"), AnyOf(valid_pets)])
    photo_url = StringField("Photo Url: ", validators=[Optional(), URL(message='Not valid url')])
    notes = StringField("Notes :")
    age = IntegerField("Age: ", validators=[NumberRange(min=0, max=30), Optional()])


class EditForm(FlaskForm):
    """ Form for editing pet """

    photo_url = StringField("Photo Url: ", validators=[Optional(), URL()])
    notes = StringField("Notes :")
    available = RadioField("Available: ", choices=[(True, 'yes'), (False, 'no')])

    @classmethod
    def fill_pet(cls, form, pet):
        """ method for placing form data into pet object """

        print(form.available.data)
        pet.notes = form.notes.data
        pet.available = True if form.available.data.startswith('T') else False
        pet.photo_url = form.photo_url.data