class Customer:
    def __init__(self, customer, customer_id):
        self.customer = customer
        self.customer_id = customer_id


    def to_dict(self):
        return {
            "customer": self.customer,
            "user id": self.customer_id
        }
