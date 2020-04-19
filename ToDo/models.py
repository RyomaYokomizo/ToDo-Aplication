from django.db import models

# Create your models here.
class ToDo(models.Model):
    
    date = models.DateTimeField()
    job_name = models.TextField(max_length=50)
    job_text = models.TextField(max_length=255)

    def __str__(self):
        return self.job_name
