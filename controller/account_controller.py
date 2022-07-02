from flask import Blueprint, request
from exception.customer_not_found import UserNotFoundError
from exception.invalid_account import AccountNotFound
from service.account_service import AccountService
from model.bank_accounts import BankAccount

ac = Blueprint('account_controller', __name__)

account_service = AccountService()


@ac.route('/customer/<customer_id>/accounts', methods=['GET'])
def get_all_accounts_by_customer_id(customer_id):
    try:
        return {
                   "accounts": account_service.get_all_accounts_by_customer_id(customer_id)
               }, 201
    except UserNotFoundError as e:
        return {
                   "message": str(e)
               }, 404


@ac.route('/customer/<customer_id>/accounts', methods=['POST'])
def add_new_account(customer_id):
    account_json_dict = request.get_json()
    account_obj = BankAccount(customer_id, True, account_json_dict['account_type'], account_json_dict['account_number'],
                              account_json_dict['balance'])
    try:
        return account_service.add_new_account(account_obj), 201

    except AccountNotFound as e:
        return {
                   "message": str(e)
               }, 404


@ac.route('/customer/<customer_id>/accounts/<account_id>')
def get_account_by_customer_id(customer_id, account_id):
    try:
        return account_service.get_account_by_id(customer_id, account_id), 201
    except AccountNotFound as e:
        return {
            "message": str(e)
        }, 405
