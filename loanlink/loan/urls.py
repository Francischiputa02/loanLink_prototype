from django.urls import path, include
from .views import LoanListView, ActiveLoanListViewset, PendingLoanListViewset,ClosedLoanListViewset, RejectedLoanListViewest, ApprovedLoanListView, CreditScoreSerializerViewset, LoanUpdateViewSet,LoanTransactionSerializerView
from .views import DisbursementOfFunds

urlpatterns = [

    path('loans/', LoanListView.as_view({'get': 'list', 'post': 'create'})),
    path('loans/<str:loan_id>', LoanListView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('loans/approve-loan/<uuid:pk>/', LoanUpdateViewSet.as_view({'post': 'update'})),

    path('loans/disbursement-of-funds/<uuid:loan_id>/', DisbursementOfFunds.as_view({'post': 'loan_disbursement'}), name='disbursement-of-funds'),

    path('loans/active/', ActiveLoanListViewset.as_view({'get': 'list'})),
    path('loans/<str:loan_id>', ActiveLoanListViewset.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy' })),

    path('loans/pending/', PendingLoanListViewset.as_view({'get': 'list'})),
    path('loans/<str:loan_id>', PendingLoanListViewset.as_view({'get': 'retrieve', 'put': 'update','delete': 'destroy'})),

    path('loans/closed/', ClosedLoanListViewset.as_view({'get': 'list'}), name='closeloans'),
    path('loans/<str:loan_id>', ClosedLoanListViewset.as_view({'get': 'retreive', 'put': 'update', 'delete': 'destroy'}), name='closeloans'),

    path('loans/rejected/', RejectedLoanListViewest.as_view({'get': 'list'}), name='rejectedloan'),
    path('loans/<str:loan_id>', RejectedLoanListViewest.as_view({'get': 'retreive', 'put': 'update', 'delete': 'destroy'}), name='rejectedloansid'),

    path('loans/approved/', ApprovedLoanListView.as_view({'get': 'list'}), name='approvedloans'),
    path('loans/<str:loan_id>', ApprovedLoanListView.as_view({'get': 'retreive', 'put': 'update', 'delete': 'destroy'}), name='approvedloansid'),

    path('creditscore/', CreditScoreSerializerViewset.as_view({'get': 'list', 'post': 'create'}), name='creditscore'), 
    path('creditscore/<str:client_id>/', CreditScoreSerializerViewset.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='creditscoreid'),

    path('transaction/',  LoanTransactionSerializerView.as_view({'get': 'list', 'post': 'create'})),
    path('transaction/<str:loan_id>', LoanTransactionSerializerView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='loan-transactions'),

]
