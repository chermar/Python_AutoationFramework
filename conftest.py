import pytest




def pytest_addoption(parser):
    parser.addoption("--browser",default="chrome",help=("Type browser Name"))
@pytest.fixture(scope="class")
def setup(request):
    from selenium import webdriver
    browser = request.config.getoption("--browser")
    if browser =="chrome".lower():
        driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
    if browser =="Firefox".lower():
        driver=webdriver.Firefox(executable_path="../drivers/geckodriver.exe")
    if browser =="Edge".lower():
        driver=webdriver.Edge(executable_path="../drivers/MicrosoftWebDriver.exe")
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()
    driver.quit()
