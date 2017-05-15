import requests
from configuration import *


class Job2jobEmployerAPI():

    config = GetConfig()

    def project_list(self):
        get_dashboard = self.config.api_request(service_url="Job2Job/GetProjectList/514/753/0", request_type="GET")
        return get_dashboard

    def draft_project(self):
        get_dashboard = self.config.api_request(service_url="Job2Job/DraftProject/514/753/0", request_type="GET")
        return get_dashboard

    def shortlisted_contractor(self):
        get_dashboard = self.config.api_request(service_url="Job2Job/ShortlistedContractor/514/753/0", request_type="GET")
        return get_dashboard

    def posted_project(self):
        get_dashboard = self.config.api_request(service_url="Job2Job/PostedProject/514/753/0", request_type="GET")
        return get_dashboard

    def inprogress_project(self):
        get_dashboard = self.config.api_request(service_url="Job2Job/InProgressProject/514/753/0",request_type="GET")
        return get_dashboard


class Job2jobContractorAPI():

    config = GetConfig()

    def get_home(self):
        get_contractor_home_result = self.config.api_request(service_url="Job2Job/ContractorHome/515/754/0 ", request_type="GET")
        return get_contractor_home_result

    def get_project (self):
        get_dashboard = self.config.api_request(service_url="Job2Job/ContractorShortlistProject/515/754/0", request_type="GET")
        return get_dashboard

    def profile_view (self):
        get_dashboard = self.config.api_request(service_url="Job2Job/ContractorProfileView/515/754/0/1", request_type="GET")
        return get_dashboard

    def project_inprogress (self):
        get_dashboard = self.config.api_request(service_url="Job2Job/ContractorInProgressProject/515/754/0", request_type="GET")
        return get_dashboard

    def completed_project (self):
        get_dashboard = self.config.api_request(service_url="Job2Job/ContractorCompletedProject/515/754/0", request_type="GET")
        return get_dashboard


if __name__ == "__main__" :
    print("### EMPLOYER")
    employer = Job2jobEmployerAPI()
    print(employer.project_list().json())
    print(employer.draft_project().json())
    print(employer.shortlisted_contractor().json())
    print(employer.posted_project().json())
    print(employer.inprogress_project().json())

    print("### CONTRACTOR")
    employer = Job2jobContractorAPI()
    print(employer.get_home().json())
    print(employer.get_project().json())
    print(employer.profile_view().json())
    print(employer.project_inprogress().json())
    print(employer.completed_project().json())

