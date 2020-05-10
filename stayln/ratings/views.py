#! /usr/bin/python3

__author__ = "CunjunWang <cw3199@columbia.edu>"
__date__ = "2020/5/10"

from django.contrib import messages
from django.shortcuts import redirect

from ratings.models import Ratings


def add_rating(request):
    if request.method == 'POST':
        score = request.POST['score']
        comment = request.POST['comment']
        user_id = request.POST['user_id']
        realtor_id = request.POST['realtor_id']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_rating = Ratings.objects.all().filter(
                user_id=user_id, realtor_id=realtor_id, type=1, is_published=True)
            if has_rating:
                messages.error(
                    request, 'You have already rated this realtor!')
                return redirect('/realtors/' + realtor_id)
        else:
            messages.error(request, 'Please login')
            return redirect('login')

        rating = Ratings(score=score, user_id=user_id, realtor_id=realtor_id,
                         content=comment, type=1, is_published=True)
        rating.save()

        return redirect('/realtors/' + realtor_id)
