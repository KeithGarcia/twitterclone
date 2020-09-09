from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from notification.models import Notification


@login_required
def notification_view(request):
    notifications = Notification.objects.filter(
        user_notification=request.user, is_active=True)
    for obj in notifications:
        obj.is_active = False
        obj.save()
    return render(request, "notification.html", {"notifications": notifications})