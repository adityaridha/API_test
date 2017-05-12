class Credentials():

    marsha = {
        "email" : "marsha@freehub.com",
        "password" : "ZXasqw12",
        "system_user_id" : 753,
        "business_id":514
    }

if __name__=="__main__":
    cred = Credentials()
    print(cred.marsha["email"])