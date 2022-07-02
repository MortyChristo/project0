class Customer:
    def __init__(self, customer_name, customer_id):
        self.customer_name = customer_name
        self.customer_id = customer_id

    def to_dict(self):
        return {
            "customer_name": self.customer_name,
            "customer_id": self.customer_id
        }
