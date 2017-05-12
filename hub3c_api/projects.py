import requests
from configuration import *

class ProjectsAPI():

    config = GetConfig()

    def get_project_list_by_progress(self, state = "New"):
        get_progress = self.config.api_request(service_url="Project/GetProjectListByProgress/514/753/0/{}".format(state), request_type="GET")
        return get_progress

    def get_project_detail(self):
        get_project_detail_result = self.config.api_request(service_url="Project/GetProjectDetail/514/753/0/493", request_type="GET")
        return get_project_detail_result

    def get_project_notification(self):
        get_project_notification_result = self.config.api_request(service_url="Project/ProjectNotification/514/753/0/493", request_type="GET")
        return get_project_notification_result

    def get_activities(self):
        get_activities_result = self.config.api_request(service_url="Project/Activities/753/493", request_type="GET")
        return get_activities_result

    def get_team_member(self):
        get_team_member_result = self.config.api_request(service_url="Project/GetProjectTeamMember/753/493", request_type="GET")
        return get_team_member_result

    def get_project_bulletin(self):
        get_project_bulletin_result = self.config.api_request(service_url="Project/getProjectBulletin/514/753/0/493", request_type="GET")
        return get_project_bulletin_result

    def get_project_notes(self):
        get_project_notes_result = self.config.api_request(service_url="Project/GetProjectNoteList/514/753/0/493", request_type="GET")
        return get_project_notes_result

    def get_project_attachment(self):
        get_project_attachment_result = self.config.api_request(service_url="Project/GetProjectAttachments/514/753/0/493", request_type="GET")
        return get_project_attachment_result

    def get_project_agenda(self):
        get_project_agenda_result = self.config.api_request(service_url="Project/GetProjectAgendaList/493/753", request_type="GET")
        return get_project_agenda_result

    def get_project_timesheet(self):
        get_project_timesheet_result = self.config.api_request(service_url="Project/ProjectTimesheet/514/753/0/493", request_type="GET")
        return get_project_timesheet_result



if __name__ == "__main__" :
    projects = ProjectsAPI()
    # print(projects.get_project_list_by_progress(state="New").text)
    # print(projects.get_project_list_by_progress(state="InProgress").text)
    # print(projects.get_project_list_by_progress(state="OnHold").text)
    # print(projects.get_project_list_by_progress(state="Cancelled").text)
    # print(projects.get_project_list_by_progress(state="Complete").text)
    #
    print(projects.get_project_detail().json()["status"]['type'])
    print(projects.get_project_notification().json()["status"]['type'])
    print(projects.get_activities().json()["status"]['type'])
    print(projects.get_team_member().json())
    print(projects.get_project_bulletin().json()["status"]['type'])
    print(projects.get_project_notes().json()["status"]['type'])
    print(projects.get_project_attachment().json())
    print(projects.get_project_agenda().json()["status"]['type'])
    print(projects.get_project_timesheet().json()["status"]['type'])


