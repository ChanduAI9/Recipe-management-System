# recipes/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='recipes/login.html', next_page='home'), name='login'),  # specify next_page
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('edit/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('delete/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
    path('category/<int:category_id>/', views.recipes_by_category, name='recipes_by_category'),
]
