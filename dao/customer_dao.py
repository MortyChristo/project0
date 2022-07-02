from model.customer import Customer
import psycopg
import copy

class CustomerDao:
    def get_all_customers(self):
         with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="YeMother6") as conn:
             with conn.cursor()as cur:
                cur.execute("SELECT * FROM customer")

                list_of_customers = []

                for customer in cur:
                    customers_name = customer[0]
                    customer_id = customer[1]

                    customer_obj = Customer(customers_name,customer_id)
                    list_of_customers.append(customer_obj)

                return list_of_customers

    def delete_customer_by_id(self, customer_id):  ##delete
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="YeMother6") as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM customer WHERE customer_id = %s", (customer_id,))
                rows_deleted = cur.rowcount
                if rows_deleted != 1:
                    conn.commit()
                    return True
                else:
                    conn.commit()
                    return False

    def add_customer(self, customer_object):

        customer_name = customer_object.customer
        customer_id = customer_object.customer_id

        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="YeMother6") as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO customer (customer_name, customer_id) VALUES (%s, %s) RETURNING *", (customer_name, customer_id))
                user_row_that_was_just_inserted = cur.fetchone()
                conn.commit()
                return Customer(user_row_that_was_just_inserted[0], user_row_that_was_just_inserted[1])

    def get_customer_by_id(self, customer_id):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="YeMother6") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM customer WHERE customer_id = %s", (customer_id,))

                user_row = cur.fetchone()
                if not user_row:
                    return None

                customer_name = user_row[0]
                customer_id = user_row[1]

                return Customer(customer_name, customer_id)

    def update_user_by_id(self, customer_object):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres", password="YeMother6") as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE customer SET customer_name = %s WHERE customer_id = %s RETURNING *", (customer_object.customer_name, customer_object.customer_id))
                conn.commit()
                updated_user_row = cur.fetchone()
                if updated_user_row is None:
                    return None
                return Customer(updated_user_row[0], updated_user_row[1])
