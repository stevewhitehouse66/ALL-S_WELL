from django.db import models

class About(models.Model):
    content = models.TextField()

    def __str__(self):
        return "About Content"
