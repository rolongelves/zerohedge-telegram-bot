
import requests
import feedparser
import time
from googletrans import Translator
import os

rss_url = 'https://cms.zerohedge.com/fullrss2.xml'
bot_token = os.getenv("7575556763:AAFhJ5C5WLgM0z6Uv9_wzXwbvJAwyjaW3Xc")
chat_id = os.getenv("6258554266")

translator = Translator()
last_title = ""

while True:
    feed = feedparser.parse(rss_url)
    if feed.entries:
        latest_entry = feed.entries[0]
        if latest_entry.title != last_title:
            title_es = translator.translate(latest_entry.title, src='en', dest='es').text
            description_es = translator.translate(latest_entry.summary, src='en', dest='es').text

            message = f"📰 {title_es}\n\n{description_es}\n\n{latest_entry.link}"
            send_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
            params = {'chat_id': chat_id, 'text': message}
            requests.get(send_url, params=params)
            last_title = latest_entry.title
    time.sleep(10)
