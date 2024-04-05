from rest_framework import serializers
from .models import Loan, CreditScore
from userProfile.models import ClientProfile,AgentProfile



class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfile
        fields = '__all__'


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentProfile
        fields = '__all__'


class LoanSerializer(serializers.ModelSerializer):
    #client = ClientSerializer()
    
    class Meta:
        model = Loan
        fields = '__all__'


class CreditScoreSerializer(serializers. ModelSerializer):
    class Meta:
        model = CreditScore
        fields = '__all__'



