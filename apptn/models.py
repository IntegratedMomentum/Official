from django.db import models

# Create your models here.
class Contact(models.Model):
  name = models.CharField(max_length=100)
  password = models.CharField(max_length=100, null=True)
  desc = models.CharField(max_length=500, null=True)

class Inst(models.Model):
  iname = models.CharField(max_length=100)
  ipassword = models.CharField(max_length=100, null=True)

