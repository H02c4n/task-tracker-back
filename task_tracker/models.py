from django.db import models

# Create your models here.



class Task(models.Model):
    task = models.CharField(max_length=50)
    priority = models.CharField(max_length=6)
    date = models.DateTimeField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.task}'

