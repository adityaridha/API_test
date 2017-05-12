class Credentials():

    marsha = {
        "email" : "marsha@freehub.com",
        "system_user_id" : 753,
        "business_id":514
    }

if __name__=="__main__":
    cred = Credentials()
    print(cred.marsha["email"])