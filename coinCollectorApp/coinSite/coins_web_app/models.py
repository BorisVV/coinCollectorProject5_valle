from django.db import models

class DisplayQuaters(models.Model):
        number = models.IntegerField()
        state = models.CharField(max_length = 200)
        release_date = models.CharField(max_length = 200)
        elements = models.CharField(max_length = 200)
        engraver = models.CharField(max_length = 200)
        link = models.TextField()

        # def __str__(self):
        #     return self.number, self.state, self.release_date, self.elements, self.engraver, self.link
