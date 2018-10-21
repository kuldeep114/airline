from django.db import models


class Airport(models.Model):

    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return "[{}]{}".format(self.code, self.city)


class Flight(models.Model):
    origin = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return "{} - {} to {}".format(self.id, self.origin, self.destination)


class Passengers(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flight = models.ManyToManyField(Flight, blank=True, related_name="flights")

    def __str__(self):
        return "{} {}".format(self.first, self.last)
