from seleniumbase import BaseCase
import requests
import urllib.request

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class HomeTest(BaseCase):

    def test_home_page(self):
        # self.open("https://practice.automationbro.com")
        #
        # self.assert_title("Practice E-Commerce Site – Automation Bro")
        #
        # self.assert_element(".custom-logo-link")
        #
        # self.click("#get-started")
        #
        # get_started_url = self.get_current_url()
        # self.assert_equal(get_started_url, "https://practice.automationbro.com/#get-started")
        # self.assert_true("get-started" in get_started_url)
        #
        # self.assert_text("Think different. Make different.", "h1")
        # self.scroll_to_bottom()
        # self.assert_text("Copyright © 2020 Automation Bro", ".tg-site-footer-section-

        url = 'https://production.assets.clips.twitchcdn.net/H2fDQkazczMQVwF0zdYh_A/AT-cm%7CH2fDQkazczMQVwF0zdYh_A.mp4?sig=7eb2882a9ba48d5de9efede4bc5a7daa768f314b&token=%7B%22authorization%22%3A%7B%22forbidden%22%3Afalse%2C%22reason%22%3A%22%22%7D%2C%22clip_uri%22%3A%22https%3A%2F%2Fproduction.assets.clips.twitchcdn.net%2FH2fDQkazczMQVwF0zdYh_A%2FAT-cm%257CH2fDQkazczMQVwF0zdYh_A.mp4%22%2C%22device_id%22%3A%22u6ipmbtNYAQBwIlg4zoRMCvDPe6XccTH%22%2C%22expires%22%3A1689431781%2C%22user_id%22%3A%22%22%2C%22version%22%3A2%7D'
        urllib.request.urlretrieve(url, 'video_name.mp4')
