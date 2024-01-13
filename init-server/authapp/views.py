from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response 

from candidate.models import CandidateProfile
from company.models import CompanyProfile

from candidate.serializers import CandidateProfileSerializer 
from company.serializers import CompanyProfileSerializer
from .serializers import CustomUserSerializer


class GetUser(APIView):
    def get(self,request):
        user = request.user 
        if user.account_type == 'candidate':
            serializer = CandidateProfileSerializer(CandidateProfile.objects.get(user=user))
        elif user.account_type == 'company':
            serializer = CompanyProfileSerializer(CompanyProfile.objects.get(user=user))
        return Response({'user_info':serializer.data,'account_type':user.account_type})
        
