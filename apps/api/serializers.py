from rest_framework import serializers

from apps.tree.models import Location, PlantedTree, Tree
from apps.user.models import Account


class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        exclude = ["id"]


class PlantedTreeSerializer(serializers.ModelSerializer):
    tree = TreeSerializer(read_only=True)
    account = AccountSerializer(read_only=True)
    location = LocationSerializer(read_only=True)

    class Meta:
        model = PlantedTree
        fields = "__all__"
