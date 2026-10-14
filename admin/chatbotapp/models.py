from django.db import models

# Create your models here.
class chat(models.Model):
    query=models.TextField(max_length=255)
    answer=models.TextField(max_length=255)
    timestamp=models.DateTimeField()
    
