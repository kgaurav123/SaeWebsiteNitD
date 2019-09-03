from django.db import models

class Autopia(models.Model):
    name = models.CharField(max_length=150)
    institution = models.CharField(max_length=150)
    article = models.TextField()

    def __str__(self):
        return (self.name)
