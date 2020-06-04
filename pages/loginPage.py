class LoginPage():

    def __init__(self,driver):
        self.driver = driver

        self.userName_textbox_name="txtUsername"
        self.password_textbox_name = "txtPassword"
        self.login_button_name="Submit"

    def enterUsername(self,userName):
        self.driver.find_element_by_name(self.userName_textbox_name).clear()
        self.driver.find_element_by_name(self.userName_textbox_name).send_keys(userName)


    def enterPassword(self,Password):
        self.driver.find_element_by_name(self.password_textbox_name).clear()
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(Password)


    def Click_Submit(self):
        self. driver.find_element_by_name(self.login_button_name).click()


