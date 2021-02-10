from django.urls import include, path

from . import views

urlpatterns = [ 
    path("", views.index, name="index"), 
    path("profile/<str:username>/", views.profile, name="profile"), 
    path("new/", views.new_recipe, name="new_recipe"), 
    path("<str:username>/<int:recipe_id>/", views.recipe_view, name="recipe"), 
    path(
        "<str:username>/<int:recipe_id>/edit/", 
        views.recipe_edit, name="recipe_edit"), 
    path("favorites/", views.api_favorites_add, name="favorites_add"),
    path(
        "favorites/<int:id>/", 
        views.api_favorites_delete, name="favorites_delete"),
    path("favor/", views.favorites, name="favorites"), 
    path("subscriptions/", views.api_follow_add, name="follow_add"),
    path(
        "subscriptions/<str:id>/", 
        views.api_follow_delete, name="follow_delete"),
    path("followers/", views.follow, name="followers"),
    path("ingredients/", views.ingredients),
    path("shop/", views.purchases, name="my_purchases"),
    path("shop/download/", views.purchases_download, name="download"),
    path("purchases/", views.api_purchases_add, name="purchases_add"),
    path(
        "purchases/<int:id>/", 
        views.api_purchases_delete, name="purchases_delete"),
    path('about/', views.AboutPage.as_view(), name="about"),
    path('technology/', views.TechnologyPage.as_view(), name="technology"),
    path('brand/', views.BrandPage.as_view(), name="brand"),   
] 
