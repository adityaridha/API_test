import pytest
import requests
from helper import *
from hub3c_api import *

__author__      = "Muhammad Aditya Ridharrahman"
__version__     = "1.0"
__email__       = "aditya.ridharrahman@geekseat.com.au"
__status__      = "development"
__last_update__ = "10th Feb 2017"

print("######### Execute Utility test cases #########")


class TestUtility():

    util = Util()

    @pytest.mark.get_only
    def test_time_zone(self):
        result = requests.get(url='http://54.206.115.140:6971/api/v1/Utility/TimeZoneList')
        self.util.print_response(result)
