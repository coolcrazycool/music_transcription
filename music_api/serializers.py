from rest_framework import serializers


class MelodySerializer(serializers.Serializer):
    user = serializers.CharField(max_length=100)
    melody = serializers.URLField(max_length=200, min_length=None, allow_blank=False)
    name = serializers.CharField(max_length=100)
    pdf = serializers.URLField(max_length=200, min_length=100, allow_blank=True)
