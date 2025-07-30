from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_google():
    chrome_options = Options()
    service = Service(ChromeDriverManager().install())
    google_driver = webdriver.Chrome(service=service, options=chrome_options)
    google_driver.implicitly_wait(10)
    google_driver.get("http://www.google.com/")
    assert google_driver.title.lower() == "google"
    google_driver.quit()

def test_facebook():
    chrome_options = Options()
    service = Service(ChromeDriverManager().install())
    fb_driver = webdriver.Chrome(service=service, options=chrome_options)
    fb_driver.implicitly_wait(20)
    fb_driver.get("http://www.facebook.com/")
    normalized_title = fb_driver.title.replace("–", "-")
    assert normalized_title == "Facebook - log in or sign up"
    fb_driver.quit()
