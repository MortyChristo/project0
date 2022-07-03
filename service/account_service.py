from dao.customer_dao import CustomerDao
from dao.account_dao import BankAccountDAO
from exception.customer_not_found import UserNotFoundError
from exception.invalid_account import AccountNotFound
from exception.invalid_amount import InvalidAmount

class AccountService:

    def __init__(self):
        self.account_dao = BankAccountDAO()
        self.customer_dao = CustomerDao()

    def get_all_accounts_by_customer_id(self, customer_id):
        if self.customer_dao.get_customer_by_id(customer_id) is None:
            raise UserNotFoundError(f"Customer id {customer_id} not correct")

        return list(map(lambda a: a.to_dict(), self.account_dao.get_all_accounts_by_customer_id(customer_id)))

    def get_account_by_balance(self, customer_id, less_than, greater_than):
        if self.customer_dao.get_customer_by_id(customer_id) is None:
            raise UserNotFoundError(f"Customer id {customer_id} not correct")
       ## if less_than < greater_than:
        ##    raise InvalidAmount(f"{less_than} should be greater than {greater_than}")
        return list(map(lambda a: a.to_dict(), self.account_dao.get_customer_account_by_amount(customer_id, less_than, greater_than)))

    def add_new_account(self, account_obj):
        new_account_obj = self.account_dao.add_new_account(account_obj)
        return new_account_obj.to_dict()

    def get_account_by_id(self, customer_id, account_id):
        account_obj = self.account_dao.get_account_by_id(customer_id, account_id)
        if not account_obj:
            raise AccountNotFound(f"Account {account_id} under customer {customer_id} could not be found")

        return account_obj.to_dict_account()

    def change_account_by_id(self, account_obj):
        new_account_obj = self.account_dao.change_account_by_id(account_obj)
        if new_account_obj is None:
            raise AccountNotFound(f"Account {account_obj.account_num} cannot be located")
        return new_account_obj.to_dict()

    def delete_account_by_num(self, customer_id, account_num):
        if not self.account_dao.get_account_by_id(customer_id, account_num):
            raise AccountNotFound(f"Account number {account_num} under customer id {customer_id} was not found")
        self.account_dao.delete_account_by_id(customer_id, account_num)

