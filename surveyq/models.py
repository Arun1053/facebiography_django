from django.db import models

# Create your models here.


class SurveyResponse(models.Model):
    all_in_one = models.JSONField()
    # images = models.JSONField(default={})
    # email_id = models.EmailField(unique=True, null=False, blank=False)
    # que_one = models.CharField(max_length=10, blank=True)
    # que_two = models.CharField(max_length=10, blank=True)
    # que_three = models.CharField(max_length=10, blank=True)
    # que_four = models.CharField(max_length=10, blank=True)
    # que_five = models.CharField(max_length=10, blank=True)
    # comm = models.CharField(max_length=100, blank=True)

