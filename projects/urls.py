from rest_framework import routers
from .api import ProjectViewSet, TechnologyViewSet

router = routers.DefaultRouter()
router.register("api/projects", ProjectViewSet, "projects")
router.register("api/technologies", TechnologyViewSet, "tecnologies",)
urlpatterns = router.urls
