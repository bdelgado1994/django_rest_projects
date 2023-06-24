from .models import Project, Technology
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer, TechnologySerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer


class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TechnologySerializer
