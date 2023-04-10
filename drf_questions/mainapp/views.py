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

    def perform_create(self, serializer):
        serializer.validated_data['modified_by'] = self.request.user
        return super().perform_create(serializer)

    def perform_update(self, serializer):
        serializer.validated_data['modified_by'] = self.request.user
        return super().perform_update(serializer)

class PropertyViewSet(viewsets.ModelViewSet):
    '''View set of Property class serializer
    '''
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
