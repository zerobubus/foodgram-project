from django.contrib import admin
from .models import Recipe, Ingredient, Number, Favorite, Follow, Tag, Purchase


class IngredientAdmin(admin.ModelAdmin):
    
    list_display = ("pk", "title", "dimension") 


class NumberAdmin(admin.ModelAdmin):
    
    list_display = ("pk", "ingredient", "amount") 


class FavoriteAdmin(admin.ModelAdmin):
    
    list_display = ("id", "recipe", "user")    


class PurchaseAdmin(admin.ModelAdmin):
    
    list_display = ("id", "recipe", "user")   


class FollowAdmin(admin.ModelAdmin):
    
    list_display = ("id", "author", "user")   


class TagAdmin(admin.ModelAdmin):
    
    list_display = ("id", "name", "color")    


class RecipeAdmin(admin.ModelAdmin):
    
    list_display = ("pk", "name", "pub_date", "author") 
    search_fields = ("text",) 
    list_filter = ("pub_date",) 
    empty_value_display = "-пусто-"


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Number, NumberAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Tag, TagAdmin)

