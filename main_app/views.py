from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pokemon, Item
from .forms import AttackForm

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def pokemons_index(request):
  pokemons = Pokemon.objects.all()
  return render(request, 'pokemons/index.html', { 'pokemons': pokemons })

def pokemons_detail(request, pokemon_id):
  pokemon = Pokemon.objects.get(id=pokemon_id)
  # Get the toys the cat doesn't have...
  # First, create a list of the toy ids that the cat DOES have
  id_list = pokemon.items.all().values_list('id')
  # Now we can query for toys whose ids are not in the list using exclude
  items_pokemon_doesnt_have = Item.objects.exclude(id__in=id_list)
  attack_form = AttackForm()
  return render(request, 'pokemons/detail.html', {
    'pokemon': pokemon, 'attack_form': attack_form,
    # Add the toys to be displayed
    'items': items_pokemon_doesnt_have
  })

def add_attack(request, pokemon_id):
  form = AttackForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_attack = form.save(commit=False)
    new_attack.pokemon_id = pokemon_id
    new_attack.save()
  return redirect('detail', pokemon_id=pokemon_id)



def assoc_item(request, pokemon_id, item_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Pokemon.objects.get(id=pokemon_id).items.add(item_id)
  return redirect('detail', pokemon_id=pokemon_id)



class PokemonCreate(CreateView):
  model = Pokemon
  fields = ['name', 'type', 'description', 'level']
  success_url = '/pokemons/'


class PokemonUpdate(UpdateView):
  model = Pokemon
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['type', 'description', 'level']

class PokemonDelete(DeleteView):
  model = Pokemon
  success_url = '/pokemons/'


class ItemList(ListView):
  model = Item

class ItemDetail(DetailView):
  model = Item

class ItemCreate(CreateView):
  model = Item
  fields = '__all__'

class ItemUpdate(UpdateView):
  model = Item
  fields = ['name', 'description']

class ItemDelete(DeleteView):
  model = Item
  success_url = '/items/'
