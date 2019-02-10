from django.shortcuts import render

# Create your views here.
from catalog.models import Game, Publisher

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_games= Game.objects.all().count()
    
    num_publisher = Publisher.objects.all().count()
        
    
    # The 'all()' is implied by default.    
   
    
    context = {
        'num_games': num_games,
        'num_publisher': num_publisher,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic
class GameListView (generic.ListView):
    model = Game
   
class GameDetailView(generic.DetailView):
    model = Game
