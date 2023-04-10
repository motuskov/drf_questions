from rest_framework import viewsets

from .models import (
    Entity,
    Property,
)
from .serializers import (
    EntitySerializer,
    PropertySerializer,
)

class EntityViewSet(viewsets.ModelViewSet):
    '''View set of Entity class serializer
    '''
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

class PropertyViewSet(viewsets.ModelViewSet):
    '''View set of Property class serializer
    '''
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
