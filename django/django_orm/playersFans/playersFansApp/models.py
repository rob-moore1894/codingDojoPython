from django.db import models

# Create your models here.
class PlayerManager(models.Manager):
	def playerValidator(self, postData):
		#create errors dictionary where we will store our validation error messages
		errors = {}
		if len(postData['fname']) == 0:
			errors['fnameRequired'] = "First name required!"
		if len(postData['lname']) == 0:
			errors['lnameRequired'] = "Last name required!"
		if len(postData['team']) < 3:
			errors['teamRequired'] = "Team Name must be at least 3 characters long"
		print(errors)
		return errors



class Player(models.Model):
	firstname = models.CharField(max_length=255)
	lastname = models.CharField(max_length=255)
	team = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = PlayerManager()
	def __repr__(self):
		return f"Player Object {self.firstname} - {self.id}"

class Fan(models.Model):
	firstname = models.CharField(max_length=255)
	lastname = models.CharField(max_length=255, null = True)
	# books = models.ManyToManyField(Book, related_name="publishers")
	favPlayers = models.ManyToManyField(Player, related_name = "fans")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __repr__(self):
		return f"Fan Object {self.firstname} - {self.id}"






