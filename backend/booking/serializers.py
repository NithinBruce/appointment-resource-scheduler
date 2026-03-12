from rest_framework import serializers
from .models import Resource, Appointment


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Appointment
        fields = '__all__'
    def validate(self, data):
        resource = data["resource"]
        start = data["start_time"]
        end = data["end_time"]

        if start >= end:
            raise serializers.ValidationError("End time must be after start time.")

        # If updating an existing appointment, exclude itself
        appointment_id = self.instance.id if self.instance else None

        conflict = Appointment.objects.filter(
            resource=resource,
            start_time__lt=end,
            end_time__gt=start,
            status="booked",
        ).exclude(id=appointment_id).exists()

        if conflict:
            raise serializers.ValidationError(
                "This resource is already booked for the selected time."
            )

        return data