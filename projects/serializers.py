from rest_framework import serializers
from .models import Project, Technology


class ProjectSerializer(serializers.ModelSerializer):
    technology_name = serializers.CharField(source="technology.name", read_only=True)
    class Meta:
        model = Project
        fields = ("id", "title", "description", "technology_name", "created_at")
        read_only_fields = ["created_at"]


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ("id", "name", "created_at")
        read_only_fields = ["created_at"]
