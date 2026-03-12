from rest_framework import viewsets
from .models import Resource, Appointment
from rest_framework.permissions import IsAuthenticated
from .serializers import ResourceSerializer, AppointmentSerializer


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer 
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)