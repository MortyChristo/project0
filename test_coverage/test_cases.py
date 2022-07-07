import dao.customer_dao
import dao.account_dao
from exception.positive_balance import NegativeBalanceError
from exception.invalid_amount import InvalidAmount
from exception.invalid_account import AccountNotFound
from exception.customer_not_found import UserNotFoundError
from exception.invalid_parameter import InvalidParameterError
from model.customer import Customer
from model.bank_accounts import BankAccount
from service.customer_service import CustomerService
from service.account_service import AccountService
import pytest


def testing_get_customers(mocker):
    def mock_get_customers(self):
        return [Customer("Chris", 1), Customer("Corey", 2)]
    mocker.patch('dao.customer_dao.CustomerDao.get_all_customers', mock_get_customers)

    customer_serv = CustomerService()

    actual = customer_serv.get_all_customers()

    assert actual == [
        {
            "customer_name": 'Chris',
            "customer_id": 1
         },
        {
            "customer_name": 'Corey',
            "customer_id": 2
        }
    ]


def test_positive_customer_by_id(mocker):
    def mock_customer_by_id(self, customer_id):
        if customer_id == 1:
            return Customer('Chris', 1)
        else:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_customer_by_id)
    customer_serv = CustomerService()
    actual = customer_serv.get_customer_by_id(1)

    assert actual == {
        "customer_name": 'Chris',
        "customer_id": 1
    }


def test_negative_customer_by_id(mocker):
    def mock_get_customer_by_id(self, customer_id):
        if customer_id == 1:
            return True
        else:
            return False
    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    customer_serv = CustomerService()
    with pytest.raises(UserNotFoundError) as excinfo:
        customer_serv.get_customer_by_id(200)

    assert str(excinfo.value) == "Customer with id 200 was not found"


def test_positive_delete_customer(mocker):
    def mock_customer_by_id(self, customer_id):
        if customer_id == 1:
            return Customer('Chris', 1)
        else:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_customer_by_id)
    def mock_positive_delete_customer(self, customer_id):
        if customer_id == 1:
            return True
        else:
            return False

    mocker.patch('dao.customer_dao.CustomerDao.delete_customer_by_id', mock_positive_delete_customer)
    customer_serv = CustomerService()

    actual = customer_serv.delete_customer_by_id(1)
    assert actual is None


def test_negative_delete_customer(mocker):
    def mock_negative_delete_customer(self, customer_id):
        if customer_id == 1:
            return True
        else:
            return False

    mocker.patch('dao.customer_dao.CustomerDao.delete_customer_by_id', mock_negative_delete_customer)

    customer_serv = CustomerService()

    with pytest.raises(UserNotFoundError) as excinfo:
        customer_serv.delete_customer_by_id(200)
        assert str(excinfo.value) == "Customer with 200 was not found"


def test_positive_add_customer(mocker):
    def mock_get_customer_by_id(self, customer_id):
        if customer_id == 1:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    add_customer_obj = Customer("Chris", 1)

    def mock_positive_add_customer(self, customer_obj):
        if customer_obj == add_customer_obj:
            return Customer("Chris", 1)
        else:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.add_customer', mock_positive_add_customer)
    customer_serv = CustomerService()
    actual = customer_serv.add_customer(add_customer_obj)

    assert actual == {
        "customer_name": "Chris",
        "customer_id": 1
    }


def test_positive_edit_customer(mocker):
    add_customer_obj = Customer("Chris", 1)
    new_customer_obj = Customer("Christopher", 1)

    def mock_positive_add_customer(self, customer_obj):
        if customer_obj == add_customer_obj:
            return Customer("Chris", 1)
        else:
            return None

    def mock_get_account_by_customer_id(self, customer_id):
        if customer_id == 1:

            return Customer("Chris", 1)
        else:
            return None

    def mock_edit_customer_by_id(self, customer_obj):
        if customer_obj.customer_name == 1:
            return Customer("Christopher", 1)
        else:
            return False


        mocker.patch('dao.customer_dao.CustomerDao.add_customer', mock_positive_add_customer)
        mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_account_by_customer_id)
        mocker.patch('dao.customer_dao.CustomerDao.update_user_by_id', mock_edit_customer_by_id)

        customer_serv = CustomerService()
        customer_serv.add_customer(add_customer_obj)

        actual = customer_serv.edit_customer_by_id(new_customer_obj)
        assert actual == [
            {
                "customer_name": "Christopher",
                "customer_id": 1
            }
        ]


def test_negative_edit_customer(mocker):
    new_customer_info = Customer("Christopher", 10)
    def mock_edit_customer_by_id(self, customer_obj):
        if customer_obj.customer_id == 1:
            return Customer("Chris", 1)
        else:
            return None
    mocker.patch('dao.customer_dao.CustomerDao.update_user_by_id', mock_edit_customer_by_id)
    customer_serv = CustomerService()

    with pytest.raises(UserNotFoundError) as excinfo:
        actual = customer_serv.edit_customer_by_id(new_customer_info)
    assert str(excinfo.value) == "Customer with id 10 was not found"


