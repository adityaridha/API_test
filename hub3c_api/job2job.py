import requests
import time
import datetime as dt
from configuration import *

config = GetConfig()
date = dt.datetime.utcfromtimestamp(time.time()).strftime("%Y/%m/%d %H:%M")

class Job2jobEmployerAPI():

    def get_job2job_dashboard(self):
        result = config.api_request(service_url="Job2Job/GetProjectList/514/753/0", request_type="GET")
        return result

    def draft_job(self):
        result = config.api_request(service_url="Job2Job/DraftProject/514/753/0", request_type="GET")
        return result

    def shortlisted_contractor(self):
        result = config.api_request(service_url="Job2Job/ShortlistedContractor/514/753/0", request_type="GET")
        return result

    def posted_job(self):
        result = config.api_request(service_url="Job2Job/PostedProject/514/753/0", request_type="GET")
        return result

    def inprogress_project(self):
        result = config.api_request(service_url="Job2Job/InProgressProject/514/753/0",request_type="GET")
        return result

    def searh_contractor(self):
        data = {"currency":"","hourlyRateFrom":"0.0","industry":"0","projectCompleted":"0","skills":[],"hourlyRateTo":"0.0"}
        result = config.api_request(service_url="Job2Job/SearchContractor/514/753/0", data_body=str(data))
        return result

    def post_job_time_material(self, is_draft = False):

        data = {"areaOfWork":"1",
                "averagePerHour":"500",
                "currency":"USD",
                "proposedDateFrom":"1494867600",
                "proposedDateTo":"1495818000",
                "jobDescription":"Created from API",
                "fixedPrice":"0",
                "isDraft":"false",
                "isHideJobFromContractor":"false",
                "isProposedDateLater":"false",
                "projectTitle":"From python automation {}".format(date),
                "subSkills":["Python"]}

        result = config.api_request(service_url="Job2Job/JobTimeMaterial/514/753/0",data_body= str(data))
        return  result

    def post_job_fixed_price(self):
        pass

    def edit_draft(self):
        pass

    def delete_draft(self):
        pass

    def decline_contractor(self):
        pass

    def view_candidates(self):
        pass

    def view_shortlisted(self):
        pass

    def get_whats_happening(self):
        pass

class Job2jobContractorAPI():

    def get_home(self):
        result = config.api_request(service_url="Job2Job/ContractorHome/515/754/0 ", request_type="GET")
        return result

    def get_project (self):
        result = config.api_request(service_url="Job2Job/ContractorShortlistProject/515/754/0", request_type="GET")
        return result

    def profile_view (self):
        result = config.api_request(service_url="Job2Job/ContractorProfileView/515/754/0/1", request_type="GET")
        return result

    def project_inprogress (self):
        result = config.api_request(service_url="Job2Job/ContractorInProgressProject/515/754/0", request_type="GET")
        return result

    def completed_project (self):
        result = config.api_request(service_url="Job2Job/ContractorCompletedProject/515/754/0", request_type="GET")
        return result

    def search_job(self):
        data = {"currency":"","hourlyRateFrom":"0.0","industry":"0","skills":[],"hourlyRateTo":"0.0"}
        result = config.api_request(service_url="Job2Job/SearchJob/515/754/0", data_body=str(data))
        return result



if __name__ == "__main__" :
    print("### EMPLOYER")
    employer = Job2jobEmployerAPI()
    print(employer.project_list().json())
    print(employer.draft_project().json())
    print(employer.shortlisted_contractor().json())
    print(employer.posted_project().json())
    print(employer.inprogress_project().json())
    print(employer.searh_contractor())
    print(employer.post_job_time_material())

    print("### CONTRACTOR")
    contactor = Job2jobContractorAPI()
    print(contactor.get_home().json())
    print(contactor.get_project().json())
    print(contactor.profile_view().json())
    print(contactor.project_inprogress().json())
    print(contactor.completed_project().json())
    print(contactor.search_job().json())

