from django import forms
from .models import Settings, File
from django.forms.widgets import NumberInput


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file', )

class SettingEditForm(forms.ModelForm):
	class Meta:
		model = Settings
		fields = ['image_width', 'image_height', 'image_rotation', 'timeout']
		widgets = {
			'image_width'	: NumberInput(attrs={'min': 160, 'max': 640}),
			'image_height'	: NumberInput(attrs={'min': 120, 'max': 480}),
			'timeout'		: NumberInput(attrs={'min': 500, 'max': 4000}),			
			}



