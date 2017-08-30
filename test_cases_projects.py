import pytest
from helper import *
from hub3c_api import *

__author__      = "Muhammad Aditya Ridharrahman"
__version__     = "1.0"
__email__       = "aditya.ridharrahman@geekseat.com.au"
__status__      = "development"
__last_update__ = "10th Feb 2017"

print("######### Execute Account test cases #########")

util = Util()

class TestProjects():

    projects = ProjectsAPI()
    util = Util()

    @pytest.mark.get_only
    def test_get_project_list_new(self):
        result = self.projects.get_project_list_by_progress(state="New")
        self.util.print_response(result, verbose=True)

    @pytest.mark.get_only
    def test_get_project_list_inprogress(self):
        result = self.projects.get_project_list_by_progress(state="InProgress")
        self.util.print_response(result, verbose=True)

    @pytest.mark.get_only
    def test_get_project_list_onhold(self):
        result = self.projects.get_project_list_by_progress(state="OnHold")
        self.util.print_response(result, verbose=True)

    @pytest.mark.get_only
    def test_get_project_list_cancelled(self):
        result = self.projects.get_project_list_by_progress(state="Cancelled")
        self.util.print_response(result, verbose=True)

    @pytest.mark.get_only
    def test_get_project_list_complete(self):
        result = self.projects.get_project_list_by_progress(state="Complete")
        self.util.print_response(result, verbose=True)

    @pytest.mark.get_only
    def test_get_project_detail(self):
        result = self.projects.get_project_detail()
        self.util.print_response(result, verbose=True)

    @pytest.mark.get_only
    def test_get_project_notification(self):
        result = self.projects.get_project_notification()
        self.util.print_response(result, verbose=True)


class TestActivities():

    activities = ActivitiesAPI()
    util = Util()

    @pytest.mark.get_only
    def test_get_activities(self):
        result = self.activities.get_activities()
        self.util.print_response(result, verbose=True)

    @pytest.mark.skip(reason="Structure still not correct")
    def test_add_activity(self):
        pass


class TestTeammember():

    team_member = TeamMemberAPI()
    util = Util()

    @pytest.mark.get_only
    def test_get_team_member(self):
        result = self.team_member.get_team_member()
        self.util.print_response(result, verbose=True)

    @pytest.mark.skip(reason="not ready")
    def test_add_team_member(self):
        pass

    @pytest.mark.skip(reason="not ready")
    def test_delete_team_member(self):
        pass

    def test_update_team_member(self):
        pass


class TestBulletin():
    bulletin = BulletinAPI()
    util = Util()

    @pytest.mark.get_only
    def test_get_bulletin(self):
        result = self.bulletin.get_project_bulletin()
        self.util.print_response(result, verbose=True)

    @pytest.mark.get_only
    def test_get_bulletin_comment(self):
        result = self.bulletin.get_project_bulletin_comment()
        self.util.print_response(result, verbose=True)

    def test_like_unlike_bulletin(self):
        result = self.bulletin.like_unlike_bulletin()
        self.util.print_response(result, verbose=True)

    def test_create_bulletin(self):
        result = self.bulletin.create_bulletin()
        self.util.print_response(result, verbose=True)

    def test_create_bulletin_comment(self):
        result = self.bulletin.create_bulletin_comment()
        self.util.print_response(result, verbose=True)

    def test_update_bulletin(self):
        result = self.bulletin.update_project_bulletin()
        self.util.print_response(result, verbose=True)

    @pytest.mark.skip(reason="not ready")
    def test_delete_comment(self):
        pass


class TestNotes():

    notes = NotesAPI()
    util =  Util()

    @pytest.mark.get_only
    def test_get_notes(self):
        result = self.notes.get_project_notes()
        self.util.print_response(result, verbose=True)

    def test_add_notes(self):
        result = self.notes.add_project_note()
        self.util.print_response(result, verbose=True)

    def test_update_notes(self):
        result = self.notes.update_project_note()
        self.util.print_response(result, verbose=True)


class TestAttachment():

    attachment = AttachmentAPI()

    @pytest.mark.get_only
    def test_get_attachment(self):
        result = self.attachment.get_project_attachment()
        util.print_response(result, verbose=True)

    def test_edit_attachment(self):
        result = self.attachment.edit_attachment()
        util.print_response(result, verbose=True)

    @pytest.mark.skip(reason="not ready")
    def test_download_attachment(self):
        pass

    @pytest.mark.skip(reason="not ready")
    def test_upload_attachment(self):
        pass

    @pytest.mark.skip(reason="not ready")
    def test_delete_attachment(self):
        pass


class TestAgenda():

    agenda = AgendaAPI()

    @pytest.mark.get_only
    def test_get_project_agenda(self):
        result = self.agenda.get_project_agenda()
        util.print_response(result, verbose=True)

    def test_add_project_agenda(self):
        result = self.agenda.add_agenda()
        util.print_response(result, verbose=True)

    def test_edit_project_agenda(self):
        result = self.agenda.edit_agenda()
        util.print_response(result, verbose=True)


class TestTimesheet():

    timesheet = TimesheetAPI()

    @pytest.mark.get_only
    def test_get_project_timesheet(self):
        result = self.timesheet.get_project_timesheet()
        util.print_response(result, verbose=True)

    def test_get_activity_timesheet(self):
        pass

    def test_get_team_member_activity(self):
        pass

    def test_add_time_sheet(self):
        pass

    def test_edit_timesheet(self):
        pass

