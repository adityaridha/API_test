# import os, sys
# from pathlib import Path
# root = Path(__file__).parents[1]   #get the root directory
# root_model = os.path.join(str(root),'API_test')
# sys.path.append(root_model)
# print(root_model)

import requests
from configuration import *
from helper import helper

__author__      = "Muhammad Aditya Ridharrahman"
__version__     = "1.0"
__email__       = "aditya.ridharrahman@geekseat.com.au"
__status__      = "development"
__last_update__ = "10th Feb 2017"


config      = GetConfig()
base_url    = config.address
helper      = helper.Helper()

timezone_response = requests.get(base_url+"Utility/TimeZoneList")
helper.print_response(timezone_response)

project_dashboard = requests.get(base_url+"Project/GetProjectListByProgress/514/753/0/InProgress")
helper.print_response(project_dashboard)