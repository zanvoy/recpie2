
from django import forms
from cookbook.models import Author

class RecipeAddForm(forms.Form):
    title = forms.CharField(max_length=42)
    req_time = forms.CharField(max_length=42)
    description = forms.CharField(widget=forms.Textarea)
    instructions = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())

class AuthorAddForm(forms.ModelForm):
    class Meta:
        fields = ['name','bio']
        model = Author
