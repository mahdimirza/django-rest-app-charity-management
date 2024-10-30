from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    # id = models.AutoField()
    address = models.TextField(blank=True, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    # email = models.EmailField(blank=True, null=True)
    # date_joined = models.DateTimeField()
    # first_name = models.CharField(blank=True ,max_length=150, null=True)

    gender_choices = (
        ('F', 'female'),
        ('M', 'male'),
    )

    gender = models.CharField(choices=gender_choices, max_length=1, null=True, blank=True)
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)
    # last_login = models.DateTimeField(blank=True, null=True)
    # last_name = models.CharField(max_length=150, blank=True, null=True)
    # password = models.CharField(max_length=128)
    phone = models.CharField(max_length=15, blank=True, null=True)
    # username = models.CharField(unique=True, max_length=150)
