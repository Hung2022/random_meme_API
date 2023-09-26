import requests
import random
class memeAPI:
    def __init__(self, subreddit=None, api_url='https://meme-api.com/gimme'):
        #self.nsfw = nsfw
        self.subreddit = subreddit
        self.api_url = api_url

    def get_meme_json(self):
        #response = requests.get(self.api_url)
        self.customSubreddit()
        response = requests.get(self.api_url + '/' + self.subreddit)
        if response.status_code != 200:
            raise Exception
        #response = self.customSubreddit(response)
        return response.json()

    def customSubreddit(self):
        if self.subreddit == None:
            self.set_randomSubreddit()
            return
            # subreddit_name = 'dankmemes'
            # return subreddit_name
        params = 'wholesomememes'
        return params

    def set_randomSubreddit(self):
        subreddit_list = ['me_irl', 'dankmemes', 'memes']
        total_subreddit = len(subreddit_list) - 1
        subreddit_index = random.randint(0, total_subreddit)
        self.subreddit = subreddit_list[subreddit_index]



