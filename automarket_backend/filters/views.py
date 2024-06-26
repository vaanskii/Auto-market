from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from cars.models import Car
from cars.serializers import CarSerializer
from .filters import CarFilter
from rest_framework.permissions import AllowAny

class CarList(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarFilter
    permission_classes = [AllowAny]
    authentication_classes = []

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('q', None)
        if search_query:
            queryset = queryset.filter(manufacturer__icontains=search_query) | \
                       queryset.filter(car_model__icontains=search_query)
        return queryset