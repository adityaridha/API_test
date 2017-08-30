import pytest
from helper import *
from hub3c_api import *

__author__      = "Muhammad Aditya Ridharrahman"
__version__     = "1.0"
__email__       = "aditya.ridharrahman@geekseat.com.au"
__status__      = "development"
__last_update__ = "10th Feb 2017"

print("######### Execute Account test cases #########")

util = Util()

class TestAccount():

    account_api = AccountAPI()
    util = Util()

    @pytest.mark.auth_set
    def test_login(self):
        result = self.account_api.login()
        self.util.print_response(result, verbose=True)

    @pytest.mark.auth_set
    def test_register(self):
        result = self.account_api.register()
        self.util.print_response(result, verbose=True)

    @pytest.mark.get_only
    @pytest.mark.auth_set
    def test_account_list(self):
        result = self.account_api.account_list()
        self.util.print_response(result, verbose=True)

    @pytest.mark.auth_set
    def test_logout(self):
        result = self.account_api.logout()
        self.util.print_response(result, verbose=True)

    @pytest.mark.auth_set
    def pytesttest_switch_account(self):
        result = self.account_api.switch_account()
        self.util.print_response(result, verbose=True)

    @pytest.mark.auth_set
    def test_forgot_password(self):
        result = self.account_api.forgot_password()
        self.util.print_response(result, verbose=True)




