from django.contrib.auth import authenticate, login
from django.http import Http404, HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from apps.tree.models import PlantedTree

from . import forms


class LoginView(View):
    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return redirect(to="/admin", permanent=True)
            return redirect(to="dashboard")

        return render(request, "login/index.html")

    def post(self, request: HttpRequest):
        form = forms.LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.data["username"],
                password=form.data["password"],
            )

            if user is not None:
                login(request, user)
                if request.user.is_superuser:
                    return redirect(to="/admin", permanent=True)
                return redirect(to="dashboard", permanent=True)

        return Http404("Not found")


class DashboardView(View):
    def get(self, request):
        planted_trees = PlantedTree.objects.filter(user=request.user)
        context = {"planted_trees": planted_trees}
        return render(request, "dashboard/index.html", context=context)
