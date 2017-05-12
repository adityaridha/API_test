import requests
from configuration import *

class Job2jobAPI():

    config = GetConfig()

    def get_project_list(self):
        get_dashboard = self.config.api_request(service_url="Job2Job/GetProjectList/514/753/0", request_type="GET")
        return get_dashboard

    def employer_get_draft_project(self):
        get_dashboard = self.config.api_request(service_url="Job2Job/DraftProject/514/753/0", request_type="GET")
        return get_dashboard

    def employer_get_shortlisted_contractor(self):
        get_dashboard = self.config.api_request(service_url="Job2Job/ShortlistedContractor/514/753/0", request_type="GET")
        return get_dashboard

    def employer_get_posted_project(self):
        get_dashboard = self.config.api_request(service_url="Job2Job/PostedProject/514/753/0", request_type="GET")
        return get_dashboard

    def employer_get_inprogress_project(self):
        get_dashboard = self.config.api_request(service_url="Job2Job/InProgressProject/514/753/0", request_type="GET")
        return get_dashboard


if __name__ == "__main__" :
    job2job = Job2jobAPI()
    print(job2job.get_project_list().text)
    print(job2job.employer_get_draft_project().text)
    print(job2job.employer_get_shortlisted_contractor().text)
    print(job2job.employer_get_posted_project().text)
    print(job2job.employer_get_inprogress_project().text)

