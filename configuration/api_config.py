import requests

__author__      = "Muhammad Aditya Ridharrahman"
__version__     = "1.0"
__email__       = "aditya.ridharrahman@geekseat.com.au"
__status__      = "development"
__last_update__ = "10th Feb 2017"


class GetConfig():

    def __init__(self):
        pass

    @property
    def address(self):
        BASE_URL = "http://119.9.53.234:6969/api/v1/"
        return BASE_URL

    @property
    def post_header(self):
        HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}
        return HEADERS

    def api_request(self, service_url, data_body = "" , request_type = "POST"):
        if request_type == "POST" :
            request_result = requests.post(url = self.address + service_url, data = data_body, headers = self.post_header)
        if request_type == "PUT":
            request_result = requests.put(url = self.address + service_url, data = data_body, headers = self.post_header)
        if request_type == "GET":
            request_result = requests.get(url=self.address + service_url)

        return request_result


if __name__ == "__main__" :
    Config = GetConfig()
    print(Config.address)
