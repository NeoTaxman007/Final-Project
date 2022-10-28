# Yu-Gi-Oh-Project

## Contents:
* [Project Brief](#Project-Brief)  
* [App Design](#App-Design)
* [CI Pipeline](#CI-Pipeline)  
* [Risk Assessment](#Risk-Assessment)
* [Testing](#Testing)
* [The App](#The-App)
* [Updates](#Updates)
* [Known Issues](#Known-Issues)
* [Future Work](#Future-Work)

## The Project Brief  
The aim for the project was to design a web application intergrated with a database via Python using Flask micro-framework. The design for the app needed to have a CRUD functionality (create, read, update, and delete). The CI/CD pipeline creates the automation via Jenkins deployment, then the app is deployed using Docker products (Dockerfile, Docker-Compose, & Docker-Swarm) interfaced using Microsoft Azure VMs. The information is stored via a MySQL database consisting of two tables and sharing a one-to-many relationship.

![Picture2](https://user-images.githubusercontent.com/108364254/197344567-b0a8d54c-a732-48ad-b06a-b83d60f54d55.png)

The diagram illusrates the basic premise of the web app functionality. The HTML will acts as the front-end interfaced with the Flask micro-framework via Python to execute the logic and the information is stored via MySQL database, both the micro-framework and database acts as the back-end server. 

## The App Design
In terms of the design I have chosen to build a Yu-Gi-Oh! database app, which allows users to enter their favourite duel monster card and the monster type (create function), view the new data via the index.html page (read function), users can also update the current data, i.e. the ID of the duel monster card is linked to the card name and type (update function), additionally the user can also delete the current data relative to the card ID (delete function). The database for this project consists of a duel monster name table and an duel monster type table, hence with each duel monster type is associated with multiple duel monster names (one-to-many relationship). The Entity Relationship Diagram is illustrated below:

![Picture6](https://user-images.githubusercontent.com/108364254/197350597-fbe5e13e-a0be-4dcc-97a8-081a5e7dc5ac.png)

The ERD diagram illustrates the functionality of the MySQL database. The foreign key is assiocated with the duel monster name and level, where card ID will be linked via both the name and type relationship.

## The CI/CD Pipeline 
The project required the implementation of several stages of a automated CI/CD pipeline. These included: version control, development enviroment and a build server.

![cicd-pipeline-1536x532](https://user-images.githubusercontent.com/108364254/198750152-57c62135-4616-45f3-8acb-f510a35239c3.png)

Github was used for version control the project respository hosted via Github.com. In terms of version control via Github this allows updates to the project to be commited and pushed, whilst keeping the commit history for access to previous versions. The Github as a repository allows the repository to host the service and to be stored via the development enviroment, in addition providing webhooks, which sends HTTP POST requests to the build server to automate both the build and the unit-testing.
  
The development environment used was Python3 virtual environment (venv) hosted on a virtual machine running Ubuntu 20.04. Python is used as the core for the code and the Flask is a python-based micro-framework. The venv allows the pip to install the basic requirements.txt and the performance of the app to run without causing any conflicts when pip install the modules on the same machine or VMs.

Jenkins will be used as the build server to provide the automation for both the build and the unit-testing. It is to note the automation is achieved by setting up a freestyle project, which will execute the test.sh script when it recieves the webhook via Github (files needs to commited then pushed). Jenkins will also be used to run the app via Gunicorn, achieved when testing is completed.

////INSERT IMAGE HERE////
  
 ## The Risk Assessment
 
Before buidling the web app, a risk assessment was conducted to identify and to propose measure to control the potential risks that could affect the process for deploying the app. The measure will then be implemented in the app, the initial risk assesment is illustrated below:

![Picture8](https://user-images.githubusercontent.com/108364254/197365789-188f763d-005d-4369-9af0-e750a6bf75d3.png)
The control measure implemented in the project will demostrate the risk assesment in terms of:
* The user profiles per database was not part of the initial design, as this would reqire sending an authentication process via unsecured HTTP connection.
* The SQLAlchemy was inerfaced with the Flask micro-framework to prevent MySQL commands being sent directly via the database.
* The credentuals will be stored as a secret text via Jenkins VMs and exported as environment variable to avoid releasing confidential information.

The likelihood and impact level of each risk identified were estimated before and after the implementation of each control measures, to quantify the effect of potential control measures and implementation.

## The Unit-Tests

Testing the flask app was an essential part for the project and by extension the development process. It was required to test the app itself via unit testing, which were written for the create, read, update and delete functionality to verify the app performance and to achieve high coverage. For the project the unit-testing will be conducted on several files to achieve the 200 return response.   

It is to note, tests such as security and performance were part of the project scope, only the testing in terms of functionality was conducted. The tests will be automated via Jenkins and interfaced with Github webhooks to demostrate the automation when a change is made to the code. A successful build, in which all test passed, is illustrated below: 

![22](https://user-images.githubusercontent.com/108364254/198747528-cd3082a7-f23f-4b2d-ae86-768d479fde2e.PNG)

The coverage report shows unit-test at 100% archived during post-build:

![22222222222222](https://user-images.githubusercontent.com/108364254/198748277-423eb67e-83e5-4421-a87f-ffa7bcc36881.PNG)

All tests must pass for a build to be successful a single point failure means the overall test build failed.


