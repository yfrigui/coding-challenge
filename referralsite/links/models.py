from django.db import models

# Create your models here.
class Link(models.Model):
	title = models.CharField(max_length=20)
	clicks = models.IntegerField(default=0)

	def __str__(self):
		return self.title



