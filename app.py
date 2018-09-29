from flask import Flask
from flask_cors import CORS

import config
from dal import Dal
from routes.login import Login
from routes.carts import Carts

app = Flask(__name__)
cors = CORS(app)

db = Dal(config.DB['HOST'], config.DB['PORT'])

login_route = Login()
carts_route = Carts(db)

app.add_url_rule('/login', view_func=login_route.login, methods=['POST'])
app.add_url_rule('/carts/<user>', view_func=carts_route.get_all_carts)

if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT)
