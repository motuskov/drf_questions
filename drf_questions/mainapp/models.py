from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    '''Property class
    '''
    key = models.CharField(
        max_length=100,
        help_text='Key of the property'
    )
    value = models.CharField(
        max_length=100,
        help_text='Value of the property'
    )

class Entity(models.Model):
    '''Entity class
    '''
    modified_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text='User that modified the entity'
    )
    value = models.IntegerField(
        help_text='Value of the entity'
    )
    properties = models.ManyToManyField(
        Property,
        help_text='Properties of the entity'
    )
