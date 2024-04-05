from rest_framework import serializers
from .models import ClientProfile, AgentProfile
from user.models import User



class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}
