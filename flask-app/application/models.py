#Designing the database
from application import db

#Creating a dataset class for the duel monster type.
class MonsterType(db.Model):
    mtid = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(30))
    fk_nameid = db.Column(db.Integer, db.ForeignKey('monster_name.id'))
    
#Creating a dataset class for the duel monster name. 
class MonsterName(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    stars = db.Column(db.Integer)
    #fk_typeid = db.Column(db.Integer, db.ForeignKey('monster_type.mtid'))
    