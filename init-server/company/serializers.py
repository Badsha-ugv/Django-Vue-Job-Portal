from rest_framework import serializers
from .models import JobPost, CompanyProfile

class CompanyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = '__all__'
        read_only_fields = ['user'] 
        

class JobPostSerializer(serializers.ModelSerializer):
    company = CompanyProfileSerializer()

    class Meta:
        model = JobPost
        fields = '__all__'
