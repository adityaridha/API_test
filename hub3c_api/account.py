import requests
from configuration import *
from credentials import *

class AccountAPI():

    config = GetConfig()
    user = Credentials()

    email = user.marsha["email"]
    password = user.marsha["password"]
    system_user_id = user.marsha["system_user_id"]

    def login(self):
        data = {"email":self.email,"password":self.password,"deviceToken":"0"}
        post_login = self.config.api_request(service_url = "Account/Login", data_body = str(data))
        return post_login

    def logout(self):
        data = {"systemUserId":self.system_user_id}
        post_logout = self.config.api_request(service_url = "Account/Logout", data_body = str(data))
        return post_logout

    def account_list(self):
        data = {"systemUserId": self.system_user_id}
        post_account_list = self.config.api_request(service_url = "Account/AccountList", data_body = str(data))
        return post_account_list

    def switch_account(self):
        data = {"systemUserId": self.system_user_id, "deviceToken": "0"}
        post_switch_account = self.config.api_request(service_url = "Account/SwitchAccount", data_body = str(data))
        return post_switch_account

    def forgot_password(self):
        data = {"emailAddress":self.email}
        post_forgot_password = self.config.api_request(service_url = "Account/ForgotPassword", data_body = str(data))
        return post_forgot_password

if __name__ == "__main__" :
    account = AccountAPI()
    print(account.login().text)
    print(account.logout())
    print(account.account_list().json())
    print(account.switch_account().status_code)
    print(account.forgot_password().json())
