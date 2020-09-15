from django.shortcuts import render, HttpResponseRedirect, reverse
# from django.views.generic.base import View

from twitteruser.models import TwitterUser
from tweet.models import Tweet


def user_view(request, username):
    user = TwitterUser.objects.get(username=username)
    tweets = Tweet.objects.filter(user=user.id)
    if request.user.username:
        is_following = user in request.user.following.all()
    else:
        is_following = False
    following = len(user.following.all())
    return render(request, "user.html", {"user": user, "tweets": tweets, "is_following": is_following, "following": following})

# class UserView(View):
#     def get(self, request, username):
        
#         user = TwitterUser.objects.get(username=username)
#         tweets = Tweet.objects.filter(user=user.id)
#         if request.user.username:
#             is_following = user in request.user.following.all()
#         else:
#             is_following = False
#         following = len(user.following.all())
#         return render(request, "user.html", {"user": user, "tweets": tweets, "is_following": is_following, "following": following})


def follow(request, username):
    user = TwitterUser.objects.get(username=username)
    request.user.following.add(user)
    return HttpResponseRedirect(reverse("user", args=[username]))


def unfollow(request, username):
    user = TwitterUser.objects.get(username=username)
    request.user.following.remove(user)
    return HttpResponseRedirect(reverse("user", args=[username]))