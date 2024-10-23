from django.db import models


# Create your models here.
class Car(models.Model):
    title = models.TextField(max_length=250)
    year = models.TextField(max_length=4, null=True)
    color = models.TextField(max_length=20, null=True)

    # Return the title of the car for show in shell
    def __str__(self):
        return f"{self.title} - {self.year} - {self.color}"


class Publisher(models.Model):
    name = models.TextField(max_length=200)
    address = models.TextField(max_length=250, null=True)
    # city = models.TextField(max_length=250, null=True)
    # state_province = models.TextField(max_length=250, null=True)
    # country = models.TextField(max_length=250, null=True)

    # Return the name of the publisher for show in shell
    def __str__(self):
        return f"{self.name} - {self.address}"


class Book(models.Model):
    title = models.TextField(max_length=200)
    publication_date = models.DateField()
    # ForeignKey is a relationship between two models
    # what is on_delete=models.CASCADE?
    # CASCADE: If the referenced object is deleted, also delete the object that has the ForeignKey.
    # If publisher is deleted, also delete the book
    # also, on_delete have more options.
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.publication_date} - {self.publisher}"
