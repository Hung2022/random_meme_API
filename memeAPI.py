import requests
import random


class memeAPI:
    def __init__(self, subreddit=None, api_url='https://meme-api.com/gimme'):
        # self.nsfw = nsfw
        self.subreddit = subreddit
        self.api_url = api_url

    def get_meme_json(self, subreddit_name) -> dict:
        # response = requests.get(self.api_url)
        self.customSubreddit(subreddit_name)
        response = requests.get(self.api_url + '/' + self.subreddit)
        if response.status_code != 200:
            raise Exception
        return response.json()

    def customSubreddit(self, name) -> None:
        """
        set sub reddit name, use for endpoint of API
        :param name: name of a sub reddit
        :return:
        """
        if name is not None:
            self.subreddit = name
        else:
            self.set_randomSubreddit()
        return

    def set_randomSubreddit(self) -> None:
        """
        pick a random sub reddit from the subreddit_list
        :return:
        """
        subreddit_list = ['me_irl', 'dankmemes', 'memes']
        # subreddit_list = ['beatles']
        total_subreddit = len(subreddit_list) - 1
        subreddit_index = random.randint(0, total_subreddit)
        self.subreddit = subreddit_list[subreddit_index]
