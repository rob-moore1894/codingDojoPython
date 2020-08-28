from django.db import models
import re
import bcrypt

class userManager(models.Manager):
    def regValidator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors = {}
        if len(postData['name']) == 0:
            errors['nameReq'] = 'Register: Name is required'
        if len(postData['email']) == 0:
            errors['emailreq'] = 'Register: Email is required'
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Register: Invalid email address!"
        else:
            repeatEmail = Users.objects.filter(email = postData['email'])
            if len(repeatEmail) > 0:
                errors['emailTaken'] = "Register: This email is already in use"
        if len(postData['password']) < 4:
            errors['pwreq'] = 'Register: Password must contain at least 4 characters'
        if postData['password'] != postData['confirmPassword']:
            errors['nomatchpw'] = 'Register: Passwords must match'
        return errors

    def loginValidator(self, postData):
        print(postData)
        errors = {}
        userByEmail = Users.objects.filter(email=postData['emailLogin'])
        if len(postData['emailLogin']) == 0:
            errors['emailReq'] = "Login: Please enter your email"
        elif len(userByEmail) == 0:
            errors['noEmailExists'] = "Login: Email is not registered"
        else: 
            user = userByEmail[0]
            if bcrypt.checkpw(postData['passwordLogin'].encode(), userByEmail[0].password.encode()):
                print('Passwords Match')
            else: 
                errors['wrongPw'] = "Login: Incorrect Password"
        return errors

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = userManager()

class Child(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(Users, related_name="child_uploaded", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Chores(models.Model):
    task = models.TextField()
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    assigned_to = models.ForeignKey(Child, related_name="chore_to_do", on_delete = models.CASCADE)
    task_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)