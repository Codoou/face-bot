from app.common.config import settings
import tweepy

class Twitter:

    def __init__(self):
        """"""
        self.settings = settings
        self.auth = self._get_auth()
        self.api = self._get_api()

    def _get_auth(self):
        return tweepy.OAuth1UserHandler(
            self.settings["consumer_key"], self.settings["consumer_secret"],
            self.settings["access_token"], self.settings["access_token_secret"]
        )
    
    def _get_api(self):
        return tweepy.API(self.auth)

    def upload_image(self, file_name):
        """
        """
        response = self.api.media_upload(
            filename=file_name
        )

        return response.media_id

    def tweet(self, text, media_id):
        """"""

        self.api.update_status(
            status=text,
            media_ids=[media_id]
        )

    def get_my_mentions(self, mention_count):
        return self.api.mentions_timeline(
            count=mention_count
        )

    def get_most_recent_mention(self):
        return self.get_my_mentions(1)

    


