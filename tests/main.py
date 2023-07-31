from seleniumbase import BaseCase
import requests
import urllib.request
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import ssl
import certifi
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup


def download_video(url, folder_path, file_name):
    try:
        # Create the folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Build the full file path
        file_path = os.path.join(folder_path, file_name)

        # Create the SSL context using certifi
        ssl_context = ssl.create_default_context(cafile=certifi.where())

        # Download the video from the URL and save it to the specified file path
        with urllib.request.urlopen(url, context=ssl_context) as response:
            with open(file_path, 'wb') as f:
                f.write(response.read())

        print("Video downloaded successfully.")
    except Exception as e:
        print(f"Error downloading video: {e}")


# download_video(url, folder_path, file_name)
# Set up ChromeOptions to run in headless mode
folder_path = "./clips"
file_name = "video_name21321412.mp4"
chrome_options = Options()
chrome_options.add_argument("--headless")

# Initialize the ChromeDriver with the desired options
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.twitch.tv/k3soju/clip/BetterEnthusiasticShieldKeepo-zJRaVPigEARJTXNx")

html1 = driver.page_source
driver.quit()
soup = BeautifulSoup(html1, "html.parser")

# Find the <video> element
video_tag = soup.find("video")

# If <video> tag is found, extract the modified 'src' attribute (URL)
if video_tag:
    url = video_tag['src']
    print("Modified URL found:", url)
    download_video(url, folder_path, file_name)
else:
    print("<video> tag not found.")
print("working")



