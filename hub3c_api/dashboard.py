import requests
from configuration import *

class DashboardAPI():

    config = GetConfig()

    def get_dashboard(self):
        get_dashboard = self.config.api_request(service_url="dashboard/514/753/0", request_type="GET")
        return get_dashboard



if __name__ == "__main__" :
    dashboard = DashboardAPI()
    print (dashboard.get_dashboard().text)







