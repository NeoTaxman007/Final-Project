from application import db

#To create the database file
db.drop_all()
db.create_all()
