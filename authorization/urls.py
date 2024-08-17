from django.urls import path

from .views import login, signup, logout, test_token

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("test/", test_token, name="test"),
]
