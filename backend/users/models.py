from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.


class UserProfile(models.Model):

    user_id = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField()
    social_links = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "profiles"
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return f"{self.user_id.username}"

    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk": self.pk})
