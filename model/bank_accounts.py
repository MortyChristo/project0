class BankAccount:
        def __init__(self, customer_id, account_num, balance):
            self.customer_id = customer_id

            self.account_num = account_num
            self.balance = balance


        def to_dict(self):
            return {
                "account_num": self.account_num,
                "balance": self.balance
            }
