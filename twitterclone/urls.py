"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tweet import views
from authentication.views import *
from twitteruser.views import *
from notification.views import *

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('u/<str:username>/unfollow/', unfollow),
    path('u/<str:username>/', user_view, name="user"),
    # path('altuserview/<int:username>', UserView.as_view()),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', logout_view),
    path('signup/', signup_view, name="signup"),
    path('addtweet/',views.AddTweet.as_view()),
    path('tweet/<int:tweet_id>/', views.TweetView.as_view()),
    path('notification/', notification_view),
    path('u/<str:username>/follow/', follow),
    path('admin/', admin.site.urls),
]
