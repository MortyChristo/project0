class BankAccount:
        def __init__(self, customer_id, account_active, account_type, account_num, balance):
            self.customer_id = customer_id
            self.account_active = account_active
            self.account_type = account_type
            self.account_num = account_num
            self.balance = balance

        def to_dict(self):
            return {
                "customer_id": self.customer_id,
                "active": self.account_active,
                "account_type": self.account_type,
                "account_number": self.account_num,
                "balance": self.balance
            }
