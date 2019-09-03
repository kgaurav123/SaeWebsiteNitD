from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    date = models.DateTimeField()
    image = models.FileField(upload_to='post_image', blank=True, null=True)

    def __str__(self):
        return self.title
