
from django.contrib import admin
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from django.urls import path, include
from userProfile.urls import router

urlpatterns = [
    path('api/', include('user.urls')),
    path('api/', include('loan.urls')),
    path('api/clientview', include('userProfile.urls')),
    path('docs/', include_docs_urls(title='LoanlinkAPI')),
    path('schema/', get_schema_view(
        title='Loanlink API',
        description='Loan Management API',
        version='1.0',
    ), name='loanLink-schema'),
   # path('api/', include('userProfile.urls')),
    path('admin/', admin.site.urls),
]
