from rest_framework import serializers
from .models import Story


class StorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=200)
    desc = serializers.CharField(required=False, allow_blank=True, max_length=200)
    body = serializers.CharField(required=False, allow_blank=True, max_length=200)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Story.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get("title", instance.title)
        instance.desc = validated_data.get("desc", instance.title)
        instance.body = validated_data.get("body", instance.title)
        instance.save()
        return instance