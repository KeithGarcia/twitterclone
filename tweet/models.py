from django.db import models
from django.utils import timezone

from twitteruser.models import TwitterUser


class Tweet(models.Model):
    text = models.CharField(max_length=140)
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)