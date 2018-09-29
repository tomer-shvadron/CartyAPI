from json import dumps, loads
from flask import request, make_response


class Login:
    def login(self):
        credentials = loads(request.data)
        return_object = {'email': credentials['email'], 'name': 'Tomer', 'token': 'kaki'}

        return make_response(dumps(return_object), 200)
