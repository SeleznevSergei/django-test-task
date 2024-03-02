from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(
        Country,
        related_name='manufacturers',
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(
        Manufacturer,
        related_name='cars',
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.name


class Comment(models.Model):
    e_mail = models.EmailField(max_length=100, null=True, blank=True)
    car = models.ForeignKey(
        Car,
        related_name='comments',
        on_delete=models.PROTECT,
    )
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.comment

