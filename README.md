# The Yu-Gi-Oh-Project

## Contents:
* [The Project Brief](#The-Project-Brief)  
* [The App Design](#The-App-Design)
* [The CI/CD Pipeline](#The-CI/CD-Pipeline)  
* [The Risk Assessment](#The-Risk-Assessment)
* [The Unit-Testing](#The-UnitTesting)
* [The App](#The-App)
* [Updates](#Updates)
* [Known Issues](#Known-Issues)
* [Future Work](#Future-Work)

## The Project Brief  
The aim for the project was to design a flask application intergrated with a database via Python (Flask micro-frameworks). The core design for the app needed to have a CRUD functionality (create, read, update, and delete). The CI/CD pipeline creates the automation via Jenkins deployment, then the app is deployed using Docker products (Dockerfile, Docker-Compose, & Docker-Swarm), interfaced using Microsoft Azure VMs. The data is stored via a MySQL database consisting of two tables and sharing a one-to-many relationship.

![Picture2](https://user-images.githubusercontent.com/108364254/197344567-b0a8d54c-a732-48ad-b06a-b83d60f54d55.png)

The diagram illusrates the basic premise of the web app functionality. The HTML will acts as the front-end interfaced with the Flask micro-framework via Python to execute the logic and the information is stored via MySQL database, both the micro-framework and database acts as the back-end server. 

The diagram below illustrates how the flask app will be deployed using Microsoft Azure resources (VMs) and how the build server will be deployed. 

![yugioh-project (1)](https://user-images.githubusercontent.com/108364254/198905097-71f21986-4bfd-4187-aff5-fa546fa147f5.png)

The app will be hosted and deployed using containers, and a CI/CD pipeline must be used to automatically test, build, and delpoy the application.

## The App Design
In terms of the design I have chosen to build a Yu-Gi-Oh! database app, which allows users to create their favourite duel monster card and linking the monster type (create function). The new data will be displayyed via the home page (read function), users can also update the current data, i.e. the ID of the duel monster card is linked to the card name and type (update function), additionally the user can also delete the current data relative to the card ID (delete function). The database for this project consists of a duel monster name table and an duel monster type table, hence with each duel monster type is associated with multiple duel monster names (one-to-many relationship). The Entity Relationship Diagram is illustrated below:

![Picture6](https://user-images.githubusercontent.com/108364254/197350597-fbe5e13e-a0be-4dcc-97a8-081a5e7dc5ac.png)

The ERD diagram illustrates the functionality of the MySQL database. The foreign key is assiocated with the duel monster name and level, where card ID will be linked via both the name and type relationship.

## The CI/CD Pipeline 
The project required the implementation of several stages of a automated CI/CD pipeline. These included: version control, development enviroment, and a build server.

![pipeline](https://user-images.githubusercontent.com/108364254/198901429-96d612a8-0530-4760-882a-5d93bbf5da2d.png)

Github was used for the version control; the project respository is hosted via Github.com. In terms of version control the updates to the project to be commited and pushed, whilst keeping the commit history to authorise access to previous versions. The Github repository allows to host the service and to be stored in terms for the development enviroment. In addition by implementing webhooks, which sends HTTP POST requests to the build server to automate both the build and the unit-testing.
  
The development environment used was Python3 virtual environment (venv) hosted on a virtual machine running on Ubuntu 20.04. Python is used as the core mainframe and the Flask is a python-based micro-framework. The venv allows the pip to install the basic requirements.txt (see file) and the performance of the app to run without causing any conflicts when pip installs the modules on the same local machine or VMs.

Jenkins will be used as the build server to provide the automation for both the build and the unit-testing. It is to note, the automation is achieved by setting up a freestyle project, which will execute the test.sh file once it recieves the Webhook via Github (files to be commited and pushed). Jenkins will also be used to run the app, this is only possible if the testing achieves high coverage.

![222222222222222222222222222](https://user-images.githubusercontent.com/108364254/198751956-e3b7d3cd-7c87-4f4e-bc91-acecdeb75762.jpg)

The Docker containers was used to containerise and deploy the flask app by creating 3 images: the flask application, the MySQL database, and the Nginx as a reverse proxy. By deploying the containers via the host application on the local public IP address (Azure virtual machines), which connects it to the database and allows access to the reverse proxy itself. The docker images were created using a automated server (Jenkins), which was then uploaded to the Dockerhub and again using Jenkins the images will be pulled through the stack deployment via the Dockerswarm servers (manager and worker nodes). It is worth noting the docker-compose file was used to execute and to run the containers via a single command line. The flask app can now be accessed via the public IP addresses of the two virtual machines.

## The Risk Assessment
Before buidling the web app, a risk assessment was conducted to identify and to propose measure of control and potential risks that could affect the deployment process for the app. The initial risk assesment is illustrated below:

![table1](https://user-images.githubusercontent.com/108364254/198903128-2b4fc2c8-d7ed-446c-b01b-5a35ec5e5d75.jpg)

![table2](https://user-images.githubusercontent.com/108364254/198903153-473e69d2-dcc0-48de-8736-47aec98336f1.jpg)

The control measure implemented in the project will demostrate the risk assesment in terms of:
* The user profiles per database was not part of the initial design, as this would reqire sending an authentication process via unsecured HTTP connection.
* The SQLAlchemy is interfaced with the Flask micro-framework to prevent MySQL commands being sent directly to the database.
* The credentuals will be stored as a secret text via Jenkins VMs and exported as environment variable to avoid releasing confidential information (On the Github repo).

The likelihood and impact level of each risk identified were estimated before and after the implementation in terms of each control measures, to quantify the effect of potential control measures and implementation.

## The Unit-Tests

Testing the flask app was an essential part for the project and by extension the development process. It was required to test the app itself through unit testing, which were written in terms for the create, read, update and delete functionality to verify the app performance and to achieve high coverage. For the project the unit-testing will be conducted on several files to achieve the 200 return response.   

It is to note, tests such as security and performance were not part of the project scope, only the testing in terms of the app functionality was conducted. The tests will be automated through Jenkins and interfaced via Github Webhooks, which will demostrate the automation when a change is made to the code. A successful build, in which all test passed is illustrated below: 

![22](https://user-images.githubusercontent.com/108364254/198747528-cd3082a7-f23f-4b2d-ae86-768d479fde2e.PNG)

The coverage report shows unit-test at 100% archived during post-build:

![22222222222222](https://user-images.githubusercontent.com/108364254/198748277-423eb67e-83e5-4421-a87f-ffa7bcc36881.PNG)

All tests must pass for a build to be successful a single point failure means the overall test build failed and therefore the tests have been intergrated into CI/CD pipeline via Jenkins.

## The App

When navigating to the app the user is presented with the hompage as illustrated below:

![flask1](https://user-images.githubusercontent.com/108364254/198894895-e387c752-f74d-45c3-8472-01851161caec.PNG)

The user can navigate to a different page to add, update, and delete the data via the URL. To add the monster name and type the user will need to enter [http://192.168.33.22:5000/monstername] and [http://192.168.33.22:5000/monstertype] respectively as illustrated below:

![flask2](https://user-images.githubusercontent.com/108364254/198895182-2266639b-78d0-48de-b8f8-27120200cc27.PNG)

The user is redirected to the page, which allows them add the monstername for the database. The new data (monster name and type) is displayed via the home page as illustratrated below:

![flask3](https://user-images.githubusercontent.com/108364254/198895468-bfb77199-bc54-48ba-89ac-64c5ef86e108.PNG)

As stated earlier, the user can update and delete both the monster name and type by entering: [http://192.168.33.22:5000/updatename/1], [http://192.168.33.22:5000/updatetype/1], [http://192.168.33.22:5000/deletename/1], and [http://192.168.33.22:5000/deletename/1]. It is worth noting the value 1 corresponds to the card ID when the user first creates the new data. 

## Future Work


..

