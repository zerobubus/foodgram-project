from django.db import models
from django.contrib.auth import get_user_model 
User = get_user_model() 

 
class Ingredient(models.Model): 
    title = models.TextField(verbose_name="название") 
    dimension = models.TextField(verbose_name="мера") 
    
    def __str__(self): 
        return self.title


class Tag(models.Model): 
    title = models.CharField(verbose_name="тег", max_length=20) 
    color = models.CharField(verbose_name="цвет", max_length=20) 
    name = models.CharField(verbose_name="имя тега", max_length=20)
    
    def __str__(self): 
        return self.name


class Recipe(models.Model): 
    name = models.CharField(verbose_name="имя", max_length=50) 
    description = models.TextField(verbose_name="описание") 
    pub_date = models.DateTimeField("date published", auto_now_add=True) 

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, 
        related_name="authors", 
        verbose_name="автор"
    ) 
    
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    time = models.TextField(verbose_name="время") 
    ingredient = models.ManyToManyField(
        Ingredient, through='Number', through_fields=('recipe','ingredient'), 
        related_name='recipes'
    )
    tags = models.ManyToManyField(Tag)


    class Meta: 
        ordering = ["-pub_date"] 
     

    def __str__(self): 
        return self.name


class Number(models.Model): 
    recipe = models.ForeignKey(
        Recipe , on_delete=models.CASCADE, related_name='numbers')
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name='numbers')
    amount = models.IntegerField()

    def __str__(self):
        return str(self.amount)


class Favorite(models.Model): 
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='favorite')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE, 
        related_name="follower"
        )
    
    class Meta:
        unique_together = ('user', 'recipe')


class Purchase(models.Model): 
    recipe = models.ForeignKey(
        Recipe , on_delete=models.CASCADE,  related_name='purchase')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE, 
        related_name="owner"
        )
    
    class Meta:
        unique_together = ('user', 'recipe')


class Follow(models.Model): 
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follow"
        )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following"
        )
    
    class Meta:
        unique_together = ('user', 'author')