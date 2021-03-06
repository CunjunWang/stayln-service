from django.core.paginator import Paginator
from django.db.models import Avg
from django.shortcuts import render, get_object_or_404
from listings.choices import price_choices, bedroom_choices, state_choices, bathroom_choices
from ratings.models import Ratings

from .models import Listing


def index(req):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 24)
    page = req.GET.get('page')
    pageed_listings = paginator.get_page(page)

    context = {'listings': pageed_listings}
    return render(req, 'listings/listings.html', context)


def listing(req, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    ratings = Ratings.objects.filter(
        listing_id=listing.id, type=2, is_published=True
    ).order_by('submit_date')

    avg = Ratings.objects.filter(listing_id=listing.id, type=2, is_published=True).aggregate(Avg('score'))

    if avg['score__avg'] is None:
        avg = '-'
    else:
        avg = avg['score__avg']

    context = {
        'listing': listing,
        'ratings': ratings,
        'avg': avg,
        'total': len(ratings)
    }

    return render(req, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)
        # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__iexact=bedrooms)  # Bedrooms

    if 'bathrooms' in request.GET:
        bathrooms = request.GET['bathrooms']
        if bathrooms:
            queryset_list = queryset_list.filter(bathrooms__gte=bathrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'listings': queryset_list,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'bathroom_choices': bathroom_choices,
        'price_choices': price_choices,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
