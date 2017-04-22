from django.db import models

class DisplayQuarters(models.Model):

    number = models.IntegerField()
    state = models.CharField(max_length = 200)
    release_date = models.CharField(max_length = 200)
    elements = models.CharField(max_length = 200)
    engraver = models.CharField(max_length = 200)
    image_link = models.TextField()

    def __str__(self):
        return '{}'.format(self.state)
