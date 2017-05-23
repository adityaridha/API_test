class Util():

    def print_response(self, response, verbose = False ) :
        print("\n### Status Code : {}".format(response.status_code))
        assert response.status_code == 200, print(response.text)
        if verbose == True :
            print("\n#### Header :")
            print(response.headers)
            print("\n#### Body :")
            print(response.text)




