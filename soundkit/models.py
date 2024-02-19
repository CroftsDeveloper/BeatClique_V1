from django.db import models
from django.core.validators import FileExtensionValidator

class SoundKit(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # Reverted back to ImageField for image uploads, using Django's default file storage
    image = models.ImageField(upload_to='soundkits/images/')
    # FileField for ZIP file uploads
    zip_file = models.FileField(upload_to='soundkits/zips/', validators=[FileExtensionValidator(allowed_extensions=['zip'])])

    def __str__(self):
        return self.name
