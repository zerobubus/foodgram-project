from django.contrib import admin

from .models import Favorite, Follow, Ingredient, Number, Purchase, Recipe, Tag


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


class IngredientInline(admin.TabularInline):
    model = Number
    min_num = 1
    extra = 0
    verbose_name = 'ингредиент'


class RecipeAdmin(admin.ModelAdmin):
    
    list_display = ("pk", "name", "pub_date", "author", "count_favor") 
    search_fields = ("text",) 
    list_filter = ("pub_date",) 
    empty_value_display = "-пусто-"
    inlines = [IngredientInline,]

    def count_favor(self, obj):
        
        result = Favorite.objects.filter(recipe=obj).count()
        return result
    count_favor.short_description = "количество добавлений в избранное"


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Number, NumberAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Tag, TagAdmin)
