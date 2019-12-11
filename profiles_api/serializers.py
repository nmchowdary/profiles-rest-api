from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """ serializes a name filed for testing our APIViews"""
    name = serializers.CharField(max_length=10)
