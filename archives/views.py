from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Genus

def archives(request):
    genus_list = Genus.objects.all()
    return render(request, 'archives.html', {'genus_list': genus_list})

def search(request):
    query = request.GET.get('query', '')  # Get the search query from the request
    results = []  # Placeholder for search results

    # Perform search logic here and populate the 'results' list

    context = {
        'query': query,
        'results': results,
    }

    return render(request, 'search_results.html', context)
