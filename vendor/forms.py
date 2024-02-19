from django import forms
from soundkit.models import SoundKit

# Form to be used for adding and editing sound kits.
class SoundKitForm(forms.ModelForm):
    class Meta:
        model = SoundKit
        fields = ['name', 'description', 'price', 'image', 'zip_file']
