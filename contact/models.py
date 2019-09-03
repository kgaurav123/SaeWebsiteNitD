from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    institution = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return (self.name)
