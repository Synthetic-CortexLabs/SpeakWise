"""Organizers app models module."""

from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.


class Organizer(models.Model):
    """
    Model representing an Organizer.
    Attributes:
        user (OneToOneField): A one-to-one relationship with the User model.
        twitter (CharField): Twitter handle of the organizer, optional.
        facebook (CharField): Facebook profile of the organizer, optional.
        instagram (CharField): Instagram handle of the organizer, optional.
        linkedin (CharField): LinkedIn profile of the organizer, optional.
        organization (CharField): Name of the organization the organizer is associated with, optional.
        avatar (ImageField): Avatar image of the organizer, optional.
    Meta:
        verbose_name (str): Human-readable name for the model in singular form.
        verbose_name_plural (str): Human-readable name for the model in plural form.
    Methods:
        __str__(): Returns the string representation of the Organizer.
        get_absolute_url(): Returns the absolute URL for the Organizer detail view.
    """

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)
    organization = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    class Meta:
        """Meta options for the Organizer model."""

        db_table = "organizers"
        verbose_name = "Organizer"
        verbose_name_plural = "Organizers"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the absolute URL for the Organizer detail view."""
        return reverse("Organizer_detail", kwargs={"pk": self.pk})
