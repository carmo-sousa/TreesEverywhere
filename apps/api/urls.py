from rest_framework import routers

from apps.api.views import PlantedTreeViewSet

router = routers.SimpleRouter()
router.register(r"planted-trees", PlantedTreeViewSet)

urlpatterns = router.urls
