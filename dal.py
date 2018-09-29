from pymongo import MongoClient


class Dal:
    def __init__(self, host, port):
        self.db = MongoClient(host, port)

    def get_all_carts(self, user):
        return list(self.db.carty.carts.find({'user': user}))
