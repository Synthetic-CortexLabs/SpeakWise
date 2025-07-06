from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    social_links = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'profiles'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f"{self.user.username}'s Profile"
    

    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk": self.pk})
    
