from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import (
    Recipe, Ingredient, Number, 
    Favorite, User, Follow, Tag, Purchase
)
from .forms import RecipeForm, NumberForm
from .serializers import (
    FavoriteSerializer, 
    FollowSerializer, 
    IngredientSerializer, 
    PurchaseSerializer
)
from django.http import JsonResponse
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.pdfbase.ttfonts import TTFont   
from reportlab.pdfbase import pdfmetrics

def index(request):
    
    TAGS = ["breakfast", "dinner", "lunch"]
    tags = request.GET.getlist("tag", TAGS )
    recipe_list = Recipe.objects.filter(
        tags__title__in=tags).select_related(
            "author").distinct()
    tags = Tag.objects.all()
    paginator = Paginator(recipe_list, 6)  
    page_number = request.GET.get("page")  
    page = paginator.get_page(page_number) 
    
    return render(
        request,
        "indexAuth.html", {"recipe_list": recipe_list, 
        "tags":tags, "page": page, "paginator": paginator}
    )

def profile(request, username):
    TAGS = ["breakfast", "dinner", "lunch"]
    tags = request.GET.getlist("tag", TAGS )
    recipe_list = Recipe.objects.filter(
        author__username=username, tags__title__in=tags).distinct()
    profile = get_object_or_404(User, username=username)
    tags = Tag.objects.all()
    paginator = Paginator(recipe_list, 6)  
    page_number = request.GET.get("page")  
    page = paginator.get_page(page_number)
    
    return render(
        request,
        "authorRecipe.html", {"recipe_list": recipe_list, 
        "profile": profile, "tags":tags, "page": page, 
        "paginator": paginator 
        }
    )

@login_required
def new_recipe(request):

    form = RecipeForm(request.POST or None, files=request.FILES or None)
    if not form.is_valid():
        return render(request, "formRecipe.html", {"form": form })      
    recipe = form.save(commit=False)
    recipe.author = request.user
    recipe.save()
    form.save_m2m()
    
    request_dict = request.POST
    numbers = [k[15:] for k,v in request_dict.items() if 'nameIngredient' in k]
   
    for number in numbers:
        name = 'nameIngredient_' + str(number)
        value ='valueIngredient_' + str(number)
        ingredient = get_object_or_404(Ingredient, title=request_dict[name])
        number_create = Number.objects.create(
            recipe=recipe, ingredient=ingredient, amount=request_dict[value])      
    return redirect("index")  

def recipe_view(request, username, recipe_id):
        
    recipe = get_object_or_404(Recipe, pk=recipe_id, author__username=username)
    author = recipe.author
    ingredients = Ingredient.objects.filter(recipes=recipe)
    favorite = Favorite.objects.filter(
        recipe=recipe, user__username=request.user).exists()
    follow = Follow.objects.filter(
        author__username=username, user__username=request.user).exists()
    amounts = Number.objects.filter(recipe=recipe)
    tags = Tag.objects.filter(recipe=recipe)
    return render(
        request, 
        "singlePage.html", 
        {"recipe": recipe, 
        "author": author,
        "ingredients": ingredients,
        "favorite": favorite,
        "follow": follow,
        "amounts": amounts,
        "tags": tags,
        }
    )

@login_required()
def recipe_edit(request, username, recipe_id):

    recipe = get_object_or_404(Recipe, pk=recipe_id, author__username=username)
    amounts = Number.objects.filter(recipe=recipe)
    if request.user != recipe.author:
        return redirect(f"/{recipe.author}/{recipe_id}")
    form = RecipeForm(
        request.POST or None, files=request.FILES or None, instance=recipe)
    if not form.is_valid():
        return render(
            request, 
            "formChangeRecipe.html",
            {"recipe": recipe, 
            "form": form,
            "amounts": amounts}
        )  
    recipe = form.save(commit=False)
    recipe.author = request.user
    recipe.save()
    form.save_m2m()
    
    request_dict = request.POST
    numbers = [k[15:] for k,v in request_dict.items() if 'nameIngredient' in k and v != '']
   
    for number in numbers:
        name = 'nameIngredient_' + str(number)
        value ='valueIngredient_' + str(number)
        ingredient = get_object_or_404(Ingredient, title=request_dict[name])
        number_create = Number.objects.create(
            recipe=recipe, ingredient=ingredient, amount=request_dict[value])   
    return redirect(f"/{recipe.author}/{recipe_id}/")


