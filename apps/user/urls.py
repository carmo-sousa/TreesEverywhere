from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("dashboard/", login_required(views.DashboardView.as_view()), name="dashboard"),
]
