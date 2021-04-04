from flask import Flask, request, redirect, render_template 
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet 
from forms import PetForm, EditForm

app = Flask(__name__)


app.config['SECRET_KEY'] = 'This is such a secret'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

connect_db(app)

debug = DebugToolbarExtension(app)


@app.route("/")
def index():
    return render_template('index.html', pets=Pet.get_all())


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """ GET and POST for adding a pet"""
    form = PetForm() 
    
    if(form.validate_on_submit()):
        Pet.add_from_form(form)
        return redirect('/')

    return render_template('pet_form.html', form=form)

@app.route('/<int:id>', methods=['GET', 'POST'])
def details(id):
    """GET and POST for displaying pet details and editing pet """
    
    pet = Pet.get(id)
    form = EditForm(obj=pet)
    if(form.validate_on_submit()):
        EditForm.fill_pet(form, pet)
        db.session.commit() 
        return redirect('/')

    return render_template('details.html', pet=pet, form=form)