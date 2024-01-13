from rest_framework import serializers
from .models import Education, Experience, Award, CandidateProfile 
from authapp.serializers import UserSerializer 

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id','user', 'title', 'company', 'location', 'duration']

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id','user', 'exam', 'institute', 'passing_year', 'result']
        read_only_fields = ['user']
        
class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = ['id','user', 'topic', 'title', 'organization', 'date', 'link']

class CandidateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateProfile
        fields = ['id', 'user','first_name','last_name', 'profile_avatar', 'about', 'phone','email','address', 'resume', 'hard_skill', 'linkedin', 'github', 'portfolio', 'slug']


    # def create(self, validated_data):
    #     request = self.context['request']
    #     return CandidateProfile.objects.create(user=request.user ,**validated_data)
    
    # def create(self, validated_data):
    #     experience_data = validated_data.pop('experience', [])
    #     award_data = validated_data.pop('award', [])
    #     education_data = validated_data.pop('education', [])

    #     profile = CandidateProfile.objects.create(**validated_data)

    #     for exp_data in experience_data:
    #         Experience.objects.create(user=profile.user, **exp_data)

    #     for award_data in award_data:
    #         Award.objects.create(user=profile.user, **award_data)

    #     for edu_data in education_data:
    #         Education.objects.create(user=profile.user, **edu_data)

    #     return profile
    
