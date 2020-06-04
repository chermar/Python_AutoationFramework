class HomePage():

    def __init__(self,driver):
        self.driver  = driver
        self.welcome_css="#welcome"
        self.logout_linkText="Logout"


    def click_welcome(self):
        self.driver.find_element_by_css_selector(self.welcome_css).click()

    def click_Logout(self):
        self. driver.find_element_by_link_text(self.logout_linkText).click()



