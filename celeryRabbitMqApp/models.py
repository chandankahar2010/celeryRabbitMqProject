from django.db import models

# Create your models here.
# superUser chandan|chandan
class Items(models.Model):
    id = models.IntegerField(primary_key=True)
    item = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
