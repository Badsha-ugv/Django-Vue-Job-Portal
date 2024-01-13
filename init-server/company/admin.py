from django.contrib import admin

from .models import CompanyProfile, JobApplication , JobPost


admin.site.register(CompanyProfile)
admin.site.register(JobPost)
admin.site.register(JobApplication)