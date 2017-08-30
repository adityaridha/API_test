import pytest
from helper import *
from hub3c_api import *

__author__      = "Muhammad Aditya Ridharrahman"
__version__     = "1.0"
__email__       = "aditya.ridharrahman@geekseat.com.au"
__status__      = "development"
__last_update__ = "10th Feb 2017"

print("######### Execute Account test cases #########")

class TestJob2job():

    employer = Job2jobEmployerAPI()
    contractor = Job2jobContractorAPI()
    util = Util()

    @pytest.mark.get_only
    def test_employer_get_project_list(self):
        result = self.employer.get_job2job_dashboard()
        self.util.print_response(result)

    @pytest.mark.get_only
    def test_employer_get_draft_project(self):
        result = self.employer.draft_job()
        self.util.print_response(result)

    def test_employer_get_inprogress_project(self):
        result = self.employer.inprogress_project()
        self.util.print_response(result)

    @pytest.mark.get_only
    def test_employer_get_posted_project(self):
        result = self.employer.posted_job()
        self.util.print_response(result)

    @pytest.mark.get_only
    def test_employer_get_shortlisted_contractor(self):
        result = self.employer.shortlisted_contractor()
        self.util.print_response(result)

    @pytest.mark.get_only
    def test_employer_search_contractor(self):
        result = self.employer.searh_contractor()
        self.util.print_response(result)

    def test_employer_post_job_time_material(self):
        result = self.employer.post_job_time_material()
        self.util.print_response(result)

    @pytest.mark.get_only
    def test_contractor_get_completed_project(self):
        result = self.contractor.completed_project()
        self.util.print_response(result)

    @pytest.mark.get_only
    def test_contractor_get_home(self):
        result = self.contractor.get_home()
        self.util.print_response(result)