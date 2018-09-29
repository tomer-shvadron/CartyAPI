from bson.json_util import dumps
from flask import make_response


class Carts:
    def __init__(self, db):
        self.db = db

    def get_all_carts(self, user):
        carts = self.db.get_all_carts(user)
        return make_response(dumps(carts), 200)
