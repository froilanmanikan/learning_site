from django.db import models

# Create your models here.
class Course(models.Model):
	"""docstring for Course"""
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=255)
	description = models.TextField()

	def __str__(self):
		return self.title