from django import forms


class CategoryForms(forms.Form):
    name = forms.CharField(max_length=200, label="Nome")
