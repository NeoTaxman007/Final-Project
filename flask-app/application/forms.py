#Linking the database via routes and creating the input forms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from application.models import MonsterName, MonsterType

#Creating a class object for the duel monster card name, i.e. Dark Magician, Blue-Eyes White Dragon, etc.
class Monsterform(FlaskForm):
    name = StringField("Duel Monster Name")
    stars = StringField("Duel Monster Star Level")
    submit = SubmitField("Submit")

#Creating a class object for the duel monster type, i.e. Spellcaster, Dragon, etc.  
class TypeForm(FlaskForm):
    type = StringField("Duel Monster Type")
    fk_nameid = IntegerField("Duel Monster ID")
    submit = SubmitField("Submit")
    
