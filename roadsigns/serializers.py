from rest_framework import serializers
from .models import Categories, Documents


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'


class DocumentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Documents
        fields = '__all__'