# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Prenom(models.Model):

    #__Prenom_FIELDS__
    evt = models.CharField(max_length=255, null=True, blank=True)
    level = models.CharField(max_length=255, null=True, blank=True)
    sexe = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    code_dpt = models.IntegerField(null=True, blank=True)
    prenom = models.CharField(max_length=255, null=True, blank=True)
    fichier = models.IntegerField(null=True, blank=True)

    #__Prenom_FIELDS__END

    class Meta:
        verbose_name        = _("Prenom")
        verbose_name_plural = _("Prenom")



#__MODELS__END
