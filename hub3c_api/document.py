import requests
from configuration import *

class DocumentAPI():

    config = GetConfig()

    def download(self):
        get_document = self.config.api_request(service_url="dashboard/514/753/0", request_type="GET")
        return get_document


if __name__ == "__main__" :
    dashboard = DashboardAPI()
    print (dashboard.get_dashboard().text)







