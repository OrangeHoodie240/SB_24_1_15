from flask_sqlalchemy import SQLAlchemy 


db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """ model for pets table """

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, nullable=False, default = True)

    @classmethod
    def get_all(cls):
        return cls.query.all() 

    @classmethod
    def add(cls, name, species, photo_url=None, notes=None, age=None):
        pet = Pet(name=name, species=species, photo_url=photo_url, notes=notes, age=age)
        db.session.add(pet)
        db.session.commit() 

    @classmethod 
    def add_from_form(cls, form):
        """ will take a PetForm and create a Pet object from it """ 
        name, species, photo_url, notes, age = Pet.from_form(form)
        cls.add(name=name, species=species, photo_url=photo_url, notes=notes, age=age)
    
  

    @classmethod
    def from_form(cls, form):
        """ Takes data out of an EditForm and returns bindings with the appropriate names """

        name = form.name.data 
        species = form.species.data 
        photo_url = form.photo_url.data 
        notes = form.notes.data 
        age = form.age.data 
        return name, species, photo_url, notes, age

    @classmethod
    def get(cls, id):
        return Pet.query.get(id)