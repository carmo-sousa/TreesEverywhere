from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path("", login_required(views.DashboardView.as_view()), name="index"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path(
        "plants/create/",
        login_required(views.PlantView.as_view()),
        name="plants-create",
    ),
]
