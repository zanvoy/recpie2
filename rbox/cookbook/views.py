from django.shortcuts import render, reverse, HttpResponseRedirect 
from cookbook.models import Recipe, Author
from cookbook.forms import RecipeAddForm, AuthorAddForm


# Create your views here.
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

def authoradd(request):
    html = 'addform.html'

    if request.method == 'POST':
        form = AuthorAddForm(request.POST)
        form.save()
        return HttpResponseRedirect('/')

    form = AuthorAddForm()
    return render(request, html, {'form': form})