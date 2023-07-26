from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q


def search(request):
    template = 'patterns/search.html'
    context = {}

    context['query'] = query = request.POST['q'] if request.method == 'POST' else ''

    context['patterns'] = list(
        Pattern.objects.filter(
            Q(type__name="Objetivos") & 
            (Q(name__icontains=query)
            | Q(description__icontains=query)
            | Q(catalogue__title__icontains=query))
        )
    )

    return render(request, template, context)

def pattern_detail(request, pattern_id):
    template = 'patterns/pattern_detail.html'
    context = {}

    # Get the pattern instance using the provided pattern_id or display a 404 page if not found
    pattern = get_object_or_404(Pattern, id=pattern_id)

    context['pattern'] = pattern

    return render(request, template, context)