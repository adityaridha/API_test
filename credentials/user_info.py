import sqlite3

class Credentials():

    marsha = {
        "email" : "marsha@freehub.com",
        "password" : "ZXasqw12",
        "system_user_id" : 753,
        "business_id":514,
        "project_sample":"Web project"
    }


    karin = {
        "email" : "karin@freehub.com",
        "password" : "ZXasqw12",
        "system_user_id" : 754,
        "business_id":515,
        "project_sample":"Web project"
    }

    fitri_live = {
        "email": "fitri.sample@dev.com",
        "password": "ZXasqw12",
        "system_user_id": 125,
        "business_id": 62,
        "project_sample": "Mobile hub3c"
    }


class Marsha():

    def __init__(self):
        self.email = "marsha@freehub.com"
        self.password = "ZXasqw12"
        self.system_user_id = 753
        self.business_id = 514

class Karin():

    def __init__(self):
        self.email = "karin@freehub.com"
        self.password = "ZXasqw12"
        self.system_user_id = 754
        self.business_id = 515


if __name__=="__main__":
    user = Karin()

    print(user.email)
    print(user.system_user_id)
    print(user.password)