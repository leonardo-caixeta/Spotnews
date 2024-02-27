from django import forms

from news.models import Category, User
from news.utils import validate_title


class CreateCategoryForm(forms.Form):
    name = forms.CharField(max_length=200, required=True)


class CreateNewsForm(forms.Form):
    title = forms.CharField(max_length=200, validators=[validate_title])
    content = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=User.objects.all())
    created_at = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    image = forms.ImageField(required=False)
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all())