@api_view( ['POST']) 
def api_favorites_add(request):
    
    serializer = FavoriteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(
            user = request.user, recipe = Recipe.objects.get(
                pk=request.data['id'])
        )
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)


@api_view( ['DELETE']) 
def api_favorites_delete(request, id):
    
    recipe = Recipe.objects.get(pk=id)
    favorite = get_object_or_404(Favorite, recipe=recipe, user = request.user)
   
    if request.method == 'DELETE':
        if request.user.is_authenticated:
            if favorite.user == request.user:
                favorite.delete()
                return Response('errors')
            return Response('errors', status=status.HTTP_403_FORBIDDEN)
        return Response('errors', status=status.HTTP_403_FORBIDDEN)

def favorites(request):

    TAGS = ["breakfast", "dinner", "lunch"]
    tags = request.GET.getlist("tag", TAGS )
    favorite = Favorite.objects.filter(
        user__username=request.user, recipe__tags__title__in=tags).distinct()
    tags = Tag.objects.all()
    paginator = Paginator(favorite, 6)  
    page_number = request.GET.get("page")  
    page = paginator.get_page(page_number) 
    
    return render(
        request,
        "favorite.html", {"favorite": favorite, "tags":tags, 
        "page": page, "paginator": paginator}
    )

@api_view( ['POST']) 
def api_follow_add(request):
    
    serializer = FollowSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(
            user = request.user, author = get_object_or_404(
                User, username = request.data['id'])
        )
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)

@api_view( ['GET','DELETE']) 
def api_follow_delete(request, id):
    
    author = get_object_or_404(User, username = id)
    follow= get_object_or_404(Follow, author=author, user = request.user)
    
    if request.method == 'DELETE':
        if request.user.is_authenticated:
            if follow.user == request.user:
                follow.delete()
                return Response('errors')
            return Response('errors', status=status.HTTP_403_FORBIDDEN)
        return Response('errors', status=status.HTTP_403_FORBIDDEN)

@login_required
def follow(request):

    follow = User.objects.filter(
        following__user=request.user).prefetch_related('authors')
    paginator = Paginator(follow, 6)  
    page_number = request.GET.get("page")  
    page = paginator.get_page(page_number)

    return render(
        request,
        "myFollow.html", {"follow": follow, 
        "page": page, "paginator": paginator}
    ) 

@login_required
def purchases(request):
    
    purchases = Purchase.objects.filter(user=request.user)  
   
    return render(
        request,
        "shopList.html", {"purchases": purchases}
    ) 


@login_required
def purchases_download(request):
    
    recipes = Recipe.objects.filter(
    purchase__user=request.user
)
    ingr = {}
    
    for recipe in recipes:
        ingredients = recipe.ingredient.values_list('title', 'dimension')
        numbers = recipe.numbers.values_list('amount', flat=True)
        
        for num in range(len(ingredients)):
            name = ingredients[num][0]
            unit = ingredients[num][1]
            amount = numbers[num]
            if name in ingr:
                ingr[name] = [ingr[name][0] + amount, unit]
            else:
                ingr[name] = [amount, unit]
        
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="shop_list.pdf"'
    p = canvas.Canvas(response)
    pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
    p.setFont("Verdana", 16)
    a = [k + ' - ' + str(v[0]) + v[1] for k,v in ingr.items() ]
    p.drawString(200 , 800, "СПИСОК ПОКУПОК")
    for i, item in enumerate(a):
        p.drawString(230 , 700 + i*20, str(a[i]))
    p.showPage()
    p.save()
    return response
    

def ingredients(request):
    
    q = request.GET.get('query')

    ingredients = Ingredient.objects.filter(title__istartswith=q)
    results = []
    for ingredient in ingredients:
        dic = {}
        dic['title']= ingredient.title
        dic['dimension']= ingredient.dimension
        results.append(dic)
       
    return JsonResponse(results, safe=False)

@api_view( ['POST']) 
def api_purchases_add(request):
    
    serializer = PurchaseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(
            user = request.user, recipe = Recipe.objects.get(
                pk=request.data['id'])
        )
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)


@api_view( ['DELETE']) 
def api_purchases_delete(request, id):
    
    recipe = Recipe.objects.get(pk=id)
    purchase = get_object_or_404(Purchase, recipe=recipe, user = request.user)
   
    if request.method == 'DELETE':
        if request.user.is_authenticated:
            if purchase.user == request.user:
                purchase.delete()
                return Response('errors')
            return Response('errors', status=status.HTTP_403_FORBIDDEN)
        return Response('errors', status=status.HTTP_403_FORBIDDEN)



