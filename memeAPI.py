import requests
import random
class memeAPI:
    def __init__(self, subreddit=None, api_url='https://meme-api.com/gimme'):
        #self.nsfw = nsfw
        self.subreddit = subreddit
        self.api_url = api_url

    def get_meme_json(self) -> dict:
        #response = requests.get(self.api_url)
        self.customSubreddit()
        response = requests.get(self.api_url + '/' + self.subreddit)
        if response.status_code != 200:
            raise Exception
        return response.json()

    def customSubreddit(self) -> None:
        """
        set sub reddit name, use for endpoint of API
        :return:
        """
        if self.subreddit is None:
            self.set_randomSubreddit()
            return
        self.subreddit = 'wholesomememes'

    def set_randomSubreddit(self) -> None:
        """
        pick a random sub reddit from the subreddit_list
        :return:
        """
        subreddit_list = ['me_irl', 'dankmemes', 'memes']
        total_subreddit = len(subreddit_list) - 1
        subreddit_index = random.randint(0, total_subreddit)
        self.subreddit = subreddit_list[subreddit_index]



