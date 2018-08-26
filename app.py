from flask import Flask, request, make_response
from flask_cors import CORS
from bson.json_util import dumps
import json
import config
from dal import Dal

app = Flask(__name__)
cors = CORS(app)

db = Dal(config.DB['HOST'], config.DB['PORT'])


@app.route('/login', methods=['POST'])
def login():
    credentials = json.loads(request.data)
    return_object = {'email': credentials['email'], 'name': 'Tomer', 'token': 'kaki'}

    return make_response(json.dumps(return_object), 200)


@app.route('/carts/<user>')
def getAllCarts(user):
    carts = db.getAllCarts(user)
    return make_response(dumps(carts), 200)


if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT)
