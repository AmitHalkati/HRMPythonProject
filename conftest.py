from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# Base URL and credentials
BaseUrl = "https://opensource-demo.orangehrmlive.com/"
Username = "Admin"
Password = "admin123"


@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    """
    Set up the Selenium WebDriver before tests and tear down afterward.
    """
    # Initialize the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Maximize the browser window
    driver.maximize_window()

    # Open the Base URL
    driver.get(BaseUrl)

    # Attach the driver instance to the requesting class
    request.cls.driver = driver

    # Tear down the driver after all tests in the class are done
    yield
    driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today = datetime.now()
    report_dir = Path("hrmreports", today.strftime("%Y%m%d"))
    report_dir.mkdir(parents=True, exist_ok=True)  # Create the report directory if it doesn't exist

    # Set the HTML report path
    html_report_path = report_dir / f"Report_{today.strftime('%Y%m%d%H%M')}.html"
    print(f"Report will be saved at: {html_report_path}")  # Debugging line to check path

    # Ensure we pass a string path for htmlpath
    config.option.htmlpath = str(html_report_path)
    config.option.self_contained_html = True

def pytest_html_report_title(report):
    report.title = "HRM Test Report"