def test_get_accounts_by_customer_id(mocker):
    add_customer_obj = Customer("Chris", 1)
    list_of_accounts = []
    account1 = BankAccount(1, 1, 1000)
    account2 = BankAccount(1, 2, 2000)
    list_of_accounts.append(account1)
    list_of_accounts.append(account2)

    def mock_positive_add_customer(self, customer_obj):
        if customer_obj == add_customer_obj:
            return Customer("Chris", 1)
        else:
            return None

    def mock_get_account_by_customer_id(self, customer_id):
        if customer_id == 1:

            return list_of_accounts
        else:
            return None

    customer_serv = CustomerService()
    mocker.patch('dao.customer_dao.CustomerDao.add_customer', mock_positive_add_customer)
    mocker.patch('dao.account_dao.BankAccountDAO.get_all_accounts_by_customer_id', mock_get_account_by_customer_id)
    account_serv = AccountService()
    actual = account_serv.get_all_accounts_by_customer_id(1)

    assert actual == [
        {
            "account_num": 1,
            "balance": 1000
        },
        {
            "account_num": 2,
            "balance": 2000
        }
    ]


def test_negative_get_account_by_account_id(mocker):          ##testing that an invalid account_id raises error
        list_of_accounts = []
        account1 = BankAccount(1, 1, 1000)
        list_of_accounts.append(account1)


        def mock_positive_add_customer(self, customer_obj):
            if customer_obj == customer_obj:
                return Customer("Chris", 1)
            else:
                return None


        def mock_get_account_by_customer_id(self, customer_id):
            if customer_id == 1:

                return list_of_accounts
            else:
                return None

        account_serv = AccountService()
        mocker.patch('dao.customer_dao.CustomerDao.add_customer', mock_positive_add_customer)
        mocker.patch('dao.account_dao.BankAccountDAO.get_all_accounts_by_customer_id', mock_get_account_by_customer_id)

        with pytest.raises(AccountNotFound) as excinfo:
            actual = account_serv.get_account_by_id(1, 2)
        assert str(excinfo.value) == "Account 2 under customer 1 could not be found"


def test_account_by_balance_2_parameters_positive(mocker):
    add_customer_obj = Customer("Chris", 1)
    list_of_accounts = []
    account1 = BankAccount(1, 1, 1000)
    account2 = BankAccount(1, 2, 2000)
    list_of_accounts.append(account1)
    list_of_accounts.append(account2)

    def mock_get_customer_by_id(self, customer_id):
        if customer_id == 1:
            return Customer("Chris", 1)
    def mock_positive_add_customer(self, customer_obj):
        if customer_obj == add_customer_obj:
            return Customer("Chris", 1)
        else:
            return None
    def mock_get_account_by_customer_id(self, customer_id):
        if customer_id == 1:

            return BankAccount(1, 1, 1000) ##list_of_accounts
        else:
            return None
    def mock_get_account_by_balance(self, customer_id, less_than, greater_than):
        if customer_id == 1:
            account_list = []
            if less_than > -1 and greater_than < less_than:
                account_list.append(account1)
            return account_list
        else:
            return None
    def mock_add_account(self, account_obj):
        if account_obj == account2:
            return BankAccount(1, 1, 1000)
        elif account_obj == account1:
            return BankAccount(1, 2, 2000)
        else:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.add_customer', mock_positive_add_customer)
    mocker.patch('dao.account_dao.BankAccountDAO.get_all_accounts_by_customer_id', mock_get_account_by_customer_id)
    mocker.patch('dao.account_dao.BankAccountDAO.get_customer_account_by_amount', mock_get_account_by_balance)
    mocker.patch('dao.account_dao.BankAccountDAO.add_new_account', mock_add_account)
    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    customer_serv = CustomerService()
    customer_serv.add_customer(add_customer_obj)
    account_serv = AccountService()
    account_serv.add_new_account(account1)
    account_serv.add_new_account(account2)
    customer_test = customer_serv.get_customer_by_id(1)
    actual = account_serv.get_account_by_balance(1, 1500, 500)
    assert actual == [
        {
            "account_num": 1,
            "balance": 1000
        }
    ]


    ##actual = account_serv.get_account_by_balance(1, 1500, 500)


def test_account_by_balance_2_parameters_negative(mocker): ##InvalidAmount
    less_than = 20
    greater_than = 100

    def mock_get_customer_by_id(self, customer_id):
        if customer_id == 1:
            return Customer("Chris", 1)

    def mock_invalid_amount(self, customer_id, less_than, greater_than):
        if customer_id == 1:
            if less_than < greater_than:
                return None
        else:
            return BankAccount(1, 1, 1000)
    mocker.patch('dao.account_dao.BankAccountDAO.get_customer_account_by_amount', mock_invalid_amount)
    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    account_serv = AccountService()

    with pytest.raises(InvalidAmount) as excinfo:
        actual = account_serv.get_account_by_balance(1, less_than, greater_than)
    assert str(excinfo.value) == "20 should be greater than 100"


def test_account_by_balance_2_parameters_negative(mocker): ##UserNotFoundError
    less_than = 100
    greater_than = 20

    def mock_invalid_customer(self, customer_id, less_than, greater_than):
        if customer_id == 2:
            return None
        else:
            return BankAccount(1, 1, 1000)
    mocker.patch('dao.account_dao.BankAccountDAO.get_customer_account_by_amount', mock_invalid_customer)
    ##mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)
    account_serv = AccountService()

    with pytest.raises(UserNotFoundError) as excinfo:
        actual = account_serv.get_account_by_balance(2, less_than, greater_than)
    assert str(excinfo.value) == "There is no customer with customer id 2"


##def test_get_account_by_account_id_positive(mocker):
##def test_get_account_by_id_negative_customer_id(mocker):
###def test_get_account_by_id_negative_account_id(mocker):
##def test_add_account_positive(mocker):
##def test_add_account_negative(mocker):
##def test_change_account_positive(mocker):
##def test_change_account_negative(mocker):
##def test_delete_account_negative(mocker):
##def test_delete_account_positive(mocker):
