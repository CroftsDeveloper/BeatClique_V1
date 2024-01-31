from django.db import models
from django.conf import settings

# Model for vendor profile.
class VendorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='vendor_profile_pics/', default='vendor_profile_pics/default.jpg')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
