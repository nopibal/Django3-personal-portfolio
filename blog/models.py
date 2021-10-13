from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=110)
    date = models.DateField(auto_now=True)
    description = models.CharField(max_length=250)
