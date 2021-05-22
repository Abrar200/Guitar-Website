from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.conf import settings

class Songs(models.Model):
	title = models.CharField(max_length = 100)
	lyrics = models.TextField()
	author = models.CharField(max_length = 100)
	favorited_by = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='favorite_songs'
    )
	track_image = models.CharField(max_length=2083)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('/', kwargs={'pk': self.pk})



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=300)

    def __str__(self):
        return f'{self.user.username} Profile'

