from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User)
    current_weight = models.IntegerField(null=True)
    height_feet = models.IntegerField(null=True)
    height_inches = models.IntegerField(null=True)
    sex = models.CharField(
        max_length=6,
        choices=(
            ('M', 'Male'),
            ('F', 'Female')
        ),
        null=True
    )

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Weight(models.Model):
    weight = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateField(null=True)

    def __str__(self):
        return str(self.weight) + ' lbs.'
