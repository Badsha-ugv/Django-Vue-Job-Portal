from django.db import models
from django.utils.text import slugify 
from authapp.models import CustomUser 

class Experience(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='experiences')
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=150,blank=True,null=True)
    location = models.CharField(max_length=80,blank=True,null=True)
    duration = models.CharField(max_length=100,blank=True,null=True)


class Award(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='awards')
    topic = models.CharField(max_length=150)
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=150)
    date = models.DateField(blank=True,null=True)
    link = models.URLField(blank=True,null=True)

class Education(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name='educations') 
    exam = models.CharField(max_length=100)
    institute = models.CharField(max_length=200)
    passing_year = models.CharField( max_length=50)
    result = models.CharField(max_length=50,blank=True,null=True) 


class CandidateProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=100,blank=True)
    profile_avatar = models.ImageField(upload_to='candidate_profile/',blank=True,null=True)
    about = models.TextField(blank=True,null=True)
    phone = models.CharField(max_length=20,blank=True,null=True)
    email = models.EmailField(max_length=50,blank=True)
    resume = models.FileField(upload_to='resume/',blank=True,null=True)
    hard_skill = models.CharField(max_length=100)
    linkedin = models.URLField(max_length=100,blank=True,null=True)
    github = models.URLField(max_length=100,blank=True,null=True)
    portfolio = models.URLField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=150,blank=True)
    slug = models.SlugField(unique=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username) 
        super(CandidateProfile, self).save(*args,**kwargs)
         

    def __str__(self):
        return f'{self.user.username}'