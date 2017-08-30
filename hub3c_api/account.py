import csv
from configuration import *
from credentials import *
from faker import Factory

config = GetConfig()
user = config.user_data()

class AccountAPI():

    def login(self):
        data = {"email":user.email,"password":user.password,"deviceToken":"0"}
        post_login = config.api_request(service_url = "Account/Login", data_body = str(data))
        return post_login

    def logout(self):
        data = {"systemUserId":user.system_user_id}
        post_logout = config.api_request(service_url = "Account/Logout", data_body = str(data))
        return post_logout

    def register(self):

        fake = Factory.create()
        business = fake.company()
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = first_name + "." + last_name + "@mailinator.com"

        data = {"businessName":"Android {}".format(business),
                "emailAddress":"{}".format(email),
                "firstName":"{}".format(first_name),
                "lastName":"{}".format(last_name),
                "password":"ZXasqw12",
                "defaultTimezone":"SE Asia Standard Time",
                "title":'1'}

        registration_result = config.api_request(service_url="account/register", data_body = str(data))

        print(business)
        print(email)

        with open('registration.csv', 'a', newline='') as csvfile:
            registration_data = csv.writer(csvfile, delimiter=',', quotechar='"'
                                                                             '', quoting=csv.QUOTE_MINIMAL)
            registration_data.writerow([business,email])

        return registration_result

    def account_list(self):
        data = {"systemUserId": user.system_user_id}
        post_account_list = config.api_request(service_url = "Account/AccountList", data_body = str(data))
        return post_account_list

    def switch_account(self):
        data = {"systemUserId": user.system_user_id, "deviceToken": "0"}
        post_switch_account = config.api_request(service_url = "Account/SwitchAccount", data_body = str(data))
        return post_switch_account

    def forgot_password(self):
        data = {"emailAddress": user.email}
        post_forgot_password = config.api_request(service_url = "Account/ForgotPassword", data_body = str(data))
        return post_forgot_password

if __name__ == "__main__" :
    account = AccountAPI()
    print(account.login().text)
    print(account.switch_account().status_code)
    print(account.logout())
    print(account.account_list().json())
    print(account.forgot_password().json())
    # print(account.register().status_code)
