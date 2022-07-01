from flask import Blueprint
from exception.customer_not_found import UserNotFoundError
from service.account_service import AccountService

ac = Blueprint('account_controller', __name__)

account_service = AccountService()

ac.route('/customers/<customer_id>/accounts')


def get_all_accounts_by_customer_id(customer_id):
    try:
        return {
            "accounts": account_service.get_all_accounts_by_customer_id(customer_id)
        }
    except UserNotFoundError as e:
        return {
                   "message": str(e)
               }, 404
