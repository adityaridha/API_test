import requests
from configuration import *

class BusinessAPI():

    config = GetConfig()

    def get_business(self):
        get_business = self.config.api_request(service_url="business/514/753/0", request_type="GET")
        return get_business

    def get_team_member(self):
        get_team_member = self.config.api_request(service_url="business/teammember/514/753/0", request_type="GET")
        return get_team_member

    def get_connected_business(self):
        get_connected_business = self.config.api_request(service_url="business/connectedbusiness/514/753/0", request_type="GET")
        return get_connected_business


if __name__ == "__main__" :
    business = BusinessAPI()
    print (business.get_business().text)
    print(business.get_team_member().text)
    print(business.get_connected_business().text)






