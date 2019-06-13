from shop.serializers import *
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class DepartamentViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Departament.objects.all()
    serializer_class = DepartamentSerializer

