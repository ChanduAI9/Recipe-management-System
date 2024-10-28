from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Recipe, Category
from .forms import RecipeForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


#Home view to display all recipes

def home(request):
    recipes = Recipe.objects.all()
    return render(request,'recipes/home.html',{'recipes':recipes})



#regsiter a new user

def  register(request):
    if request.method == 'POST': #checks if the request is a form submissions(POST) or a page load(GET)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() #save the new user to the database
            return redirect('login')
    else:
        form=UserCreationForm() #Display an empty form for GET request
    return render(request,'recipes/register.html',{'form':form})

#add a new recipe

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST,request.FILES) #include both form data and uploaded files
        if form.is_valid():
            recipe=form.save(commit=False) #save the form data without committing to the database yet
            recipe.user=request.user #set the recipe user as the logged-in user
            recipe.save() # save the recipe to the database
            return redirect('home') # redirec to the home page after saving
    else:
        form=RecipeForm() #dispaly an empty form for get requets
    return render(request,'recipes/recipe_form.html',{'form':form})


#Edit an existing recipe
#This view allows users to edit a recipe they've previously created.
@login_required
def edit_recipe(request,recipe_id):
    recipe=get_object_or_404(Recipe,pk=recipe_id,user=request.user) #Fetches the recipe by its ID and ensures it belongs to the logged-in user.
    if request.method == 'POST':
        form = RecipeForm(request.POST,request.FILES,instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecipeForm(instance=recipe) #Display a form populated with the recipe's current data
    return render(request,'recipes/recipe_form.html',{'form':form})


#delete recipe
@login_required
def delete_recipe(request,recipe_id):
    recipe=get_object_or_404(Recipe,pk=recipe_id,user=request.user)
    if request.method == 'POST':
        recipe.delete() #delete the recipe from the database
        return redirect('home')
    return render(request,'recipes/recipe_confirm_delete.html',{'recipe':recipe})


#View Recipes By category (filter by category)

def recipes_by_category(request,category_id):
    category=get_object_or_404(Category,pk=category_id)
    recipes=Recipe.objects.filter(category=category)
    return render(request,'recipes/recipes_by_category.html',{'category':category,'recipes':recipes})

        