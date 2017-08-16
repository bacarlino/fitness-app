from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User)
    current_weight = models.DecimalField(max_digits=6, decimal_places=1, null=True)
    height_feet = models.IntegerField(null=True)
    height_inches = models.IntegerField(null=True)
    sex = models.CharField(
        max_length=6,
        choices=(
            ('Male', 'Male'),
            ('Female', 'Female')
        ),
        null=True
    )

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()
