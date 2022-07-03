import psycopg
from model.bank_accounts import BankAccount
from exception.invalid_amount import InvalidAmount

class BankAccountDAO:
    def get_all_accounts_by_customer_id(self, customer_id):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="YeMother6") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM account WHERE customer_id = %s", (customer_id,))
                account_list = []
                for row in cur:
                    account_list.append(BankAccount(row[0], row[1], row[2]))

                return account_list
    def get_customer_account_by_amount(self, customer_id, less_than, greater_than):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="YeMother6") as conn:
            with conn.cursor() as cur:
                account_list = []
                cur.execute("SELECT * FROM account WHERE customer_id = %s AND %s < balance AND balance < %s", (customer_id, greater_than, less_than))
                for row in cur:
                    account_list.append(BankAccount(row[0], row[1], row[2]))

            return account_list


    def add_new_account(self, account_obj):

        customer_id = account_obj.customer_id
        account_num = account_obj.account_num
        balance = account_obj.balance

        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="YeMother6") as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO account(customer_id, account_num, balance)"
                            " VALUES (%s, %s, %s) RETURNING *", (customer_id, account_num, balance))
                account_row = cur.fetchone()
                conn.commit()

                return BankAccount(customer_id, account_num, balance)

    def get_account_by_id(self, customer_id, account_num):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="YeMother6") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM account WHERE customer_id = %s AND account_num = %s", (customer_id, account_num))

                account_row = cur.fetchone()
                if not account_row:
                    return None
                customer_id = account_row[0]
                account_num = account_row[1]
                balance = account_row[2]

                return BankAccount(customer_id, account_num, balance)

    def change_account_by_id(self, account_obj):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="YeMother6") as conn:
                with conn.cursor() as cur:
                    cur.execute("UPDATE account SET balance = %s WHERE customer_id = %s and account_num = %s RETURNING *", (account_obj.balance, account_obj.customer_id, account_obj.account_num))
                    conn.commit()
                    account_row = cur.fetchone()
                    if account_row is None:
                        return None
                    return BankAccount(account_row[0], account_row[1], account_row[2])

    def delete_account_by_id(self, customer_id, account_num):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="YeMother6") as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM account WHERE customer_id = %s AND account_num = %s", (customer_id, account_num))
                rows_deleted = cur.rowcount
                if rows_deleted != 1:
                   return False
                else:
                    conn.commit()
                    return True