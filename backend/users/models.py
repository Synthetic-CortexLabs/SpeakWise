from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
class UserProfile(models.Model):
    """
    UserProfile model represents the profile information associated with a user.
    Attributes:
        user_id (OneToOneField): A one-to-one relationship to the user model.
        bio (TextField): A text field to store the user's biography.
        profile_picture (ImageField): An image field to store the user's profile picture.
        social_links (CharField): A character field to store the user's social media links, can be null.
    Meta:
        db_table (str): The name of the database table.
        verbose_name (str): The human-readable name of the model.
        verbose_name_plural (str): The human-readable plural name of the model.
    Methods:
        __str__(): Returns the username of the associated user.
        get_absolute_url(): Returns the absolute URL for the user's profile detail view.
    """
    user_id = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(null=True)
    social_links = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "profiles"
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return f"{self.user_id.username}"

    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk": self.pk})
