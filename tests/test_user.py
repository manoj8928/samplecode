from .base import BaseTestCase
from models.user import User
from models import db
from flask import json
from datetime import date


class TestUser(BaseTestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPostUserData(self):
        payload = {"username": "manoj666", "dob":"1991-05-03"}
        response = self.client.post('api/v1/hello',
                                    data = json.dumps(payload),
                                    content_type='application/json'
                                    )
        data = response.json
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["Message"], "User Record created Successfully")
        delete_user(payload["username"])

    def testPutUserData(self):
        payload = {"username": "manoj666", "dob": "1991-05-03"}
        create_user(payload)
        response = self.client.put('api/v1/hello/{}'.format(payload["username"]),
                                    data=json.dumps({"username": "manoj666", "dob": "1992-05-03"}),
                                    content_type='application/json'
                                    )
        data = response.json
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["Message"], "Record Updated Successfully")
        delete_user(payload["username"])

    def testBirthdayGreetings(self):
        today = date.today()
        day = today.strftime("%Y-%m-%d")
        payload = {"username": "jdhsdjhskj", "dob": day}
        create_user(payload)
        response = self.client.get('api/v1/hello/{}'.format(payload["username"]))
        data = response.json
        self.assertEqual(response.status_code, 200)
        txt = "Hello {}! Happy Birthday! ".format(payload["username"])
        self.assertEqual(data["Message"], txt)
        delete_user(payload["username"])


def create_user(data):
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return user


def delete_user(username):
    user_to_delete = User.query.filter(User.username == username).first()
    db.session.delete(user_to_delete)
    db.session.commit()