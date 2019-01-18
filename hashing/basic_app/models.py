from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Creating model with one to one relationship

class UserProfileInfo(models.Model):

    #Creating the variables for taken users field info

    user = models.OneToOneField(User, on_delete=models.PROTECT)

    #Adding more fields to user
    portfolio_site = models.URLField(blank=True, )
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    # interested = models.TextField(blank=False)
    
    # Adding method for printing the users info
    def __str__(self):

        return self.user.username
