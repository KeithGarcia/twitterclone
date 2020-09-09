from django import forms

from tweet.models import Tweet

class TweetForm(forms.Form):
    text = forms.CharField(max_length=140)