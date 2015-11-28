# Create your models here.
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey


class MetricOperation(models.Model):
	name = models.CharField(max_length=255)

class RawData(models.Model):
	name = models.IntegerField()
	rawDataInt = models.ForeignKey('RawDataInt')
	
class RawDataInt(models.Model):
	value = models.IntegerField()

class MetricLog(models.Model):
	metricKey = models.CharField(max_length=255)
	time = models.DateTimeField(auto_now=True)
	operation = models.ForeignKey(MetricOperation)
	value = models.ForeignKey(RawData)

