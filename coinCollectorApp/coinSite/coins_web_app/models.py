from django.db import models
import datetime

class DisplayQuarters(models.Model):

    number = models.IntegerField()
    state = models.CharField(max_length = 200)
    release_date = models.CharField(max_length = 200)
    elements = models.CharField(max_length = 200)
    engraver = models.CharField(max_length = 200)
    image_link = models.TextField()

    def __str__(self):
        return self.state

class Join(models.Model):
    email = models.EmailField()
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.email


# class Person(models.Model):
#     """ The model defines a user of the application.  """
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=200, null=True)
#     last_name = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)
#     # city = models.CharField(max_length=200, null=True)
#     # state = models.CharField(max_length=200, null=True)
#     age = models.CharField(max_length=50, null=True)
