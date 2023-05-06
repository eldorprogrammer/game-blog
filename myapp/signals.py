from django.db.models.signals import post_save
from accounts.models import CustomUser
from .models import Profil,Turnir
from django.dispatch import receiver

@receiver(post_save,sender=CustomUser)
def create_profil(sender, instance, created, **kwargs):
    if created:
         Profil.objects.create(user=instance)

@receiver(post_save,sender=CustomUser)
def save_profile(sender,instance, **kwargs):
    instance.profil.save()


# @receiver(post_save,sender=CustomUser)
# def create_turnir(sender, instance, created, **kwargs):
#     if created:
#          Turnir.objects.create(user=instance)

# @receiver(post_save,sender=CustomUser)
# def save_turnir(sender,instance,**kwargs):
#     instance.turnir.save()