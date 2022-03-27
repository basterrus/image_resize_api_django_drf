from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from imageapp.models import ImageModel


class ImageSerializer(ModelSerializer):
    name = serializers.ReadOnlyField()
    width = serializers.ReadOnlyField()
    height = serializers.ReadOnlyField()
    parent_picture = serializers.ReadOnlyField()
    picture = serializers.ReadOnlyField()

    class Meta:
        model = ImageModel
        fields = '__all__'

