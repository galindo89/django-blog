from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author= models.ForeignKey(User, on_delete=models.CASCADE, related_name='about_posts')
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    
    def __str__(self):
        return self.title
   
 