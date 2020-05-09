# Create your views here.

from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .models import Realtor


def listing(request):
    realtors = Realtor.objects.all()
    # print(len(realtors))

    paginator = Paginator(realtors, 10)
    page = request.GET.get('page')
    paged_realtors = paginator.get_page(page)

    context = {'realtors': paged_realtors}

    return render(request, 'realtors/list.html', context)

