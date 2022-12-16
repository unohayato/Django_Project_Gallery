from django.db import models

# Create your models here.

class Post(models.Model):
  project = models.CharField(max_length=255, blank=False, null=False, unique=True)
  description = models.TextField(blank=True, null=False)
  team = models.CharField(max_length=255, blank=False, null=False)
  pm = models.CharField(max_length=255, blank=False, null=False)
  second_menber = models.CharField(max_length=255, blank=False, null=False)
  third_menber = models.CharField(max_length=255, blank=False, null=False)
  created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=False, null=False)
  updated_at = models.DateTimeField(auto_now=True, editable=False, blank=False, null=False)
  
  def __str__(self):
    return self.project
  