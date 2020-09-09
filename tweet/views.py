from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required

from notification.models import Notification
from tweet.forms import TweetForm
from tweet.models import Tweet
from twitteruser.models import TwitterUser


@login_required
def index(request):
    tweets = Tweet.objects.filter(
        user__in=request.user.following.all()).order_by('-date')
    user = request.user
    return render(request, "index.html", {"tweets": tweets, "user": user})

def tweet_view(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    return render(request, "tweet.html", {"tweet": tweet})


@ login_required
def add_tweet_view(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweet = Tweet.objects.create(
                text=data.get('text'),
                user=request.user,
            )
            return HttpResponseRedirect(reverse("index"))

    form = TweetForm()
    return render(request, "generic_form.html", {"form": form})