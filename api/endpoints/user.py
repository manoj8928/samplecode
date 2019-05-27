from flask_restplus import Resource, Namespace
from flask import request, jsonify
from models.user import User
from models import db
import datetime

USER_API = Namespace('hello', description='User Api')


@USER_API.route('/<username>', strict_slashes=False)
@USER_API.header('Content-Type', 'application/json')
class Users(Resource):

    def get(self, username):
        user = User.query.filter(User.username == username).first()
        td = datetime.date.today()

        bd = user.dob  # birth date in a datetime format
        nbd = datetime.date(td.year, bd.month, bd.day)  # next birthday
        if (nbd - td).days < 0:  # if the ate already passed for this year
            nbd = datetime.date(td.year + 1, bd.month, bd.day)

        if (nbd - td).days > 0:
            return {"Message": "Hello {}! your birthday is in {} days".format(username, (nbd - td).days)}
        else:
            return {"Message": "Hello {}! Happy Birthday! ".format(username)}



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
        print("Max === {}".format(max(delta1, delta2)))
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
