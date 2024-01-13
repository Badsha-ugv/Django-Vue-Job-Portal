# import from django 
from django.shortcuts import render
from django.shortcuts import get_object_or_404

# import from django rest 
from rest_framework.response import Response 
from rest_framework.views import APIView 
from rest_framework.viewsets import ModelViewSet 
from rest_framework.permissions import IsAuthenticated

# import from app 
from authapp.models import CustomUser
from .models import Education, Experience, Award, CandidateProfile
from .serializers import EducationSerializer, AwardSerializer, ExperienceSerializer, CandidateProfileSerializer

class CandidateViewset(ModelViewSet):
    queryset = CandidateProfile.objects.all()
    serializer_class = CandidateProfileSerializer

    def get_queryset(self):
        return CandidateProfile.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

class EducationViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    
    def get_queryset(self):
        return Education.objects.filter(user=self.request.user) 
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user) 

class ExperienceViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

    def get_queryset(self):
        return Experience.objects.filter(user=self.request.user) 
    
    def perform_create(self,serializer):
        user = self.request.user 
        serializer.save(user=user) 

class AwardViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Award.objects.all()
    serializer_class = AwardSerializer

    def get_queryset(self):
        return Award.objects.filter(user=self.request.user) 
    
    def perform_create(self,serializer):
        user = self.request.user 
        serializer.save(user=user) 


