from django.contrib.auth import get_user_model
from django.test import TestCase
from apps.tree.models import Location, PlantedTree, Tree
from apps.user.models import Account
from .services.plant_tree import PlantTreeService


User = get_user_model()


class PlantTreeServiceTestCase(TestCase):
    def setUp(self):
        self.service = PlantTreeService()
        self.user = User.objects.create(username="test_user")
        self.account = Account.objects.create(name="Account 1")
        self.user.account.add(self.account)
        self.user.save()
        self.location = Location.objects.create(latitude=123.456, longitude=789.123)
        self.tree = Tree.objects.create(
            name="Tree test", scientific_name="Tree test scientific"
        )

    def test_plant_tree(self):
        planted_tree = self.service.plant_tree(
            self.tree, self.location, self.user, account_id=1
        )
        self.assertIsInstance(planted_tree, PlantedTree)
        self.assertEqual(planted_tree.age, 1)
        self.assertEqual(planted_tree.user, self.user)
        self.assertEqual(planted_tree.tree, self.tree)
        self.assertEqual(planted_tree.location, self.location)
        self.assertEqual(planted_tree.account_id, 1)
