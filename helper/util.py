class Util():

    def print_response(self, response, verbose = False ):

        if verbose == True :
            print("\n#### Header :")
            print(response.headers)
            print("\n#### Body :")
            print(response.text)

        print("\n### Status Code : {}".format(response.status_code))


