from dao.customer_dao import CustomerDao
from dao.account_dao import BankAccountDAO
from exception.customer_not_found import UserNotFoundError
from exception.invalid_account import AccountNotFound

class AccountService:

    def __init__(self):
        self.account_dao = BankAccountDAO()
        self.customer_dao = CustomerDao()

    def get_all_accounts_by_customer_id(self, customer_id):
        if self.customer_dao.get_customer_by_id(customer_id) is None:
            raise UserNotFoundError(f"Customer id {customer_id} not correct")

        return list(map(lambda a: a.to_dict(), self.account_dao.get_all_accounts_by_customer_id(customer_id)))

    def add_new_account(self, account_obj):
        new_account_obj = self.account_dao.add_new_account(account_obj)
        return new_account_obj.to_dict()

    def get_account_by_id(self, customer_id, account_id):
        account_obj = self.account_dao.get_account_by_id(customer_id, account_id)
        if not account_obj:
            raise AccountNotFound(f"The account {account_id} under customer {customer_id} could not be found")

        return account_obj.to_dict()


