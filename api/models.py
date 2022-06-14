from django.db import models

# Create your models here.

class Task(models.Model):
    STATUS = (
            ('ToDo','ToDo'),
            ('In Progress', 'In Progress'),
            ('Done','Done'),
               )

    start_time = models.DateTimeField(auto_now_add=False, null=True)
    end_time = models.DateTimeField(auto_now_add=False, null=True)
    title = models.CharField(max_length=200, null=True)
    describtion = models.CharField(max_length=200,null=True, blank=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS, default='ToDo')
    completed = models.BooleanField(default=False, blank=True, null=True)
      
    def __str__(self):
        return self.title