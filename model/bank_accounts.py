class BankAccount:
        def __init__(self, user_id, account_active, account_type, account_num):
            self.user_id = user_id
            self.account_active = account_active
            self.account_type = account_type
            self.account_num = account_num

        def to_dict(self):
            return {
                "customer_id": self.user_id,
                "active": self.account_active,
                "account_type": self.account_type,
                "account_number": self.account_num
            }
