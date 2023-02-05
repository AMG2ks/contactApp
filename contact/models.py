from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from contactProject import settings


# Create your models here.
class Contact(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="owner", on_delete=models.CASCADE)
    name = models.CharField(max_length=20, unique=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)

    REQUIRED_FIELDS = ['owner', 'name', 'phone']

    def __str__(self):
        return str(self.id)

