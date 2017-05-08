import requests
from configuration import *

class AccountAPI():

    config = GetConfig()

    def login(self):
        data = '{"email":"marsha@freehub.com","password":"ZXasqw12","deviceToken":"0"}'
        post_login = self.config.api_request(service_url="Account/Login", data_body=data)
        return post_login

    def logout(self):
        data = '{"systemUserId":753}'
        post_logout = self.config.api_request(service_url="Account/Logout", data_body=data)
        return post_logout

    def account_list(self):
        data = '{"systemUserId":753}'
        post_account_list = self.config.api_request(service_url="Account/AccountList", data_body=data)
        return post_account_list

    def switch_account(self):
        data = '{"systemUserId":753,"deviceToken":"0"}'
        post_switch_account = self.config.api_request(service_url="Account/SwitchAccount", data_body=data)
        return post_switch_account

    def forgot_password(self):
        data = '{"emailAddress":"aditya.ridharrahman%40geekseat.com.au"}'
        post_forgot_password = self.config.api_request(service_url="Account/ForgotPassword", data_body=data)
        return post_forgot_password

if __name__ == "__main__" :
    account = AccountAPI()
    print (account.login)
