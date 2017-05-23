import requests
import time
import datetime as dt
from configuration import *

config = GetConfig()
date = dt.datetime.utcfromtimestamp(time.time()).strftime("%Y/%m/%d %H:%M")

class ProjectsAPI():

    def get_project_list_by_progress(self, state = "New"):
        result = config.api_request(service_url="Project/GetProjectListByProgress/514/753/0/{}".format(state), request_type="GET")
        return result

    def get_project_detail(self):
        result = config.api_request(service_url="Project/GetProjectDetail/514/753/0/493", request_type="GET")
        return result

    def get_project_notification(self):
        result = config.api_request(service_url="Project/ProjectNotification/514/753/0/493", request_type="GET")
        return result

class ActivitiesAPI():

    def get_activities(self):
        result = config.api_request(service_url="Project/Activities/753/493", request_type="GET")
        return result

    def add_activity(self):
        pass

class TeamMemberAPI():

    def get_team_member(self):
        result = config.api_request(service_url="Project/GetProjectTeamMember/753/493", request_type="GET")
        return result

    def update_team_member(self):
        data = {"hourlyRateCharge":"500.0",
                "hourlyRateCost":"500.0",
                "isProjectOwner":"false",
                "projectRole":"Project Role Edited from API automation {}".format(date),
                "timezoneId":"SE Asia Standard Time"}
        result = config.api_request(service_url="Project/TeamMembers/2777/753", data_body=str(data), request_type="PUT")
        return result

    def delete_team_member(self):
        pass

    def add_team_member(self):
        pass

class BulletinAPI():

    def get_project_bulletin(self):
        result = config.api_request(service_url="Project/getProjectBulletin/514/753/0/1939", request_type="GET")
        return result

    def like_unlike_bulletin(self):
        result = config.api_request(service_url="Project/likeOrUnlikeProjectBulletin/514/753/0/1684", request_type="POST")
        return result

    def create_bulletin(self):
        data = {"postId":"0","postMessage":"add buletin from python {}".format(date),"projectId":"1939"}
        result = config.api_request(service_url="Project/addProjectBulletin/753", data_body=str(data))
        return result

    def create_bulletin_comment(self):
        data = {"postId":"1684","postMessage":"comment from python {}".format(date),"projectId":"1939"}
        result = config.api_request(service_url="Project/addProjectBulletin/753", data_body=str(data))
        return result

    def get_project_bulletin_comment(self):
        result = config.api_request(service_url="Project/BulletinComment/1939/1677", request_type="GET")
        return result

    def update_project_bulletin(self):
        data = {"postId":"1684","postMessage":"buletin from python edited on {}".format(date)}
        result = config.api_request(service_url="Project/UpdateProjectBulletin/514/753/0", data_body=str(data))
        return result

    def delete_bulletin_comment(self):
        pass

class NotesAPI():

    def get_project_notes(self):
        result = config.api_request(service_url="Project/GetProjectNoteList/514/753/0/493", request_type="GET")
        return result

    def add_project_note(self):
        data = {"dateCreated":"1495006686",
                "projectId":"1939",
                "projectNoteId":"0",
                "description":"New note from python API {}".format(date),
                "subject":""}
        result = config.api_request(service_url="Project/NewProjectNote/514/753/0", data_body=str(data))
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
                "subject":"Edited from python script {}".format(date)}
        result = config.api_request(service_url="Project/UpdateProjectNote/514/753/0", data_body=str(data))
        return result

class AttachmentAPI():

    def get_project_attachment(self):
        result = config.api_request(service_url="Project/GetProjectAttachments/514/753/0/493", request_type="GET")
        return result

    def upload_attachment(self):
        pass

    def download_attachment(self):
        pass

    def delete_attachment(self):
        pass
        #Project/1939/Attachments/33578/753

    def edit_attachment(self):
        data = {"fileName":"Edited from python script {}.jpg".format(date)}
        result = config.api_request(service_url="Project/1939/Attachments/33580/753", data_body=str(data), request_type="PUT")
        return result

class AgendaAPI():

    def get_project_agenda(self):
        result = config.api_request(service_url="Project/GetProjectAgendaList/493/753", request_type="GET")
        return result

    def add_agenda(self):

        data = {"date":"{}".format(int(time.time())),
                "description":"New agenda",
                "projectId":"1939",
                "title":"From Python Script {}".format(date)}

        result = config.api_request(service_url="Project/AddProjectAgenda/753", data_body=str(data), request_type="POST")
        return result

    def edit_agenda(self):

        data = {"date":"1495159260",
                "description":"New agenda",
                "projectAgendaId":"246",
                "projectid":"1939",
                "title":"Edited From Python Script {}".format(date)}


        result = config.api_request(service_url="Project/AddProjectAgenda/753", data_body=str(data), request_type="POST")
        return result

    def delete_agenda(self):
        pass

class TimesheetAPI():

    def get_project_timesheet(self):
        result = config.api_request(service_url="Project/ProjectTimesheet/514/753/0/493", request_type="GET")
        return result

    def get_activity_timesheet(self):
        pass

    def get_team_member_activities(self):
        pass

    def add_timesheet(self):
        pass

    def edit_timesheet(self):
        pass




if __name__ == "__main__" :
    projects = ProjectsAPI()
    bulletin = BulletinAPI()
    team_member = TeamMemberAPI()
    notes = NotesAPI()
    print(projects.get_project_list_by_progress(state="New").text)
    print(projects.get_project_list_by_progress(state="InProgress").text)
    print(projects.get_project_list_by_progress(state="OnHold").text)
    print(projects.get_project_list_by_progress(state="Cancelled").text)
    print(projects.get_project_list_by_progress(state="Complete").text)
    print(projects.get_project_detail().json()["status"]['type'])
    print(projects.get_project_notification().json())

    #TeamMember
    print(team_member.get_team_member().json())
    print(team_member.update_team_member().json())

    # Bulletin
    print(bulletin.get_project_bulletin().json()["data"])
    print(bulletin.get_project_bulletin_comment().json()["data"])
    print(bulletin.like_unlike_bulletin())
    print(bulletin.create_bulletin().text)
    print(bulletin.create_bulletin_comment().text)
    print(bulletin.update_project_bulletin().status_code)

    # projectnotes
    print(notes.update_project_note())

    # attachment
    attachment = AttachmentAPI()
    print(attachment.edit_attachment())

    # agenda
    agenda = AgendaAPI()
    print(agenda.get_project_agenda().json())
    print(agenda.add_agenda())


