from rest_framework import serializers
from .models import Manager, Intern

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['id', 'name', 'department', 'has_company_card']
        read_only_fields = ['has_company_card']

class InternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern
        fields = ['id', 'name', 'mentor', 'internship_end']
        # Assuming 'mentor' is a foreign key to the Manager model
        depth = 1  # This will include the related Manager details in the response

    def validate(self, attrs):
        # Custom validation can be added here if needed
        return attrs