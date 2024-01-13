from django.urls import path, include 
from .views import * 
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()
router.register('candidate-profile',CandidateViewset)
router.register(r'education',EducationViewset,basename='education')
router.register(r'experience',ExperienceViewset,basename='experience')
router.register(r'award',AwardViewset,basename='award')

urlpatterns = [
    path('',include(router.urls)),
    
]