import psycopg
from model.bank_accounts import BankAccount

class BankAccountDAO:
    def get_all_accounts_by_customer_id(self, customer_id):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="YeMother6") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM account WHERE customer_id = %s", (customer_id,))
                print("executed select")
                account_list = []
                for row in cur:
                    account_list.append(BankAccount(row[0], row[1], row[2], row[3], row[4]))

                return account_list

    def add_new_account(self, account_obj):

        customer_id = account_obj.customer_id
        account_active = account_obj.account_active
        account_type = account_obj.account_type
        account_num = account_obj.account_num
        balance = account_obj.balance

        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="YeMother6") as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO account(customer_id, account_active, account_type, account_num, balance)"
                            " VALUES (%s, %s, %s, %s, %s) RETURNING *", (customer_id, account_active, account_type, account_num, balance))
                account_row = cur.fetchone()
                conn.commit()

                return BankAccount(customer_id, account_active, account_type, account_num, balance)

    def get_account_by_id(self, customer_id, account_id):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="YeMother6") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM account WHERE customer_id = %s AND account_num = %s", (customer_id, account_id))

                account_row = cur.fetchone()
                if not account_row:
                    return None
                customer_id = account_row[0]
                account_active = account_row[1]
                account_type = account_row[2]
                account_num = account_row[3]
                balance = account_row[4]

                return BankAccount(customer_id, account_active, account_type, account_num, balance)

## def update_account_by_id(self, account_obj):
  ##      return pass

 ##   def delete_account_by_id(self, account_id):
  ##      return pass
