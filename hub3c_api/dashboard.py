import requests
from configuration import *

class DashboardAPI():

    config = GetConfig()
    user = config.user_data()

    def get_dashboard(self):
        get_dashboard = self.config.api_request(service_url="dashboard/514/753/0", request_type="GET")
        return get_dashboard

    def get_notifications(self):
        get_notif = self.config.api_request(service_url="users/{}/notifications?Top=10&Skip=0".format(
            self.user.system_user_id), request_type="GET")
        return get_notif


if __name__ == "__main__" :
    dashboard = DashboardAPI()
    # print(dashboard.get_dashboard().text)
    print(dashboard.get_notifications().text)







