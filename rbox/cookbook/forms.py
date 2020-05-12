
from django import forms
from cookbook.models import Author

class RecipeAddForm(forms.Form):
    title = forms.CharField(max_length=42)
    req_time = forms.CharField(max_length=42)
    description = forms.CharField(widget=forms.Textarea)
    instructions = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())

class AuthorAddForm(forms.ModelForm):
    username = forms.CharField(max_length =42)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields = ['name','bio']
        model = Author

class LoginForm(forms.Form):
    username = forms.CharField(max_length =42)
    password = forms.CharField(widget=forms.PasswordInput)