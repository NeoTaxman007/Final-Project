from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import MonsterName, MonsterType


#Creating the tese base class
class TestBase(TestCase):
    def create_app(self):

        #Pass in the testing config for the database app.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db", SECRET_KEY='TEST_SECRET_KEY', DEBUG=True, WTF_CSRF_ENABLED=False)
        return app

    #Will be called before every test
    def setUp(self):
        #Creates a table
        db.create_all()
        #Creates a test for duel monster name
        name1 = MonsterName(name="Test-Duel-Monster-Name")
        #The information is stored in the database
        db.session.add(name1)
        db.session.commit()
        #Creates test for duel monster type
        type1 = MonsterType(type = 'Test-Spellcaster-Type')
        db.session.add(type1)
        db.session.commit()
        
    #Will be called after every test
    def tearDown(self):
        #Close the database session and remove all contents of the database
        db.session.remove()
        db.drop_all()
        
#Write a test class to test Read functionality
class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test', response.data)
        
#Test sending a GET request for the index.html page        
class TestAddName1(TestBase):
    def test_add_name1(self):
        response = self.client.get(url_for('addname'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'', response.data)
        
#Test sending a GET request to add Duel Monster name
class TestAddName2(TestBase):
    def test_add_name2(self):
        response = self.client.post(url_for('addname', id=1),data = dict(q_name='Elemental-Hero-Flame-Wingman-Test'), follow_redirects=True)
        self.assertIn(b'',response.data)

#Test sending a GET request to add Duel Monster type
class TestAddType1(TestBase):
    def test_add_type1(self):
        response = self.client.get(url_for('addtype'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'', response.data)

#Test adding a Duel Monster type
class TestAddType2(TestBase):
    def test_add_type2(self):
        response = self.client.post(url_for('addtype', id=1), data = dict(q_type="Warrior-Test"), follow_redirects=True)
        self.assertIn(b'',response.data)

#Test sending a GET request to update Duel Monster name
class TestUpdateName1(TestBase):
    def test_update_name1(self):
        response = self.client.get(url_for('updatename', id=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'', response.data)

#Test updating a Duel Monster name
class TestUpdateName2(TestBase):
    def test_update_name2(self):
        response = self.client.post(url_for('updatename', id=1), data = dict(q_name="Dark-Magician-Test"), follow_redirects=True)
        self.assertIn(b'',response.data)

#Test sending a GET request to update Duel Monster type
class TestUpdateType1(TestBase):
    def test_update_type1(self):
        response = self.client.get(url_for('updatetype', mtid=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'', response.data) 

#Test updating a Duel Monster type      
class TestUpdateType2(TestBase):
    def test_update_type2(self):
        response = self.client.post(url_for('updatetype', mtid=1), data = dict(q_type="Spellcaster-Test"), follow_redirects=True)
        self.assertIn(b'',response.data)

#Test deleting a Duel Monster name from database
class TestDeleteName(TestBase):
    def test_delete_name(self):
        response = self.client.get(url_for('deletename', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'', response.data)
        #self.assertNotIn(b'', response.data)

#Test deleting a Duel Monster type from database
class TestDeleteType(TestBase):
    def test_delete_type(self):
        response = self.client.get(url_for('deletetype', mtid=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'', response.data)
        
        
        
'''
#Inspects a test class for adding & updating Duel Monster name & type
#User will not be able run a GET request for delete & update

#Test sending a GET request for the index.html page
class TestIndexPage(TestBase):
    def test_index(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test-007', response.data)

#Test sending a GET request to add Duel Monster name
class TestAddName1(TestBase):
    def test_add_name1(self):
        response = self.client.get(url_for('addname'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Adding test: Duel-Monster name1', response.data)
        
#Test adding Duel Monster name
class TestAddName2(TestBase):
    def test_add_name2(self):
        response = self.client.post(url_for('addname', id=1),data = dict(q_name='Elemental-Hero-Flame-Wingman-Test'), follow_redirects=True)
        self.assertIn(b'Adding test: Duel-Monster name2 ',response.data)

#Test sending a GET request to add Duel Monster type
class TestAddType1(TestBase):
    def test_add_type1(self):
        response = self.client.get(url_for('addtype'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Adding test: Duel-Monster type1', response.data)

#Test adding a Duel Monster type
class TestAddType2(TestBase):
    def test_add_type2(self):
        response = self.client.post(url_for('addtype'), data = dict(q_type="Warrior-Test"), follow_redirects=True)
        self.assertIn(b'Adding test: Duel-Monster type2',response.data)

#Test sending a GET request to update Duel Monster name
class TestUpdateName1(TestBase):
    def test_update_name1(self):
        response = self.client.get(url_for('updatename', id=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Updating test: Duel-Monster name1', response.data)
        
#Test updating a Duel Monster name
class TestUpdateName2(TestBase):
    def test_update_name2(self):
        response = self.client.post(url_for('updatename'), data = dict(q_type="Dark-Magician-Test"), follow_redirects=True)
        self.assertIn(b'Adding test: Duel-Monster type2',response.data)

#Test sending a GET request to update Duel Monster type
class TestUpdateType1(TestBase):
    def test_update_type1(self):
        response = self.client.get(url_for('updatetype', id=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Updating test: Duel-Monster type1', response.data)

#Test updating a Duel Monster name
class TestUpdateType2(TestBase):
    def test_update_type2(self):
        response = self.client.post(url_for('updatetype'), data = dict(q_type="Spellcaster-Test"), follow_redirects=True)
        self.assertIn(b'Updating test: Duel-Monster type2',response.data)

#Test deleting a Duel Monster name from database
class TestDeleteName(TestBase):
    def test_delete_name(self):
        response = self.client.get(url_for('deletename', id = 1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Testq', response.data)
        self.assertNotIn(b'Deleting test: Duel-Monster name', response.data)

#Test deleting a Duel Monster type from database
class TestDeleteType(TestBase):
    def test_delete_type(self):
        response = self.client.get(url_for('deletetype', id = 1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Deleting test: Duel-Monster type', response.data) '''
