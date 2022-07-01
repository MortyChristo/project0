from dao.customer_dao import UserDao
from dao.account_dao import BankAccountDAO
from exception.customer_not_found import UserNotFoundError

class AccountService:

    def __init__(self):
        self.account_dao = BankAccountDAO()
        self.user_dao = UserDao()

    def get_all_accounts_by_customer_id(self, customer_id):
        if self.user_dao.get_user_by_username(customer_id) is None:
            raise UserNotFoundError(f"Customer id {customer_id} not correct")

        return list(map(lambda a: a.to_dict(), self.account_dao.get_all_accounts_by_customer_id(customer_id)))
