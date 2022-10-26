from flask import render_template, url_for, redirect, request 
from application import app, db
from application.models import MonsterName, MonsterType
from application.forms import Monsterform, TypeForm

#READ BOTH DATABASES
#Location for the app function: ip_address:5000
@app.route("/", methods=["POST", "GET"])
def index():
    mtypes = MonsterType.query.all()
    mnames = MonsterName.query.all()
    return render_template("index.html", title="Yu-Gi-Oh! Duel Monsters Trading Card Game", mtypes=mtypes, mnames=mnames)

#CREATE the duel monster type.
#Location for the app function: ip_address:5000/monstertype
@app.route("/monstertype", methods=["POST", "GET"])
def addtype():
    form = TypeForm()
    if form.validate_on_submit():
        mtypes = MonsterType(
            type = form.type.data,
            fk_nameid = form.fk_nameid.data
            
        )
        db.session.add(mtypes)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("addtype.html", title="Enter a new Duel Monster type", form=form)

#CREATE the duel monster card name.
#Location for the app function: ip_address:5000/monstername
@app.route("/monstername", methods=["POST", "GET"])
def addname():
    #Navigates to MonsterForm
    form = Monsterform()
    #Validates if the user entered the submit button
    if form.validate_on_submit():
        #The variable "names" will be displayed on the form
        #The MonsterName will be added to the database
        monsters = MonsterName(
            name = form.name.data,
            stars = form.stars.data
            #Foreign key used as a option to add to the create process
            
        )
        #The code add to the database.
        db.session.add(monsters)
        #The code will commit the changes.
        db.session.commit()
        #The code will redirect to the index url function.
        return redirect(url_for("index"))
    #Otherwise the template returns the add.html.
    return render_template("addname.html", title="Enter a new Duel Monster card name", form=form)

#UPDATE the duel monster type
#Location for the app function: ip_address:5000/updatemonstertype
@app.route("/updatetype/<int:mtid>", methods=["GET", "POST"])
def updatetype(mtid):
    form = TypeForm()
    mtypes = MonsterType.query.get(mtid)
    if form.validate_on_submit():
        mtypes.type = form.type.data
        db.session.commit()
        return redirect(url_for("index"))
    elif request.method == "GET":
        form.type.data = mtypes.type
    return render_template("updatetype.html", title="Update the Duel Monster type", form=form)

#UPDATE the duel monster name.
#Location for the app function: ip_address:5000/updatemonstername
@app.route("/updatename/<int:id>", methods=["GET", "POST"])
def updatename(id):
    form = Monsterform()
    #Retrieves one duel monster name via specified ID.
    name = MonsterName.query.get(id)
    #POST method & if the user clicks the submit button.
    if form.validate_on_submit():
        #The data is edited relative to the new information via the user.
        name.name = form.name.data
        
        #Commit the updated changes
        db.session.commit()
        #Redirects the URL via the index function
        return redirect(url_for("index"))
    #If the request method is a GET
    elif request.method == "GET":
        #Update the form in the database
        form.name.data = name.name
        
    #If the user navigates the URL, returns the template to updatename.html
    return render_template("updatename.html", title="Update the Duel Monster card name", form=form)
        
#DELETE duel monster type
#Location for the app function: ip_address:5000/deletetype
@app.route("/deletetype/<int:mtid>")
def deletetype(mtid):
    mtype = MonsterType.query.get(mtid)
    db.session.delete(mtype)
    db.session.commit()
    return redirect(url_for("index"))

#DELETE duel monster name
#Location for the app function: ip_address:5000/deletename
@app.route("/deletename/<int:id>")
def deletename(id):
    #Relative to the data the user will delete via the ID
    name = MonsterName.query.get(id)
    #Deleting the item from the database
    db.session.delete(name)
    #Commit the new changes
    db.session.commit()
    #Returnthe URL via the index function. 
    return redirect(url_for('index')) 






