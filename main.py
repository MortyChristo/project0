from flask import Flask
from controller.customer_controller import cc

if __name__ == '__main__':
    bank = Flask(__name__)

    bank.register_blueprint(cc)

    bank.run(port=8081, debug=True)
