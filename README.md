#To execute :
pytest --alluredir allure_raw

#To execute specific category :
pytest -s -m 'category'

#To generate report :
allure generate allure_raw -o API_migration_report --clean

#To execute specific test case
pytest file_name.py::Class::method
pytest test_cases_account.py::TestAccount::test_register

