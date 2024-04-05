from .models import ClientProfile
from loan.models import Loan
from .models import ClientProfile
from user.models import User
from .serializers import Userserializer
from rest_framework import viewsets
from rest_framework.response import Response


class UserSerializer(viewsets.ViewSet):
	def list(self, request):
		queryset = User.objects.filter(is_client=True)
		serializer_class = UserSerializer
		serializer = serializer_class(queryset, many=True)
		return Response(serializer.data)
	
	def retrieve(self, request, pk=None):
		queryset = User.objects.get(pk=pk)
		serializer_class = UserSerializer
		serializer = serializer_class(queryset, data=request.data)
		return Response(serializer.data)


