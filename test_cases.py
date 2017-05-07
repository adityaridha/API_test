import pytest
import requests
from helper import *
from hub3c_api import *

__author__      = "Muhammad Aditya Ridharrahman"
__version__     = "1.0"
__email__       = "aditya.ridharrahman@geekseat.com.au"
__status__      = "development"
__last_update__ = "10th Feb 2017"

print("######### Execute test cases #########")

class TestAccount():

    account_api = AccountAPI()
    util = Util()

    def test_register(self):
        pass

    def test_login(self):
        result = self.account_api.login()
        self.util.print_response(result)

    def test_account_list(self):
        pass

    @pytest.mark.skip(reason = "issue in login")
    def test_logout(self):
        result = self.account_api.logout()
        self.util.print_response(result)

class TestUtility():

    util = Util()

    def test_time_zone(self):
        result = requests.get(url='http://119.9.53.234:6969/api/v1/Utility/TimeZoneList')
        self.util.print_response(result)




