from shop.models import *
from rest_framework import serializers


class DepartamentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departament
        fields = 'id', 'name', 'description',

