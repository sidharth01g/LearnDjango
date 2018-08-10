from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Additional information that the User class from Django does not have built in
class UserProfileInfo(models.Model):
    # One to one corresondence with each User
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additional fields

    # A user may have a website showcasing her/his portfolio. It may also be blank (no website URL provided)
    portfolio_site = models.URLField(blank=True)

    # Profile picture: Store in subfolder called 'profile_pics' under the 'media' directory
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self) -> str:
        return self.user.username
