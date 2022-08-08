from django.shortcuts import render
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
