import sys
import os
from pytube import YouTube



def get_date(url):
    try:
        yt = YouTube(url)
        upload_date = yt.publish_date
        formatted_date = upload_date.strftime('%d/%m/%Y')
        return formatted_date
    except Exception as e:
        print("An error occurred:", e)

url = "https://www.youtube.com/live/24eE0HMjSXU?feature=shared"
date = get_date(url)

print(date)
