
from django.urls import path
from cookbook import views

urlpatterns = [
    path('', views.index, name = 'homepage'),
    path('author/<int:id>/', views.author_detail, name='author'),
    path('recipe/<int:id>/', views.recipe_detail, name='recipe'),  
    path('recipeadd/', views.recipeadd, name='recipeadd'),
    path('authoradd/', views.authoradd, name='authoradd')
]
