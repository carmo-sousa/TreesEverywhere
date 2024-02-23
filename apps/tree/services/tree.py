from apps.tree.models import Tree


class TreeService:
    def create(self, name: str, scientific_name: str):
        tree = Tree.objects.create(name=name, scientific_name=scientific_name)

        return tree
