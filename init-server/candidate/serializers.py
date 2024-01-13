from rest_framework import serializers
from .models import Education, Experience, Award, CandidateProfile, Project
from authapp.serializers import UserSerializer 

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id','user', 'title', 'company', 'location', 'duration']
        read_only_fields = ['user']

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id','user', 'exam', 'institute', 'passing_year', 'result']
        read_only_fields = ['user']
        
class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = ['id','user', 'topic', 'title', 'organization', 'date', 'link']
        read_only_fields = ['user']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project 
        fields = ['id','user','title','descreption','link']
        read_only_fields = ['user']

class CandidateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateProfile
        fields = ['id', 'user','first_name','last_name', 'profile_avatar', 'about', 'phone','email','address', 'resume', 'hard_skill', 'linkedin', 'github', 'portfolio', 'extra_activities', 'slug']

    
