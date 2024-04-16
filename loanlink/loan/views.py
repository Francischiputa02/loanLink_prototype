from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Loan, CreditScore
from .serializers import LoanSerializer, CreditScoreSerializer, LoanUpdateSerializer
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# List all the loans
class LoanListView(viewsets.ViewSet):
    def list(self, request):
        queryset = Loan.objects.all()
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, loan_id=None):

        def retrieve(self, request, pk=None):
            queryset = Loan.objects.filter(loan__loan_id=loan_id)
            serializer_class = LoanSerializer
            serializer = serializer_class(queryset)
            return Response(serializer.data)

    def update(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Individual loan details
class LoanDetailView(viewsets.ViewSet):
    def list(self, request):
        queryset = Loan.objects.all()
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# Listing all activaate loans
class ActiveLoanListViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Loan.objects.filter(status='active')
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# List all closed loans
class ClosedLoanListViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Loan.objects.filter(status='closed')
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrive(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        queryset = Loan.objects.get(pk=pk)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# List all pending loans
class PendingLoanListViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Loan.objects.filter(status='pending')
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrive(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# List all rejected loans
class RejectedLoanListViewest(viewsets.ViewSet):
    def list(self, request):
        queryset = Loan.objects.filter(status='rejected')
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrive(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# List all approved loans
class ApprovedLoanListView(viewsets.ViewSet):
    def list(self, request):
        queryset = Loan.objects.filter(status='approved')
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrive(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Loan.objects.get(pk=pk)
        serializer_class = LoanSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Credit score list 
class CreditScoreSerializerViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = CreditScore.objects.all()
        serializer_class = CreditScoreSerializer
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def create(self, request):
        serializer_class = CreditScoreSerializer
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, client_id=None):
        queryset = CreditScore.objects.filter(client__id=client_id).first()
        serializer_class = CreditScoreSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = CreditScoreSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, loan_id=None):
        queryset = Loan.objects.filter(loan__loan_id=loan_id)
        serializer_class = CreditScoreSerializer
        serializer = serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoanUpdateViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanUpdateSerializer
    def approve_loan(self, request, loan_id=None):
        try:
            loan = Loan.objects.get(loan__loan_id=loan_id)
            loan.status = 'approved'
            loan.save()
            return Response({'status': 'Loan approved successfully'})
        except Loan.DoesNotExist:
            return Response({'status': 'Loan not found'}, status=404)

