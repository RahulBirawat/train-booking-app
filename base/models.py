from django.db import models

# Create your models here.
class register_user(models.Model):
    full_name = models.CharField(max_length=200)
    e_mail = models.CharField(max_length=200)
    pass_word = models.CharField(max_length=200)