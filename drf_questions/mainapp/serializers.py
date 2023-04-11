from rest_framework import serializers

from .models import (
    Entity,
    Property,
)

class AliasIntegerField(serializers.IntegerField):
    '''Integer field with possibility of creating a field name alias 
    '''
    def __init__(self, field_name_alias: str=None, **kwargs):
        self.field_name_alias = field_name_alias
        super().__init__(**kwargs)

    def get_value(self, dictionary):
        try:
            dictionary[self.field_name] = dictionary.pop(self.field_name_alias)
        except KeyError:
            pass
        return super().get_value(dictionary)

class PropertySerializer(serializers.ModelSerializer):
    '''Property class serializer
    '''
    class Meta:
        model = Property
        fields = ['key', 'value']

class EntitySerializer(serializers.ModelSerializer):
    '''Entity class serializer
    '''
    value = AliasIntegerField(field_name_alias='data[value]')
    properties = serializers.SerializerMethodField(read_only=True)

    def get_properties(self, obj: Entity) -> dict:
        '''Returns entity's properties as a dictionary
        '''
        properties = obj.properties.all()
        return {property.key: property.value for property in properties}

    class Meta:
        model = Entity
        fields = ['value', 'properties']
