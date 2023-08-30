from django.urls import path
from auth_app.views import *

urlpatterns = [
    path('signup/', register, name="register"),
    path('signin/', login, name="login"),
    path('signout/', logout, name="logout"),
]