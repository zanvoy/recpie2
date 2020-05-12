from django.shortcuts import render, reverse, HttpResponseRedirect 
from cookbook.models import Recipe, Author
from cookbook.forms import RecipeAddForm, AuthorAddForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def loginview(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))
    form = LoginForm()
    html = 'addform.html'
    return render(request, html, {'form': form})

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
def index(request):
    data = Recipe.objects.all()
    return render(request, 'index.html', {'data': data})

def author_detail(request, id):
    person = Author.objects.get(id=id)
    recipe = Recipe.objects.filter(author=person)
    return render(request, 'author.html', {'person': person, 'recipe': recipe})

def recipe_detail(request, id):
    recipe = Recipe.objects.filter(id=id)
    return render(request, 'recipe.html', {'recipe': recipe})

@login_required
def recipeadd(request):
    html = 'addform.html'

    if request.method == 'POST':
        form = RecipeAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title = data['title'],
                description = data['description'],
                req_time = data['req_time'],
                instructions = data['instructions'],
                author = data['author']
            )
            return HttpResponseRedirect('/')

    form = RecipeAddForm()
    return render(request, html, {'form': form})

@login_required
def authoradd(request):
    html = 'addform.html'

    if request.method == 'POST':
        if request.user.is_staff():
            form = AuthorAddForm(request.POST)
            form.save()
        return HttpResponseRedirect('/')

    form = AuthorAddForm()
    return render(request, html, {'form': form})