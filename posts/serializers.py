from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Favorite, Follow, Ingredient, Purchase


class FavoriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id','recipe', 'user')
        model = Favorite
        read_only_fields = ['recipe', 'user']


class PurchaseSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id','recipe', 'user')
        model = Purchase
        read_only_fields = ['recipe', 'user']


class FollowSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id','user', 'author')
        model = Follow
        read_only_fields = ['user', 'author']
        

class IngredientSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ['title', 'dimension']
        model = Ingredient
        