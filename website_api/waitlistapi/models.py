from django.db import models
from django.core.validators import EmailValidator
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class WaitlistEntry(models.Model):
    email = models.EmailField(unique=True, blank=False,validators=[EmailValidator()])
    FirstName = models.CharField(max_length=100, null=True, blank=False)
    LastName = models.CharField(max_length=100, null=True, blank=False)
    phone = PhoneNumberField(region='US', blank=False)
    timestamp = models.DateTimeField(auto_now_add=True,editable=False)

    def __str__(self):
        return self.email
