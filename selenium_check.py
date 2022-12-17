from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tenacity import retry, stop_after_attempt


class selenium_checker:
    def __init__(self, code, username):
        self.code = code
        self.username = username

        self.driver = None
        self.status = None

    @retry(stop=stop_after_attempt(5))
    def run(self):
        self.create_driver()
        try:
            self.access_website()
            self.login()
            self.get_status()
            if self.status == '':
                raise Exception('error accessing status')
        except Exception as e:
            raise
        finally:
            self.driver.close()
        return self.check_text(self.status)

    def create_driver(self):
        self.driver = webdriver.Firefox()

    def close_driver(self):
        if self.driver is not None:
            self.driver.close()

    def login(self):
        while not self.check_loaded('record__reference'):
            time.sleep(1)
        self.driver.find_element(by=By.ID, value='record__reference').send_keys(self.code)
        self.driver.find_element(by=By.ID, value='skname__paxnameinternet').send_keys(self.username)
        self.driver.find_element(by=By.ID, value='btn_action').click()

    def get_status(self):
        while not self.check_loaded('status0Content'):
            time.sleep(1)
        time.sleep(5)
        status = self.driver.find_element(by=By.ID, value='status0Content')
        self.status = status.text
        return self.status

    def access_website(self, url='https://wtrweb.worldtracer.aero/WTRInternet/filedsp/w6.htm'):
        self.driver.get(url)

    def check_loaded(self, id_element):
        try:
            self.driver.find_element(by=By.ID, value=id_element)
            return True
        except Exception as e:
            return False

    def check_text(self, text):
        if text == 'TRACING CONTINUES. PLEASE CHECK BACK LATER':
            return False
        else:
            return True
