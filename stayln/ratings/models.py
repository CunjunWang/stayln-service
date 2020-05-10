__author__ = "CunjunWang <cw3199@columbia.edu>"
__date__ = "2020/5/10"

from datetime import datetime

from django.db import models


class Ratings(models.Model):
    score = models.IntegerField()
    user_id = models.IntegerField()
    realtor_id = models.IntegerField(null=True)
    listing_id = models.IntegerField(null=True)
    content = models.CharField(max_length=200)
    type = models.IntegerField()
    is_published = models.BooleanField()
    submit_date = models.DateTimeField(default=datetime.now)
