from dao.customer_dao import CustomerDao
from exception.invalid_parameter import InvalidParameterError
from exception.customer_not_found import UserNotFoundError


class CustomerService:

    def __init__(self):
        self.customer_dao = CustomerDao()

    def get_all_customers(self):
        list_of_user_objects = self.customer_dao.get_all_customers()
        list_of_user_dictionaries = []
        for user_obj in list_of_user_objects:
            list_of_user_dictionaries.append(user_obj.to_dict())

        return list_of_user_dictionaries

    def get_customer_by_id(self, customer_id):
        customer_obj = self.customer_dao.get_customer_by_id(customer_id)
        if not customer_obj:
            raise UserNotFoundError(f"User with id {customer_id} was not found")

        return customer_obj.to_dict()

    def delete_customer_by_id(self, customer_id):

        if not self.customer_dao.get_customer_by_id(customer_id):
            raise UserNotFoundError(f"Customer with id {customer_id} was not found")

        self.customer_dao.delete_customer_by_id(customer_id)


    def add_customer(self, customer_obj):
    ##    if len(customer_obj.customer_name) < 2:
     ##       raise InvalidParameterError("Customer name must be longer")

        added_user_object = self.customer_dao.add_customer(customer_obj)
        return added_user_object.to_dict()

    def edit_customer_by_id(self, customer_obj):
        updated_customer_obj = self.customer_dao.update_user_by_id(customer_obj)
        if updated_customer_obj is None:
            raise UserNotFoundError(f"User with id {customer_obj.id} was not found")

        return updated_customer_obj.to_dict()
