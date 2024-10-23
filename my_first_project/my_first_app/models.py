from django.db import models


# Create your models here.
class Car(models.Model):
    title = models.TextField(max_length=250)
    year = models.TextField(max_length=4, null=True)

    # Return the title of the car for show in shell
    def __str__(self):
        return self.title
