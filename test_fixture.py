import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
driver = None

@pytest.fixture(scope="module")
def init_driver():
    global driver
    print("--------------------------------------------------------")
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://www.google.com/")

    yield
    print("--------------------------------------------------------")
    driver.quit()

def test_google(init_driver):
    assert driver.title == "Google"

def test_google_url(init_driver):
    assert driver.current_url == "https://www.google.com/"