from django import forms
from django.core.exceptions import ValidationError
from soundkit.models import SoundKit
import os

class SoundKitForm(forms.ModelForm):
    class Meta:
        model = SoundKit
        fields = ['name', 'description', 'price', 'image', 'zip_file']
        error_messages = {
            'name': {'required': 'Please enter a name.'},
            'description': {'required': 'Please enter a description.'},
            'price': {'required': 'Please enter a price.'},
        }

    from django.core.exceptions import ValidationError
import os

def clean_image(self):
        image = self.cleaned_data.get("image")
        if image:
            ext = os.path.splitext(image.name)[1].lower()
            if ext not in ['.jpg', '.jpeg', '.png']:
                raise ValidationError("Unsupported file extension. Allowed extensions are: .jpg, .jpeg, .png")
            if image.size > 5 * 1024 * 1024:  # 5MB
                raise ValidationError("Image file too large ( > 5MB )")
        return image

def clean_zip_file(self):
        zip_file = self.cleaned_data.get("zip_file")
        if zip_file:
            ext = os.path.splitext(zip_file.name)[1].lower()
            if ext != '.zip':
                raise ValidationError("Unsupported file extension. Allowed extension is: .zip")
            if zip_file.size > 10 * 1024 * 1024:  # 10MB
                raise ValidationError("ZIP file too large ( > 10MB )")
        return zip_file
