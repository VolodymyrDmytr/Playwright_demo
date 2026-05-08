# Playwright_demo

Auto tests for Swag Labs (https://saucedemo.com)

Allure instalation is required to look at reports

(First run) To run all tests with reports
> poetry run pytest --alluredir=reports/allure_report

Run all tests slow
> poetry run pytest --headed --slowmo=<sec>

Show reports
> poetry run allure serve reports/allure_report

Clear reports
> rm -rf reports/allure_report


**ADD**
 - URL tests