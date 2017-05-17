import requests
import time
import datetime as dt
from configuration import *

class ProjectsAPI():

    config = GetConfig()

    def get_project_list_by_progress(self, state = "New"):
        result = self.config.api_request(service_url="Project/GetProjectListByProgress/514/753/0/{}".format(state), request_type="GET")
        return result

    def get_project_detail(self):
        result = self.config.api_request(service_url="Project/GetProjectDetail/514/753/0/493", request_type="GET")
        return result

    def get_project_notification(self):
        result = self.config.api_request(service_url="Project/ProjectNotification/514/753/0/493", request_type="GET")
        return result

class ActivitiesAPI():

    def get_activities(self):
        result = self.config.api_request(service_url="Project/Activities/753/493", request_type="GET")
        return result

    def add_activity(self):
        pass

class TeamMemberAPI():

    config = GetConfig()
    date = dt.datetime.utcfromtimestamp(time.time()).strftime("%Y/%m/%d %H:%M")

    def get_team_member(self):
        result = self.config.api_request(service_url="Project/GetProjectTeamMember/753/493", request_type="GET")
        return result

    def update_team_member(self):
        data = {"hourlyRateCharge":"500.0",
                "hourlyRateCost":"500.0",
                "isProjectOwner":"false",
                "projectRole":"Project Role Edited from API automation {}".format(self.date),
                "timezoneId":"SE Asia Standard Time"}
        result = self.config.api_request(service_url="Project/TeamMembers/2777/753", data_body=str(data), request_type="PUT")
        return result

    def delete_team_member(self):
        pass

    def add_team_member(self):
        pass

class BulletinAPI():

    config = GetConfig()
    date = dt.datetime.utcfromtimestamp(time.time()).strftime("%Y/%m/%d %H:%M")

    def get_project_bulletin(self):
        result = self.config.api_request(service_url="Project/getProjectBulletin/514/753/0/1939", request_type="GET")
        return result

    def like_unlike_bulletin(self):
        result = self.config.api_request(service_url="Project/likeOrUnlikeProjectBulletin/514/753/0/1684", request_type="POST")
        return result

    def create_bulletin(self):
        data = {"postId":"0","postMessage":"add buletin from python {}".format(self.date),"projectId":"1939"}
        result = self.config.api_request(service_url="Project/addProjectBulletin/753", data_body=str(data))
        return result

    def create_bulletin_comment(self):
        data = {"postId":"1684","postMessage":"comment from python {}".format(self.date),"projectId":"1939"}
        result = self.config.api_request(service_url="Project/addProjectBulletin/753", data_body=str(data))
        return result

    def get_project_bulletin_comment(self):
        result = self.config.api_request(service_url="Project/BulletinComment/1939/1677", request_type="GET")
        return result

    def update_project_bulletin(self):
        data = {"postId":"1684","postMessage":"buletin from python edited on {}".format(self.date)}
        result = self.config.api_request(service_url="Project/UpdateProjectBulletin/514/753/0", data_body=str(data))
        return result

    def delete_bulletin_comment(self):
        pass

class NotesAPI():

    config = GetConfig()
    date = dt.datetime.utcfromtimestamp(time.time()).strftime("%Y/%m/%d %H:%M")

    def get_project_notes(self):
        result = self.config.api_request(service_url="Project/GetProjectNoteList/514/753/0/493", request_type="GET")
        return result

    def add_project_note(self):
        data = {"dateCreated":"1495006686",
                "projectId":"1939",
                "projectNoteId":"0",
                "description":"New note from python API {}".format(self.date),
                "subject":""}
        result = self.config.api_request(service_url="Project/NewProjectNote/514/753/0", data_body=str(data))
        return result

    def update_project_note(self):
        data = {"dateCreated":"1495006686",
                "projectId":"1939",
                "projectNoteId":"505",
                "description":"New note from python API 2017/05/17 07:43\n\nedited\n"
                              "Python is a widely used high-level programming language for general-purpose programming "
                              "created by Guido van Rossum and first released in 1991. An interpreted language, "
                              "Python has a design philosophy which emphasizes code readability "
                              "(notably using whitespace indentation to delimit code blocks rather than curly braces or keywords), "
                              "and a syntax which allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java",
                "subject":"Edited from python script {}".format(self.date)}
        result = self.config.api_request(service_url="Project/UpdateProjectNote/514/753/0", data_body=str(data))
        return result

class AttachmentAPI():

    config = GetConfig()
    date = dt.datetime.utcfromtimestamp(time.time()).strftime("%Y/%m/%d %H:%M")

    def get_project_attachment(self):
        result = self.config.api_request(service_url="Project/GetProjectAttachments/514/753/0/493", request_type="GET")
        return result

    def upload_attachment(self):
        pass

    def download_attachment(self):
        pass

    def delete_attachment(self):
        pass
        #Project/1939/Attachments/33578/753

    def edit_attachment(self):
        data = {"fileName":"Edited from python script {}.jpg".format(self.date)}
        result = self.config.api_request(service_url="Project/1939/Attachments/33580/753", data_body=str(data), request_type="PUT")
        return result

class AgendaAPI():

    def get_project_agenda(self):
        result = self.config.api_request(service_url="Project/GetProjectAgendaList/493/753", request_type="GET")
        return result

class TimesheetAPI():

    def get_project_timesheet(self):
        result = self.config.api_request(service_url="Project/ProjectTimesheet/514/753/0/493", request_type="GET")
        return result




if __name__ == "__main__" :
    projects = ProjectsAPI()
    bulletin = BulletinAPI()
    team_member = TeamMemberAPI()
    notes = NotesAPI()
    # print(projects.get_project_list_by_progress(state="New").text)
    # print(projects.get_project_list_by_progress(state="InProgress").text)
    # print(projects.get_project_list_by_progress(state="OnHold").text)
    # print(projects.get_project_list_by_progress(state="Cancelled").text)
    # print(projects.get_project_list_by_progress(state="Complete").text)
    # print(projects.get_project_detail().json()["status"]['type'])
    # print(projects.get_project_notification().json())

    #TeamMember
    # print(team_member.get_team_member().json())
    # print(team_member.update_team_member().json())

    #Bulletin
    # print(bulletin.get_project_bulletin().json()["data"])
    # print(bulletin.get_project_bulletin_comment().json()["data"])
    # print(bulletin.like_unlike_bulletin())
    # # print(bulletin.create_bulletin().text)
    # print(bulletin.create_bulletin_comment().text)
    # print(bulletin.update_project_bulletin().status_code)

    #projectnotes
    # print(notes.update_project_note())

    #attachment
    attachment = AttachmentAPI()
    print(attachment.edit_attachment())
