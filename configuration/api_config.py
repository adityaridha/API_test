__author__      = "Muhammad Aditya Ridharrahman"
__version__     = "1.0"
__email__       = "aditya.ridharrahman@geekseat.com.au"
__status__      = "development"
__last_update__ = "10th Feb 2017"


class GetConfig():

    def __init__(self):
        print("Set up connection")

    @property
    def address(self):
        BASE_URL_V1 = "http://119.9.53.234:6969/api/v1/"
        return BASE_URL_V1


if __name__ == "__main__" :
    Config = GetConfig()
    print(Config.address)
