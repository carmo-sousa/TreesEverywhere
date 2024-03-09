import logging

from django.contrib.auth import authenticate, login, logout
from django.http import Http404, HttpRequest
from django.shortcuts import redirect, render
from django.views import View

from apps.tree.forms import PlantTreeForm
from apps.tree.models import Location, PlantedTree
from apps.tree.services.plant_tree import PlantTreeService
from apps.tree.services.tree import TreeService

from . import forms


logger = logging.getLogger("root")


class LoginView(View):
    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return redirect(to="/admin", permanent=True)
            return redirect(to="index")

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
                return redirect(to="index", permanent=True)

        return Http404("Not found")


class LogoutView(View):
    def get(self, request: HttpRequest):
        logout(request)
        return redirect(to="login")


class DashboardView(View):
    def get(self, request):
        planted_trees = PlantedTree.objects.filter(user=request.user)
        context = {"planted_trees": planted_trees}
        return render(request, "dashboard/index.html", context=context)


class PlantView(View):
    def get(self, request: HttpRequest):
        accounts = request.user.account.all()
        context = {"accounts": accounts}
        return render(request, "dashboard/plant/create.html", context=context)

    def post(self, request: HttpRequest):
        form = PlantTreeForm(request.POST)
        plant_service = PlantTreeService()
        tree_service = TreeService()

        if form.is_valid():
            tree = tree_service.create(
                name=form.data.get("name"),
                scientific_name=form.data.get("scientific_name"),
            )

            location = Location.objects.create(
                latitude=form.data.get("latitude"),
                longitude=form.data.get("longitude"),
            )

            plant_service.plant_tree(
                tree=tree,
                location=location,
                user=request.user,
                account_id=form.data.get("account"),
            )

            return redirect(to="index")

        return redirect(to="plants-create")
