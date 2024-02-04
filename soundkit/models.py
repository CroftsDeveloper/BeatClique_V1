from django.db import models

class SoundKit(models.Model):
    # Existing fields
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='soundkit_covers/', default='soundkit_covers/default.jpg')
    # Updated to include soundkit files as ZIP
    sound_file = models.FileField(upload_to='soundkits/', default='soundkits/default_sound.mp3')
    zip_file = models.FileField(upload_to='soundkit_zips/', null=True, blank=True)

    def __str__(self):
        return self.name
