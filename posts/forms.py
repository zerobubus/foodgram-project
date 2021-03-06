from django import forms

from .models import Ingredient, Number, Recipe


class RecipeForm(forms.ModelForm):
    
    class Meta:
        
        model = Recipe
        fields = ["name", "description", "image", "time", "tags"]
        widgets = {
            "tags": forms.CheckboxSelectMultiple(),
            }

        error_messages = {
            'time': {
                'min_value': 'Время должно быть положительным числом'
            }
        }
    
class NumberForm(forms.ModelForm):
    
    class Meta:
        
        model = Number
        fields = ["recipe", "amount", "ingredient"]
    

 