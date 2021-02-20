from selenium import webdriver
import time

PROMISED_DOWN = 150
PROMISED_UP = 10

driver_path = '/home/nawodya_Dark/Third_party/chrome_Driver/chromedriver'


class InternetSpeedTwitterBot:
    def __init__(self, down, up):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.down = down
        self.up = up
        self.MESSAGE = 'Hey Internet provider, This is come from My Twitter BOT'
    
    def get_internet_speed(self):
        self.driver.get('https://fast.com/')
        time.sleep(2)
        speed = self.driver.find_element_by_id('speed-value')
        print(speed.text)


    def tweet_at_provider(self):                
        self.driver.get('https://www.twitter.com')

        log_in = self.driver.find_element_by_link_text('Log in')
        log_in.click()

        time.sleep(3)
        user_name = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        user_name.send_keys('+94779802204')

        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password.send_keys('PASSWORD')

        final_login = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
        final_login.click()

        time.sleep(4)
        tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div/span')
        tweet.send_keys(self.MESSAGE)

        time.sleep(2)
        tweet_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span')
        tweet_btn.click()



bot = InternetSpeedTwitterBot(PROMISED_DOWN, PROMISED_UP)
bot.get_internet_speed()
bot.tweet_at_provider()
