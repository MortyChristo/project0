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
    account_obj = BankAccount(customer_id, account_json_dict['account_num'], account_json_dict['balance'])
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

@ac.route('/customer/<customer_id>/accounts/<account_num>', methods= ['PUT'])
def change_account_by_id(customer_id, account_num):
    try:
        account_json_dict = request.get_json()

        return account_service.change_account_by_id(BankAccount(customer_id, account_num, account_json_dict['balance']))

    except AccountNotFound as e:
        return {
            "message": str(e)
        }, 404

@ac.route('/customer/<customer_id>/accounts/<account_num>', methods= ['DELETE'])
def delete_account_by_number(customer_id, account_num):
    try:
        account_service.delete_account_by_num(customer_id, account_num)

        return {
            "message": f"Account {account_num} under customer id {customer_id} was deleted"
        }, 201
    except AccountNotFound as e:
        return {
            "message": str(e)
        }, 404
