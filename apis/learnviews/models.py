from django.db import models

class Room(models.Model):
    title = models.CharField(max_length=300)
    price = models.FloatField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.title