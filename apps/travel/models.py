from __future__ import unicode_literals

from django.db import models
from ..logreg.models import User
from datetime import datetime, date
#from .managers import TravelManager
# Create your models here.
class TravelManager(models.Manager):
    def validation(self, post):
        print post
        today = date.today()
        errors = []
        if len(post['destination']) == 0:
            errors.append("Destination is required")
        if len(post['description']) == 0:
            errors.append("Description is required")

        if len(post['start_date']) == 0:
            errors.append("Start date is required")
        else:
            try:
                start_date = datetime.strptime(post['start_date'], '%Y-%m-%d')
                if start_date.date() < today:
                    errors.append("Start date cannot be in the past")
            except:
                errors.append("Please enter a valid date for the start date field!")

        if len(post['end_date']) == 0:
            errors.append("End date is required")
        else:
            try:
                end_date = datetime.strptime(post['end_date'], '%Y-%m-%d')
                if end_date.date() < start_date.date():
                    errors.append("End date cannot be before the start date!")
            except:
                errors.append("Please enter a valid date for the end date field!")
        return errors


class Travel(models.Model):
    destination = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    start_date = models.DateTimeField(max_length=255)
    end_date = models.DateTimeField(max_length=255)
    creator = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TravelManager()

class Member(models.Model):
    member = models.ForeignKey(User)
    travel = models.ForeignKey(Travel)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
