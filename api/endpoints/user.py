from flask_restplus import Resource, Namespace
from flask import request, jsonify
from models.user import User
from models import db
from datetime import datetime

USER_API = Namespace('hello', description='User Api')


@USER_API.route('/<username>', strict_slashes=False)
@USER_API.header('Content-Type', 'application/json')
class Users(Resource):

    def get(self, username):
        user = User.query.filter(User.username == username).first()
        birthday = user.dob
        now = datetime.now()
        days = self.calculate_dates(birthday, now)
        if days >= 365 :
            return {"Message": "Hello {}! Happy Birthday! ".format(username)}
        return {"Message": "Hello {}! your birthday is in {} days".format(username, days)}

    def put(self, username):
        raw_input = request.get_json()
        try:
            User.query.filter(User.username == username).update(raw_input)
            db.session.commit()
        except Exception as e:
            raise e

        return {"Message": 'Record Updated Successfully'}


    @staticmethod
    def calculate_dates(original_date, now):
        delta1 = datetime(now.year, original_date.month, original_date.day)
        delta2 = datetime(now.year + 1, original_date.month, original_date.day)
        days = (max(delta1, delta2) - now).days
        return days

@USER_API.route('', strict_slashes=False)
@USER_API.header('Content-Type', 'application/json')
class Users(Resource):
    def post(self):
        raw_input = request.get_json()
        try:
            user = User(**raw_input)
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            raise e

        return {"Message": 'User Record created Successfully'}
