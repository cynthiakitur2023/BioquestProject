from django import forms
from .models import Categories, Products
class Category(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['category','image']


class Product(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name','image','photoname']
        widgets = {
            'photoname': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photoname'].required = False