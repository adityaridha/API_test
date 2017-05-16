import requests
import time
import datetime as dt
from configuration import *



class Job2jobEmployerAPI():

    config = GetConfig()
    date = dt.datetime.utcfromtimestamp(time.time()).strftime("%Y/%m/%d %H:%M")

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

    def searh_contractor(self):
        data = {"currency":"","hourlyRateFrom":"0.0","industry":"0","projectCompleted":"0","skills":[],"hourlyRateTo":"0.0"}
        search_contractor_result = self.config.api_request(service_url="Job2Job/SearchContractor/514/753/0", data_body=str(data))
        return search_contractor_result

    def post_job_time_material(self, is_draft = False):

        data = {"areaOfWork":"1",
                "averagePerHour":"500",
                "currency":"USD",
                "proposedDateFrom":"1494867600",
                "proposedDateTo":"1495818000",
                "jobDescription":"Created from API",
                "fixedPrice":"0","isDraft":"false",
                "isHideJobFromContractor":"false",
                "isProposedDateLater":"false",
                "projectTitle":"From python automation {}".format(self.date),
                "subSkills":["Software Accounting"]
                }

        result = self.config.api_request(service_url="Job2Job/JobTimeMaterial/514/753/0",data_body= str(data))
        return  result

    def edit_draft(self):
        pass

    def reject_contractor(self):
        pass

    def view_candidates(self):
        pass

    def view_shotliste(self):
        pass


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

    def search_job(self):
        pass



if __name__ == "__main__" :
    print("### EMPLOYER")
    employer = Job2jobEmployerAPI()
    # print(employer.project_list().json())
    # print(employer.draft_project().json())
    # print(employer.shortlisted_contractor().json())
    # print(employer.posted_project().json())
    # print(employer.inprogress_project().json())
    print(employer.searh_contractor())
    print(employer.post_job_time_material())

    # print("### CONTRACTOR")
    # employer = Job2jobContractorAPI()
    # print(employer.get_home().json())
    # print(employer.get_project().json())
    # print(employer.profile_view().json())
    # print(employer.project_inprogress().json())
    # print(employer.completed_project().json())

