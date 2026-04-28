# Playwright_demo

Auto tests for Swag Labs (https://saucedemo.com)


Add Poetry
Add Results
 - Add allure titles for tests

Allure instalation is required to look at reports

(First run) To run all tests with reports
> pytest --alluredir=reports/allure_report

Run all tests slow
> pytest --headed --slowmo=<sec>

Show reports
> allure serve reports/allure_report

Clear reports
> rm -rf reports/allure_report

Open venv
> source venv/Scripts/activate

Close venv
> deactivate

