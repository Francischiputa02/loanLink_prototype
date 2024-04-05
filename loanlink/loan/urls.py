from django.urls import path, include
from .views import LoanListView, ActiveLoanListViewset, PendingLoanListViewset,ClosedLoanListViewset, RejectedLoanListViewest, ApprovedLoanListView, CreditScoreSerializerViewset


urlpatterns = [

    path('loans/', LoanListView.as_view({'get': 'list', 'post': 'create'})),
    path('loans/<int:pk>', LoanListView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('loans/active/', ActiveLoanListViewset.as_view({'get': 'list'})),
    path('loans/<int:pk>', ActiveLoanListViewset.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy' })),

    path('loans/pending', PendingLoanListViewset.as_view({'get': 'list'})),
    path('loans/<int:pk>', PendingLoanListViewset.as_view({'get': 'retrieve', 'put': 'update','delete': 'destroy'})),

    path('loans/closed', ClosedLoanListViewset.as_view({'get': 'list'}), name='closeloans'),
    path('loans/<int:pk>', ClosedLoanListViewset.as_view({'get': 'retreive', 'put': 'update', 'delete': 'destroy'}), name='closeloans'),

    path('loans/rejected', RejectedLoanListViewest.as_view({'get': 'list'}), name='rejectedloan'),
    path('loans/<int:pk>', RejectedLoanListViewest.as_view({'get': 'retreive', 'put': 'update', 'delete': 'destroy'}), name='rejectedloansid'),

    path('loans/approved', ApprovedLoanListView.as_view({'get': 'list'}), name='approvedloans'),
    path('loans/<int:pk>', ApprovedLoanListView.as_view({'get': 'retreive', 'put': 'update', 'delete': 'destroy'}), name='approvedloansid'),

    path('creditscore/', CreditScoreSerializerViewset.as_view({'get': 'list', 'post': 'create'}), name='creditscore'),
    path('creditscor/<int:pk>/', CreditScoreSerializerViewset.as_view({'get': 'retreive', 'put': 'update', 'delete': 'destroy'}), name='creditscoreid'),

]
