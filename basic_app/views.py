from rest_framework import generics

from basic_app import models, serializers


# Create your views here.


class ListMy(generics.ListCreateAPIView):
    queryset = models.My.objects.all()
    serializer_class = serializers.MySerializers


class DetailMy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.My.objects.all()
    serializer_class = serializers.MySerializers
