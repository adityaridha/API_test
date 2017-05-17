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

if __name__=="__main__":
    cred = Credentials()
    print(cred.marsha["email"])