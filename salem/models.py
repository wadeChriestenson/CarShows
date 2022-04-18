from django.db import models

enthusiastChoices = (
    ('JDM', "JDM"),
    ('USDM', "USDM"),
    ("EDM", 'EDM'),
)


# Create your models here.
class meetInfo(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    host_name = models.CharField(max_length=100)
    meet_place = models.CharField(max_length=100)
    meet_address = models.CharField(max_length=100)
    meet_description = models.CharField(max_length=500)
    meet_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    enthusiast_type = models.CharField(max_length=15, choices=enthusiastChoices)
