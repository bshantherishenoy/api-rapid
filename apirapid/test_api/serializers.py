from rest_framework import serializers
from test_api.models import TestApi

class TestApiSerializer(serializers.ModelSerializer):
    class Meta:
        model=TestApi
        fields = '__all__'
        fields=("id","name","email","description","created_at")
        