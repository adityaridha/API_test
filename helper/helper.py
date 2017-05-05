class Helper():

    def print_response(self,response):
        print("\n#### Header :")
        print(response.headers)
        print("\n#### Body :")
        print(response.json())
        print("\n### Status Code :")
        print(response.status_code)