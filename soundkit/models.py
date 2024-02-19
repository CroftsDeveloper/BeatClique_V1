from django.db import models
from cloudinary.models import CloudinaryField
from django.core.validators import FileExtensionValidator

class SoundKit(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # CloudinaryField for image uploads
    image = CloudinaryField('image')
    # CloudinaryField for sound file uploads
    sound_file = CloudinaryField('sound', resource_type='raw')
    # CloudinaryField for ZIP file uploads 'zip' format
    zip_file = CloudinaryField('zip', resource_type='raw', validators=[FileExtensionValidator(allowed_extensions=['zip'])])

    def __str__(self):
        return self.name
