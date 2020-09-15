from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin

from notification.models import Notification
from tweet.forms import TweetForm
from tweet.models import Tweet
from twitteruser.models import TwitterUser




class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        tweets = Tweet.objects.filter(
            user__in=request.user.following.all()).order_by('-date')
        user = request.user
        return render(request, "index.html", {"tweets": tweets, "user": user})

class TweetView(View):
    def get(self, request, tweet_id):
        html = 'tweet.html'
        tweet = Tweet.objects.get(id=tweet_id)
        return render(request, "tweet.html", {"tweet": tweet})


class AddTweet(View):
    html = 'generic_form.html'
    def get(self, request):
        form = TweetForm()
        return render(request, "generic_form.html", {"form": form})

    def post(self, request):
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweet = Tweet.objects.create(
            text=data.get('text'),
            user=request.user,
            )
            return HttpResponseRedirect(reverse("index"))
        return render(request, "generic_form.html", {"form": form})