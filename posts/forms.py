from django import forms
from .models import Recipe, Ingredient, Number


class RecipeForm(forms.ModelForm):
    
    class Meta:
        
        model = Recipe
    
        fields = ['name', 'description', 'image', 'time', 'tags']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
            }
    
    
class NumberForm(forms.ModelForm):
    
    class Meta:
        
        model = Number
    
        fields = ['recipe', 'amount', 'ingredient']

     
    