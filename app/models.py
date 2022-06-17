from email.mime import image
from django.db import models
from django.db.models import Model

# Create your models here.
class info(models.Model):
  name = models.CharField(max_length=100, blank=True, null=True)
  details = models.CharField(max_length=10000, blank=True, null=True)
  littype = models.CharField(default="Type of Litterature", blank=True, null=True, max_length=100)
  image = models.ImageField(default=None, blank=True, null=True, upload_to='app/files/covers')

class PostForm(models.Model):
  name = models.CharField(max_length=200)
  details = models.TextField()
  littype = models.TextField()
  image = models.FileField(upload_to='app/files/')

  def __str__(self):
    return self.name