from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pokemon
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
  # instantiate AttackForm to be rendered in the template
  attack_form = AttackForm()
  return render(request, 'pokemons/detail.html', {
    'pokemon': pokemon, 'attack_form': attack_form
  })

class PokemonCreate(CreateView):
  model = Pokemon
  fields = '__all__'
  success_url = '/pokemons/'

class PokemonUpdate(UpdateView):
  model = Pokemon
  fields = ['type', 'description', 'level']



class PokemonDelete(DeleteView):
  model = Pokemon
  success_url = '/pokemons/'
