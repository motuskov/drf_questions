from rest_framework import serializers

from .models import (
    Entity,
    Property,
)

class EntitySerializer(serializers.ModelSerializer):
    '''Entity class serializer
    '''
    class Meta:
        model = Entity
        fields = ['value', 'properties']

class PropertySerializer(serializers.ModelSerializer):
    '''Property class serializer
    '''
    class Meta:
        model = Property
        fields = ['key', 'value']
