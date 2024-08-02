from django.db import models
from django.contrib.auth.models import User

class SliderValue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
