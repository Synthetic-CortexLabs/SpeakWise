from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
class Speaker(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    twitter = models.CharField(max_length=50)
    organization = models.CharField(max_length=100)
    bio = models.TextField()
    avatar = models.ImageField(upload_to="speakers/avatars/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "speakers"
        verbose_name = "Speaker"
        verbose_name_plural = "Speakers"

    def __str__(self):
        return self.user.username
    

    
    def get_absolute_url(self):
        return reverse("speaker_detail", kwargs={"pk": self.pk})
    
