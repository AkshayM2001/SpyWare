from django.db import models

# Create your models here.

class Command(models.Model):
    command = models.TextField()
    executed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.command
