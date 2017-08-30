from configuration import *

config = GetConfig()
user = config.user_data()

class BusinessAPI():

    def get_business(self):
        get_business = config.api_request(service_url="business/{}/{}/0".format(
            user.business_id, user.system_user_id), request_type="GET")
        return get_business

    def get_team_member(self):
        get_team_member = config.api_request(service_url="business/teammember/{}/{}/0".format(
            user.business_id, user.system_user_id), request_type="GET")
        return get_team_member

    def get_connected_business(self):
        get_connected_business = config.api_request(service_url="business/connectedbusiness/{}/{}/0".format(
            user.business_id, user.system_user_id), request_type="GET")
        return get_connected_business

    def get_pending_invitation(self):
        get_pending_inv = config.api_request(service_url="Dashboard/PendingInvitation/{}/{}/0".format(
            user.business_id, user.system_user_id), request_type="GET")
        return get_pending_inv

    def get_connect_request(self):
        get_connect_req = config.api_request(service_url="Dashboard/ConnectRequest/{}/{}/0".format(
            user.business_id, user.system_user_id), request_type="GET")
        return get_connect_req

    def invite_registered_business(self):
        pass

    def invite_new_business(self):
        pass

    def invite_registered_team_member(self):
        pass

    def invite_new_team_member(self):
        pass

    def resend_invitation(self):
        pass

    def accept_connection(self):
        pass

    def reject_connection(self):
        pass

if __name__ == "__main__" :
    business = BusinessAPI()
    print (business.get_business().text)
    # print(business.get_team_member().text)
    # print(business.get_connected_business().text)
    # print(business.get_pending_invitation().text)
    print(business.get_connect_request().text)






