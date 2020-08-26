from django.db import models
import bcrypt

# Create your models here.
class userManager(models.Manager):
    def regValidator(self, postData):
        print(postData)
        errors = {}
        if len(postData['name']) < 3:
            errors['nameReq'] = 'Register: Name requires at least 3 characters'
        if len(postData['username']) < 3:
            errors['usernameReq'] = 'Register: Username requires at least 3 characters'
        if len(postData['password']) < 4:
            errors['pwreq'] = 'Register: Password must contain at least 4 characters'
        if postData['password'] != postData['confirmPassword']:
            errors['nomatchpw'] = 'Register: Passwords must match'
        return errors

    def loginValidator(self, postData):
        print(postData)
        errors = {}
        userByUsername = Users.objects.filter(username=postData['usernameLogin'])
        if len(postData['usernameLogin']) == 0:
            errors['usernameReq'] = "Login: Please enter your username"
        elif len(userByUsername) == 0:
            errors['noUsernameExists'] = "Login: Username is not registered"
        else: 
            user = userByUsername[0]
            if bcrypt.checkpw(postData['passwordLogin'].encode(), userByUsername[0].password.encode()):
                print('Passwords Match')
            else: 
                errors['wrongPw'] = "Login: Incorrect Password"
        return errors

    def productValidator(self, postData):
        print(postData)
        errors = {}
        if len(postData['item-product']) == 0:
            errors['itemReq'] = "Please enter an item"
        elif len(postData['item-product']) < 3:
            errors['itemChar'] = "Item must be at least 3 characters"
        return errors

class Users(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    date_hired = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = userManager()

class Products(models.Model):
    item = models.CharField(max_length=255)
    uploader = models.ForeignKey(Users, related_name="products_uploaded", on_delete = models.CASCADE)
    favoriters = models.ManyToManyField(Users, related_name="products_favorited")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

