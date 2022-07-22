from selenium.webdriver.common.by import By
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

BROWSER_URL = 'http://browser:4444/wd/hub'
WP_URI = 'http://web:8000/'

class TestFoxes(StaticLiveServerTestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.browser = webdriver.Remote(command_executor=BROWSER_URL, options=options)
        
    def tearDown(self):
        self.browser.quit()

    def test_home_page_h1_text(self):
        self.browser.get(WP_URI)
        text_h1=self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertTrue('feliz cumpleaños' in text_h1.lower())

    def test_home_page_button_text(self):
        self.browser.get(WP_URI)
        button=self.browser.find_element(By.TAG_NAME, 'button')
        self.assertTrue(button.text=='Quiero mi regalo!')
        
    def test_home_page_button_text_after_click(self):
        self.browser.get(WP_URI)
        button=self.browser.find_element(By.TAG_NAME, 'button')
        button.click()
        button=self.browser.find_element(By.TAG_NAME, 'button')
        self.assertTrue(button.text=='Quiero más!')

    def test_home_page_img_after_click(self):
        self.browser.get(WP_URI)
        button=self.browser.find_element(By.TAG_NAME, 'button')
        button.click()
        img=self.browser.find_element(By.TAG_NAME, 'img')
        img_link=img.get_attribute('src')
        self.assertTrue('https://randomfox.ca/images/' in img_link)
        
    