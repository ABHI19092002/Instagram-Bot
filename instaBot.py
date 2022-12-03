import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

SIMILAR_ACC = "travellingthroughtheworld"
USERNAME = "letslaugh1100"
PASSWORD = "letslaugh9755"

Chrome_driver_path = Service("C:\Dev\chromedriver.exe")

class InstaFollower():
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(1)

        enter_username = self.driver.find_element(By.CSS_SELECTOR, ".f0n8F input")
        enter_username.send_keys(USERNAME)
        enter_password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        enter_password.send_keys(PASSWORD)
        time.sleep(2)

        click_log_in = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
        click_log_in.click()
        time.sleep(5)

        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(2)

        self.driver.find_element(By.CSS_SELECTOR, ".HoLwm").click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACC}")
        time.sleep(2)

        click_on_followers = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        click_on_followers.click()
        time.sleep(2)

        pop_up_scroll = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]')

        for scrolls in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pop_up_scroll)
            time.sleep(2)

    def follow(self):

        start_following = self.driver.find_elements(By.CSS_SELECTOR, ".Pkbci button")
        for follower in start_following:
            try:
                follower.click()
                time.sleep(1)

            # if already we follow someone, gives this error
            except ElementClickInterceptedException:
                cancel = self.driver.find_element(By.CSS_SELECTOR, ".HoLwm")
                cancel.click()
                time.sleep(1)


bot = InstaFollower(Chrome_driver_path)
bot.login()
time.sleep(3)
bot.find_followers()
time.sleep(2)
bot.follow()