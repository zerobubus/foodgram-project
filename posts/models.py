from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator

User = get_user_model() 

 
class Ingredient(models.Model): 
    title = models.TextField(verbose_name="название") 
    dimension = models.TextField(verbose_name="мера") 
    
    def __str__(self): 
        return self.title
    
    class Meta: 
        verbose_name = "Ингредиент"


class Tag(models.Model): 
    title = models.CharField(verbose_name="тег", max_length=20) 
    color = models.CharField(verbose_name="цвет", max_length=20) 
    name = models.CharField(verbose_name="имя тега", max_length=20)
    
    def __str__(self): 
        return self.name

    class Meta: 
        verbose_name = "Тэг"


class Recipe(models.Model): 
    name = models.CharField(verbose_name="имя", max_length=50) 
    description = models.TextField(verbose_name="описание") 
    pub_date = models.DateTimeField(
        verbose_name="дата публикации", auto_now_add=True) 

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, 
        related_name="authors", 
        verbose_name="автор"
    ) 
    
    image = models.ImageField(upload_to="posts/", blank=True, null=True)
    time = models.PositiveIntegerField(
        verbose_name="время", validators=[MinValueValidator(1)]
        ) 
    ingredient = models.ManyToManyField(
        Ingredient, through="Number", through_fields=("recipe", "ingredient"), 
        related_name="recipes"
        )
    tags = models.ManyToManyField(Tag)


    class Meta: 
        ordering = ["-pub_date"]
        verbose_name = "Рецепт"
     

    def __str__(self): 
        return self.name


class Number(models.Model): 
    recipe = models.ForeignKey(
        Recipe , on_delete=models.CASCADE, 
        related_name="numbers", verbose_name="рецепт"
        )
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, 
        related_name="numbers", verbose_name="ингредиент"
        )
    amount = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return str(self.amount)
    
    class Meta: 
        verbose_name = "Число"


class Favorite(models.Model): 
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, 
        related_name="favorite", verbose_name="рецепт"
        )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE, 
        related_name="follower",
        verbose_name="пользователь"
        )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields= ["user", "recipe"], name="favorite_unique")]
        verbose_name = "Избранное"
        ordering = ("-created",)


class Purchase(models.Model): 
    recipe = models.ForeignKey(
        Recipe , on_delete=models.CASCADE,  
        related_name="purchase", verbose_name="рецепт"
        )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE, 
        related_name="owner",
        verbose_name="пользователь"
        )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields= ["user", "recipe"], name="purchase_unique")]
        verbose_name = "Покупки"
        ordering = ("-created",)


class Follow(models.Model): 
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follow",
        verbose_name="подписчик"
        )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following",
        verbose_name="на_кого_подписались"
        )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields= ["user", "author"], name="follow_unique")]
        verbose_name = "Подписки"
        ordering = ("-created",)
        