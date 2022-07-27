from django.shortcuts import render
from .models import *
from django.db.models import Q


def search(request):
    template = 'patterns/search.html'
    context = {}

    context['query'] = query = request.POST['q'] if request.method == 'POST' else ''

    patterns = context['patterns'] = list(
        Pattern.objects.filter(
            Q(name__icontains=query)
            | Q(description__icontains=query)
            | Q(type__name__icontains=query)
            | Q(catalogue__title__icontains=query)
        )
    )

    return render(request, template, context)
