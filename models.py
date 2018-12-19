from django.db import models
from datetime import datetime

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField(default=datetime.now, blank = True)
    def __str__(self):
        return self.title



