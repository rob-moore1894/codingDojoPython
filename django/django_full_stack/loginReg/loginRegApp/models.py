from django.db import models
import re

# Create your models here.
class userManager(models.Manager):
    def regValidator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        errors = {}
        if len(postData['fname']) == 0:
            errors['fnamereq'] = 'First name is required'
        if len(postData['email']) == 0:
            errors['emailreq'] = 'Email is required'
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        else:
            repeatEmail = User.objects.filter(email = postData['email'])
            if len(repeatEmail) > 0:
                errors['emailTaken'] = "This email is already in use"
        if len(postData['pw']) < 4:
            errors['pwreq'] = 'Password must contain at least 4 characters'
        if postData['pw'] != postData['pw2']:
            errors['nomatchpw'] = 'Passwords must match'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = userManager()