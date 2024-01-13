from django.db.models.signals import post_save 
from django.dispatch import receiver 
from .models import CustomUser
from candidate.models import CandidateProfile
from company.models import CompanyProfile


@receiver(post_save,sender=CustomUser)
def create_profile(sender,instance,created,**kwargs):
    if created:
        if instance.account_type == 'company':
            CompanyProfile.objects.create(user=instance)
        elif instance.account_type == 'candidate':
            CandidateProfile.objects.create(user=instance)
        