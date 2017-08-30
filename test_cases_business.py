import pytest
from helper import *
from hub3c_api import *

__author__      = "Muhammad Aditya Ridharrahman"
__version__     = "1.0"
__email__       = "aditya.ridharrahman@geekseat.com.au"
__status__      = "development"
__last_update__ = "10th Feb 2017"

print("######### Execute Account business cases #########")

class TestBusiness():

    business = BusinessAPI()
    util = Util()


    @pytest.mark.get_only
    def test_get_business(self):
        result = self.business.get_business()
        self.util.print_response(result, verbose = True)

    @pytest.mark.get_only
    def test_get_business_team_member(self):
        result = self.business.get_team_member()
        self.util.print_response(result, verbose=True)

    @pytest.mark.get_only
    def test_get_connected_business(self):
        result = self.business.get_connected_business()
        self.util.print_response(result, verbose=True)

    # @pytest.mark.skip(reason="not ready")
    # def test_get_business_logo(self):
    #     pass

    # def test_update_profile(self):
    #     pass
    #
    # def test_invite_team_member(self):
    #     pass
    #
    # def test_approve_connect_request(self):
    #     pass
    #
    # def test_resend_email_request(self):
    #     pass
    #
    # def test_reject_invitation(self):
    #     pass
    #
    # def test_business_profile(self):
    #     pass
    #
    # def test_simplified_business(self):
    #     pass
