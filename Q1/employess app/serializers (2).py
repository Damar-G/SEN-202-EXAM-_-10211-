from rest_framework import serializers
from .models import Manager, Intern

class StaffBaseSerializers(serializers.ModelSerializers):
    role = serializers.SerializerMethodField()
    
    class Meta:
        fields = ['id', 'first_name', 'last_name', 'email', 'date_joined', 'role']
        
    def get_role(self, obj):
        return obj.get_role()