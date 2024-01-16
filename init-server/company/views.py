from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 
from rest_framework.response import Response 


from .models import CompanyProfile
from .serializers import CompanyProfileSerializer

class UpdateCompanyProfile(ModelViewSet):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer

    def get_queryset(self):
        return CompanyProfile.objects.filter(user=self.request.user)
    
    def perform_create(self, serializers):
        user = self.request.user 
        serializers.save(user=user) 

    