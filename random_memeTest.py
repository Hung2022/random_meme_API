from flask import Flask, render_template, Response
import os
from PIL import Image
from memeAPI import memeAPI


app = Flask(__name__)

@app.route("/")
def main_page():
    api = memeAPI()
    meme_json = api.get_meme_json()
    subreddit = 'me_irl'
    while meme_json['nsfw'] == 'true' and meme_json['subreddit'] != subreddit:
        meme_json = find_new_meme(api)
    image_url = meme_json['url']
    print(meme_json['nsfw'])
    print(meme_json['subreddit'])
    return render_template('display_image.html', image_url=image_url)


def get_img_content(url):
    img_file = url.split("/")[-1]
    return img_file
def find_new_meme(api):
    json = api.get_meme_json()
    return json