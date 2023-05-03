from django import forms
from .models import Product
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    description = forms.CharField(min_length=20)

    class Meta:
        model = Product
        fields = [
            'name',
            'composition',
            'description',
            'quantity',
            'category',
            'price',
        ]
        # fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")
        if name == description:
            raise ValidationError(
                "Name and descriptions should be different"
            )
        return cleaned_data

    def clean_name(self):
        name = self.cleaned_data["name"]
        if name[0].islower():
            raise ValidationError(
                "Название должно начинаться с заглавной буквы"
            )
        return name
