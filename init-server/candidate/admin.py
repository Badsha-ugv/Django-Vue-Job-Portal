from django.contrib import admin

from .models import CandidateProfile, Award, Education, Experience

admin.site.register(CandidateProfile)
admin.site.register(Award)
admin.site.register(Education)
admin.site.register(Experience)