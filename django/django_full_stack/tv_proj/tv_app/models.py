from django.db import models
import datetime

# Create your models here.
class showsManager(models.Manager):
    def showValidator(self, postData):
        errors = {}
        if len(postData['inputShowTitle']) < 2:
            errors['titleReq'] = "Title must be at least 2 characters"
        if len(postData['inputShowNetwork']) < 3:
            errors['networkReq'] = "Network must be at least 3 characters"
        if len(postData['inputReleaseDate']) == 0:
            errors['releaseDateReq'] = "Release Date Required"
        if len(postData['inputShowDesc']) > 0 and len(postData['inputShowDesc']) < 10:
            errors['showDescReq'] = "Description must be at least 10 characters"
        return errors


class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    releaseDate = models.CharField(max_length=255)
    description = models.TextField(default="")
    objects = showsManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)