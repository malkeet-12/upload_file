from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(upload_to="images")
    attachment = models.FileField(upload_to="attachments")
    phone = models.CharField(max_length=10)