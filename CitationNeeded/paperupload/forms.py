from django import forms
from .models import Paper

class PaperUploadForm(forms.ModelForm):
    class Meta:
        model = Paper
        fields = {'paper_name', 'file_link'}
