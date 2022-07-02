from flask import Flask
from controller.customer_controller import cc
from controller.account_controller import ac

if __name__ == '__main__':
    bank = Flask(__name__)

    bank.register_blueprint(cc)
    bank.register_blueprint(ac)

    bank.run(port=8081, debug=True)
