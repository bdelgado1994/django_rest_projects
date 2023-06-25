from rest_framework import routers
from .api import ProjectViewSet, TechnologyViewSet
from rest_framework.documentation import include_docs_urls
from django.urls import include, path

router = routers.DefaultRouter()
router.register("api/projects", ProjectViewSet, "projects")
router.register(
    "api/technologies",
    TechnologyViewSet,
    "tecnologies",
)
urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("docs/", include_docs_urls(title="Tasks API")),
]
