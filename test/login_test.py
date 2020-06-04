from selenium import webdriver
import pytest
import allure
# import moment
import os
import sys
# sys.path.append(os.path.join(os.path.dirname(__file__),".","."))
from pages.homePage import HomePage
from pages.loginPage import LoginPage
from utils import utils as us
@pytest.mark.usefixtures("setup")
class TestLogin():
    # @pytest.fixture(scope="class")
    # def test_setup(self):
    #     global driver
    #     driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
    #     driver.implicitly_wait(5)
    #     driver.maximize_window()
    #     yield

        # driver.close()
        # driver.quit()
        # print("Test Completed")


    def test_login(self):
        self.driver.get(us.url)
        log=LoginPage(self.driver)
        log.enterUsername(us.username)
        log.enterPassword(us.password)
        log.Click_Submit()

        # driver.find_element_by_name("txtUsername").send_keys("Admin")
        # driver.find_element_by_name("txtPassword").send_keys("admin123")
        # driver.find_element_by_name("Submit").click()

    def test_logout(self):
        try:
            print("Logout Started")
            hp=HomePage(self.driver)
            hp.click_welcome()
            hp.click_Logout()
            # driver.find_element_by_css_selector("#welcome").click()
            # driver.find_element_by_link_text("Logout").click()
            x = self.driver.title
            assert  x == "abc"
        except:
            # currentTime=moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testname=us.whomai()
            scrrenshotName = testname
            allure.attach(self.driver.get_screenshot_as_png(),name=scrrenshotName,attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file("C:/Users/I_CRA/Python_Automation/AutoationFramework_1/screenshots/"+scrrenshotName+".png")
            raise
        print("Logout Ended ")



