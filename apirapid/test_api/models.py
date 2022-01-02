from django.db import models
from datetime import datetime
import uuid
# Create your models here.
class TestApi(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250,default="")
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
   
    
    def __str__(self):
        return self.name