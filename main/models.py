from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SpeedModel(models.Model):
	#pk = models.IntegerField(auto_increment=True)
	title = models.CharField(max_length=255)
	info = models.TextField()
	image = models.ImageField(upload_to='image', null=True, blank=True)
	user = models.ForeignKey(User)
	up_votes = models.ManyToManyField(User, null=True, blank=True, related_name='up_votes')
	down_votes = models.ManyToManyField(User, null=True, blank=True, related_name='down_votes')