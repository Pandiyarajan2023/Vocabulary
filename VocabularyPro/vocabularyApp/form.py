from django import forms
from vocabularyApp.models import vocabulary


class vocabularyForm(forms.ModelForm):
    class Meta:
        model = vocabulary
        fields = '__all__'
        