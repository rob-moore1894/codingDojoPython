from django.db import models
import re
import bcrypt

# Create your models here.
class userManager(models.Manager):
    def regValidator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        errors = {}
        if len(postData['fname']) == 0:
            errors['fnamereq'] = 'Register: First name is required'
        if len(postData['email']) == 0:
            errors['emailreq'] = 'Register: Email is required'
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Register: Invalid email address!"
        else:
            repeatEmail = User.objects.filter(email = postData['email'])
            if len(repeatEmail) > 0:
                errors['emailTaken'] = "Register: This email is already in use"
        if len(postData['pw']) < 4:
            errors['pwreq'] = 'Register: Password must contain at least 4 characters'
        if postData['pw'] != postData['pw2']:
            errors['nomatchpw'] = 'Register: Passwords must match'
        return errors

    def loginValidator(self, postData):
        errors = {}
        usersWithEmail = User.objects.filter(email=postData['email'])
        if len(postData['email']) == 0:
            errors['userEmailReq'] = "Login: Email is required"
        elif len(usersWithEmail) == 0:
            errors['userEmailWrong'] = "Login: Email is not registered"
        else:
            user = usersWithEmail[0]
            if bcrypt.checkpw(postData['pw'].encode(), usersWithEmail[0].password.encode()):
                print('Passwords Match')
            else: 
                errors['wrongPw'] = "Login: Incorrect Password"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = userManager()
    