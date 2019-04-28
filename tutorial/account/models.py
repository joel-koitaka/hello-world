from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.PROTECT)
	description = models.CharField(max_length=100, default='')
	city = models.CharField(max_length=100, default='')
	website = models.URLField(default='')
	phone = models.IntegerField(default=0)

def create_profile(sender, **kawrgs):   #KWARGS IS A KEYWORJD ARGUMENTS
	if kawrgs['created']:
		user_profile= UserProfile.objects.create(user=kawrgs['instance'])

post_save.connect(create_profile, sender = User)

class Article(models.Model):
	"""docstring for article"""
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(default= 'null' , blank=True)
	file = models.FileField(default= 'null' , blank=True)



def __init__(self):
	return self.title  

def __init__(self):
	return self.body[:50] +'...' 
	 
	 