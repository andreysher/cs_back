from rest_framework import serializers
from backend.models import List


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'