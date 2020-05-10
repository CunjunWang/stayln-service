#! /usr/bin/python3

__author__ = "CunjunWang <cw3199@columbia.edu>"
__date__ = "2020/5/10"

from django.contrib import messages
from django.shortcuts import redirect

from ratings.models import Ratings


def add_rating(request):
    if request.method == 'POST':
        score = int(request.POST['score'])
        comment = request.POST['comment']
        user_id = request.POST['user_id']
        user_name = request.POST['user_name']

        try:
            realtor_id = request.POST['realtor_id']
            path = 'realtors'
            rating_type = 1
            rating_id = realtor_id
        except:
            listing_id = request.POST['listing_id']
            path = 'listings'
            rating_type = 2
            rating_id = listing_id

        if (not isinstance(score, int)) or (score < 1 or score > 5):
            messages.error(
                request, 'You entered an invalid score!')
            return redirect('/' + path + '/' + rating_id)

        if request.user.is_authenticated:
            user_id = request.user.id
            if rating_type == 1:
                has_rating = Ratings.objects.all().filter(
                    user_id=user_id, realtor_id=rating_id, type=rating_type, is_published=True)
                if has_rating:
                    messages.error(
                        request, 'You have already rated this realtor!')
                    return redirect('/' + path + '/' + rating_id)
            else:
                has_rating = Ratings.objects.all().filter(
                    user_id=user_id, listing_id=rating_id, type=rating_type, is_published=True)
                if has_rating:
                    messages.error(
                        request, 'You have already rated this house!')
                    return redirect('/' + path + '/' + rating_id)
        else:
            messages.error(request, 'Please login')
            return redirect('login')

        if rating_type == 1:
            rating = Ratings(score=score, user_id=user_id, user_name=user_name, realtor_id=rating_id,
                             content=comment, type=rating_type, is_published=True)
        else:
            rating = Ratings(score=score, user_id=user_id, user_name=user_name, listing_id=rating_id,
                             content=comment, type=rating_type, is_published=True)

        rating.save()
        return redirect('/' + path + '/' + rating_id)
