from django.test import TestCase
from django.models import MetricsLog
import datetime

class CounterMetricsTest(TestCase):

    def setUp(self):
		pass  

    def test_that_counts_one_increment_per_day(self):
		counter_metric = Counter()
		date = datetime.date.today()
		
		self.assertEqual(1,counter_metric.group_per_day(date)) 
		
		
class Counter():

	def group_per_day(self, date):
		print MetricsLog.objects.all.count
		rawData = MetricsLog.objects.all.count
		