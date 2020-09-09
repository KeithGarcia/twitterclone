from django.db import models

from tweet.models import Tweet
from twitteruser.models import TwitterUser


class Notification(models.Model):
    is_active = models.BooleanField(default=True)
    user_notification = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)