import pytest
from hrmpages.LoginPage import LoginPage
from conftest import Username, Password, BaseUrl

@pytest.mark.usefixtures("browser_setup")
class Test_login:
    driver = None

    def setup_class(self):
        self.driver.get(BaseUrl)
        self.login_page = LoginPage(self.driver)

    def test_valid_login2(self):
        self.login_page.login(Username, Password)
        assert 2 ==4

    def test_valid_login3(self):
        self.login_page.login(Username, Password)
        assert 2 ==2

    def teardown_class(self):
        self.driver.quit()
