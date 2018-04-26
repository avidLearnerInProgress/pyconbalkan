from django.db import models
from django_countries.fields import CountryField

from pyconbalkan.core.models import SingleActiveModel


class Conference(SingleActiveModel):
    INTERNATIONAL = 0
    NATIONAL = 1
    CONF_TYPE = (
        (INTERNATIONAL, 'International'),
        (NATIONAL, 'National'),
    )

    event = models.CharField(null=True, blank=True, max_length=100)
    name = models.CharField(null=True, blank=True, max_length=100)
    year = models.PositiveIntegerField()
    number = models.PositiveIntegerField()
    city = models.CharField(null=True, blank=True, max_length=200)
    country = CountryField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    max_attendees = models.PositiveIntegerField(null=True, blank=True)
    type = models.IntegerField(choices=CONF_TYPE)


    def __str__(self):
        return '{} {} {}'.format(self.event, self.name, self.year)


class CountDown(SingleActiveModel):
    title = models.CharField(null=True, blank=True, max_length=100)
    count_down = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title