from seleniumbase import BaseCase
import requests
import urllib.request
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import ssl
import certifi


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


ssl_context = ssl.create_default_context(cafile=certifi.where())
url = 'https://production.assets.clips.twitchcdn.net/Zgt6WsyUWlT4oBAESU1zcQ/AT-cm%7CZgt6WsyUWlT4oBAESU1zcQ.mp4?sig=fcee0212df2f2c6172130c27f6c6e5cb10b1bfa6&token=%7B%22authorization%22%3A%7B%22forbidden%22%3Afalse%2C%22reason%22%3A%22%22%7D%2C%22clip_uri%22%3A%22https%3A%2F%2Fproduction.assets.clips.twitchcdn.net%2FZgt6WsyUWlT4oBAESU1zcQ%2FAT-cm%257CZgt6WsyUWlT4oBAESU1zcQ.mp4%22%2C%22device_id%22%3A%22Qhk5a80kmKlNpGdKovjzESfBEcd9OAUd%22%2C%22expires%22%3A1690651885%2C%22user_id%22%3A%22%22%2C%22version%22%3A2%7D'
folder_path = "./clips"
file_name = "video_name.mp4"

download_video(url, folder_path, file_name)

#
# driver = webdriver.PhantomJS("phantomjs-2.0.0-macosx/bin/phantomjs")
# driver.get("http://google.com")
#
# html1 = driver.page_source
# html2 = driver.execute_script


# url = 'https://production.assets.clips.twitchcdn.net/Zgt6WsyUWlT4oBAESU1zcQ/AT-cm%7CZgt6WsyUWlT4oBAESU1zcQ.mp4?sig=d335f8e30f69d75a6977990de014bf8e760aff3a&token=%7B%22authorization%22%3A%7B%22forbidden%22%3Afalse%2C%22reason%22%3A%22%22%7D%2C%22clip_uri%22%3A%22https%3A%2F%2Fproduction.assets.clips.twitchcdn.net%2FZgt6WsyUWlT4oBAESU1zcQ%2FAT-cm%257CZgt6WsyUWlT4oBAESU1zcQ.mp4%22%2C%22device_id%22%3A%22Qhk5a80kmKlNpGdKovjzESfBEcd9OAUd%22%2C%22expires%22%3A1690558774%2C%22user_id%22%3A%22%22%2C%22version%22%3A2%7D'
    # urllib.request.urlretrieve(url, 'video_name.mp4')
    # folder_path = "./clips"
    #
    # if not os.path.exists(folder_path):
    #     os.makedirs(folder_path)
    #
    # file_path = os.path.join(folder_path, "video_name.mp4")
    # urllib.request.urlretrieve(url, file_path)



