# recipes/forms.py
from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'image', 'category']

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image and len(image.name) > 100:
            raise forms.ValidationError("Ensure the filename has at most 100 characters.")
        return image