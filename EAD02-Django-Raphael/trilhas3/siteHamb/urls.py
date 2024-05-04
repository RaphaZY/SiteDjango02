from django.urls import path

from siteHamb.views import *

urlpatterns = [
    path("", index, name="index"),
    path("login/", login, name="login.html")
]