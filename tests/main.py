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
import glob


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


def download_from_page(folder_path, file_name, url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Initialize the ChromeDriver with the desired options
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)
    time.sleep(1)
    html1 = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html1, "html.parser")

    # Find the <video> element
    video_tag = soup.find("video")

    # If <video> tag is found, extract the modified 'src' attribute (URL)
    if video_tag:
        url2 = video_tag['src']
        print("Modified URL found:", url2)
        download_video(url2, folder_path, file_name)
    else:
        print("<video> tag not found.")
    print("working")


def download_category(folder_path, url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # Initialize the ChromeDriver with the desired options
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    html1 = driver.page_source
    driver.quit()
    # print(html1)
    soup = BeautifulSoup(html1, "html.parser")

    # Find all the elements containing the clip URLs (adjust the specific elements if needed)
    clip_elements = soup.find_all("a", class_="ScCoreLink-sc-16kq0mq-0 eYjhIv ScCoreLink-sc-bhsr9c-0 jYyMcQ tw-link")

    # Extract the URLs from the elements and store them in a list
    clip_urls = [clip["href"] for clip in clip_elements]
    for val in range(len(clip_urls)):
        clip_urls[val] = "https://www.twitch.tv"+clip_urls[val]
    # Print the list of URLs

    clipname = 0
    for file in clip_urls:
        clipname += 1
        name = "clip"+str(clipname)+".mp4"
        download_from_page(folder_path, name, str(file))


link = "https://www.twitch.tv/directory/game/Teamfight%20Tactics/clips?range=7d"
folder_path1="./clips"
download_category(folder_path1, link)
#
# print(clip_urls)
