from django import forms


class CreateCategoryForm(forms.Form):
    name = forms.CharField(max_length=200, required=True)
