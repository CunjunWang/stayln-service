# Create your views here.

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Realtor
from listings.models import Listing


def realtor_list(request):
    realtors = Realtor.objects.all()
    # print(len(realtors))

    paginator = Paginator(realtors, 10)
    page = request.GET.get('page')
    paged_realtors = paginator.get_page(page)

    context = {'realtors': paged_realtors}

    return render(request, 'realtors/list.html', context)


def detail(request, realtor_id):
    realtor = get_object_or_404(Realtor, pk=realtor_id)
    listings = Listing.objects.filter(realtor_id=realtor_id)

    context = {
        'realtor': realtor,
        'listings': listings
    }

    return render(request, 'realtors/detail.html', context)
