import psycopg
from model.bank_accounts import BankAccount

class BankAccountDAO:
    def get_all_accounts_by_customer_id(self, customer_id):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="YeMother6") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM todos WHERE customer_id = %s", (customer_id))
                account_list = []
                for row in cur:
                    account_list.append(BankAccount(row[0], row[1], row[3], row[4]))

                    return account_list
