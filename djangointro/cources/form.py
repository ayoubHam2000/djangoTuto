from django import forms

from .models import Cource

class CourceModelFrom(forms.ModelForm):
    class Meta:
        model = Cource
        fields = [
            'title',
            'content'
        ]
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.lower() == 'abc':
            raise forms.ValidationError("This is not a valide title")
        return title
    
    def clean_content(self):
        content = self.cleaned_data.get('content')
        return content