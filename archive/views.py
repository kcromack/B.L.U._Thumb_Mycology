from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Genus

def index(request, genus=None):
    if genus:
        genus_obj = get_object_or_404(Genus, genus_name=genus)
        genus_list = Genus.objects.all()
        context = {'genus_list': genus_list, 'genus': genus_obj}
    else:
        genus_list = Genus.objects.all()
        context = {'genus_list': genus_list}
    return render(request, 'archive/arc_home.html', context)

def search(request):
    query = request.GET.get('query', '')  # Get the search query from the request
    results = []  # Placeholder for search results

    # Perform search logic here and populate the 'results' list

    context = {
        'query': query,
        'results': results,
    }

    return render(request, 'search_results.html', context)

def arc_home(request):
    return render(request, 'archive/arc_home.html')