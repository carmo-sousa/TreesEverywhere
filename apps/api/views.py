from rest_framework import viewsets
from rest_framework.response import Response

from apps.api.serializers import PlantedTreeSerializer
from apps.tree.models import PlantedTree


class PlantedTreeViewSet(viewsets.ViewSet):
    queryset = PlantedTree.objects.all()

    def list(self, request):
        serializer = PlantedTreeSerializer(
            self.queryset.filter(user=request.user), many=True
        )

        return Response(serializer.data)
