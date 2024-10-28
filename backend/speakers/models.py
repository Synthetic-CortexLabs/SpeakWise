from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from base.models import TimestampedModel


# Create your models here.
class Speaker(TimestampedModel):
    """
    Speaker Model
    This model represents a speaker in the SpeakWise application. It extends the TimestampedModel to include
    timestamp fields for creation and modification times.
    Attributes:
        user_id (OneToOneField): A one-to-one relationship with the User model. This field is required and 
                                 ensures that each speaker is associated with a unique user.
        twitter (CharField): A character field to store the speaker's Twitter handle. The maximum length is 50 characters.
        organization (CharField): A character field to store the name of the organization the speaker is associated with.
                                  The maximum length is 100 characters.
        bio (TextField): A text field to store the biography of the speaker.
        avatar (ImageField): An image field to store the avatar of the speaker. The images are uploaded to the 
                             "speakers/avatars/" directory.
    Meta:
        db_table (str): The name of the database table to use for this model ("speakers").
        verbose_name (str): The human-readable name for this model ("Speaker").
        verbose_name_plural (str): The plural name for this model ("Speakers").
    Methods:
        __str__(): Returns the username of the associated user.
        get_absolute_url(): Returns the absolute URL for the speaker detail view.
    """

    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    twitter = models.CharField(max_length=50)
    organization = models.CharField(max_length=100)
    bio = models.TextField()
    avatar = models.ImageField(upload_to="speakers/avatars/", null=True, blank=True)

    class Meta:
        db_table = "speakers"
        verbose_name = "Speaker"
        verbose_name_plural = "Speakers"

    def __str__(self):
        return self.user_id.username

    def get_absolute_url(self):
        return reverse("speaker_detail", kwargs={"pk": self.pk})