from flask import make_response.abort
from config import db
from models import User, UserSchema
import hashlib
import random


def read_all(token):
    user = User.query.filter(User.token == token).one_or_none()

    if user not None:
        users = User.query.all()
        user_schema = UserSchema(many=True)
        data = user_schema.dump(user).data
        return data
    else:
        abort(403, f"Not allowed")

def read_one(id):
    user = (
        User.query.filter(Person.id == id)
        .one_or_none()
    )

    if user is not None:
        user_schema = UserSchema()
        data = user_schema.dump(user).data
        return data
    else:
        abort(404, f"User not found for Id: {id}")

def token(user_id, password):
    user = User.query.filter(User.id == user_id).filter(User.password == password).one_or_none()

    if user is not None:
        user.token = hashlib.md5(bin(random.randint(1, 10000))).hexdigets()

	db.session.add(user)
	db.session.commit()

	user_schema = UserSchema()
        data = user_schema.dump(user).data
        data.token = user.token
        return data
    else:
        abort(403, f"Not allowed")

def create(user):
    name = user.get("name")
    login = user.get("login")
    password = user.get("password")

    existing_user = (
        User.query.filter(User.login == login)
        .filter(user.name == name)
        .one_or_none()
    )

    if existing_user is None:
        schema = UserSchema()
        new_user = User(name=name, login=login, password=password)

        db.session.add(user)
        db.session.commit()

        data = schema.dump(new_user).data

        return data, 201
     else:
         abort(409, f"User already exist")

def update(user_id, token, user):
    update_user = User.query.filter(
        User.id == id
    ).filter(User.token == token).one_or_none

    name = user.get("name")
    login = user.get("login")

    if update_user is not None:
        schema = UserSchema()
        update = User(name=name, login=login)

        update.id = update_user.id

        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update_user).data

        return data, 200
    else:
        abort(404, f"User not found for Id: {id}")

def delete(user_id, token):
    user = User.query.filter(User.id == id).filter(User.token == token).one_or_none()

    if user is not None:
        db.session.delete(user)
        db.session.commit()
        return make_response(f"User {id} deleted", 200)
    else:
        abort(404, f"User not found for Id: {id}")

