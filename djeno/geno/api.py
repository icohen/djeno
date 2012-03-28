from tastypie import fields
from tastypie.resources import ModelResource
from . import models

class PersonResource(ModelResource):
    children = fields.ToManyField('self', 'children', full=True)
    
    class Meta:
        queryset = models.Person.objects.filter(parents__isnull=True)
        include_resource_uri = False
        