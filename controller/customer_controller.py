from flask import Blueprint, request
from model.customer import Customer
from service.customer_service import CustomerService
from exception.invalid_parameter import InvalidParameterError
from exception.customer_not_found import UserNotFoundError

cc = Blueprint('customer_controller', __name__)
customer_service = CustomerService()

@cc.route('/')
def init_table():
    return {
        "message": "Welcome"
    }, 200

@cc.route('/customer')
def get_all_customers():
    return {
        "customer": customer_service.get_all_customers()
    }


@cc.route('/customer/<customer_id>')
def get_customer_by_customer_id(customer_id):
    try:
        return customer_service.get_user_by_customer_id(customer_id)
    except UserNotFoundError as e:
        return {
            "message": str(e)
        }, 404


@cc.route('/customer', methods=['POST'])
def add_customer():
    user_json_dictionary = request.get_json()
    customer_obj = Customer(user_json_dictionary['customer'], user_json_dictionary['account_number'])
    try:

        return customer_service.add_customer(customer_obj), 201
    except InvalidParameterError as e:
        return {
                "message": str(e)
                }, 400


@cc.route('/customer/<customer_id>', methods=['PUT'])
def edit_customer_by_customer_id(customer_id):
    user_json_dictionary = request.get_json()
    customer_obj = Customer(user_json_dictionary['username'], user_json_dictionary['account_number'])
    return customer_service.edit_customer_by_customer_id(customer_id, customer_obj)
