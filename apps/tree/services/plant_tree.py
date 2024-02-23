from typing import Any
from apps.tree.models import Location, PlantedTree, Tree


class PlantTreeService:
    def plant_tree(self, tree: Tree, location: Location, user: Any, account_id: int):
        return PlantedTree.objects.create(
            age=1,
            user=user,
            tree=tree,
            account_id=account_id,
            location=location,
        )

    def plant_trees(self, plants: list[tuple[Tree, Location, int]], user: Any):
        return PlantedTree.objects.bulk_create(
            [
                PlantedTree(
                    age=1,
                    user=user,
                    tree=item[0],
                    location=item[1],
                    account_id=item[2],
                )
                for item in plants
            ]
        )
