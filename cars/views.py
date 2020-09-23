from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from cars.models import Car
from cars.serializers import CarDetailSerializer, CarsListSerializer
from cars.permissions import IsOwnerOrReadOnly


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer


class CarsListView(generics.ListAPIView):
    serializer_class = CarsListSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser,)


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
