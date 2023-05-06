from abc import ABC

from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"


class FileUploadSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    file = serializers.FileField()

    def create(self, validated_data):
        file = validated_data.pop('file')


class QuerySerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    query = serializers.StringRelatedField()

    def post(self, validated_data):
        print(validated_data)
        query = validated_data.pop('query')
