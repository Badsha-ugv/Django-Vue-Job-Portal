from django.db import models
import datetime
from authapp.models import CustomUser
from candidate.models import CandidateProfile 

class CompanyProfile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,blank=True,null=True)
    user_avatar = models.ImageField(upload_to='hunter_avatar/',blank=True,null=True)
    designation = models.CharField(max_length=100,blank=True,null=True) 
    company_name = models.CharField(max_length=100, null=True)
    company_type = models.CharField(max_length=100,blank=True,null=True)
    about = models.TextField(blank=True,null=True)
    address = models.TextField(blank=True, null=True) 
    city = models.CharField(max_length=50, blank=True, null= True) 
    company_logo = models.ImageField(upload_to='company_logo/', blank=True,null=True)

    def __str__(self):
        return f"{self.company_name} in {self.address}"
 

class JobPost(models.Model):
    company = models.ForeignKey(CompanyProfile,on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=100)
    position = models.CharField(blank=True,null=True, max_length=100)
    hard_skill = models.CharField(max_length=100, blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    vacancy = models.PositiveIntegerField(default=1)
    experience = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100,blank=True,null=True)
    salary = models.IntegerField(default=0.00)
    publish_date = models.DateField(auto_now_add=True)
    close_date = models.DateField(blank=True,null=True)

    def __str__(self):
        return f'{self.company.name} post for {self.positon}' 
    
class JobApplication(models.Model):
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE, 
                            related_name='job_applications')
    user = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE, related_name='job_application_user')
    expected_salary = models.CharField(max_length=5, blank=True,null=True) 
    cover_letter = models.TextField(blank=True) 
    date = models.DateField(datetime.datetime.now()) 


