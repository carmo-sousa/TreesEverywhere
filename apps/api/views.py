from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

from apps.api.serializers import PlantedTreeSerializer
from apps.tree.models import PlantedTree


class PlantedTreeViewSet(viewsets.ViewSet):
    queryset = PlantedTree.objects.all()
    serializer_class = PlantedTreeSerializer

    @extend_schema(
        request=PlantedTreeSerializer,
        responses={200: PlantedTreeSerializer(many=True)},
    )
    def list(self, request):
        serializer = self.serializer_class(
            self.queryset.filter(user=request.user), many=True
        )

        return Response(serializer.data)
