from django import forms
from django.forms import fields
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from datetime import date

from .forms import SurveyForm

from .models import Survey

# Create your views here.
def index(request):
    return render(request, 'survey/index.html', {
        'name': 'Home Page'
    })


def take_survey(request):
    return render(request, 'survey/take_survey.html', {
        'today': date.today().strftime('%Y-%m-%d')
    })


def survey_results(request):
    sum_ages = 0
    pizza_likes_count = 0
    pasta_likes_count = 0
    pap_and_wors_likes_count = 0

    surveys = Survey.objects.filter(is_deleted=0)
    surveys_count = Survey.objects.all().count()
    for survey in surveys:
        sum_ages += survey.age

    oldest_person = surveys = Survey.objects.filter(is_deleted=0).order_by('-age')
    youngest_person = surveys = Survey.objects.filter(is_deleted=0).order_by('age')
    
    fav_foods = Survey.objects.filter(is_deleted=0).values('favourite_food')
    for food in fav_foods:
        if 'Pizza' in food['favourite_food']:
            pizza_likes_count += 1

        if 'Pasta' in food['favourite_food']:
            pasta_likes_count += 1

        if 'Pap and Wors' in food['favourite_food']:
            pap_and_wors_likes_count += 1

    eats_out_rating_total = 0
    eats_out_rating_total_diviser = 0

    eats_out_ratings = Survey.objects.filter(is_deleted=0).values('likes_to_eat_out')
    for rating in eats_out_ratings:
        eats_out_rating_total_diviser += eats_out_ratings.count()
        eats_out_rating_total+=rating['likes_to_eat_out']

    watch_movies_rating_total = 0
    watch_movies_rating_total_diviser = 0

    watch_movies_ratings = Survey.objects.filter(is_deleted=0).values('likes_to_watch_movies')
    for rating in watch_movies_ratings:
        watch_movies_rating_total_diviser += watch_movies_ratings.count()
        watch_movies_rating_total+=rating['likes_to_watch_movies']

    watch_tv_rating_total = 0
    watch_tv_rating_total_diviser = 0

    watch_tv_ratings = Survey.objects.filter(is_deleted=0).values('likes_to_watch_tv')
    for rating in watch_tv_ratings:
        watch_tv_rating_total_diviser += watch_tv_ratings.count()
        watch_tv_rating_total+=rating['likes_to_watch_tv']

    listens_to_radi_rating_total = 0
    listens_to_radi_rating_total_diviser = 0

    listens_to_radio_rating = Survey.objects.filter(is_deleted=0).values('likes_listening_to_radio')
    for rating in listens_to_radio_rating:
        listens_to_radi_rating_total_diviser += listens_to_radio_rating.count()
        listens_to_radi_rating_total+=rating['likes_listening_to_radio']

    return render(request, 'survey/survey_results.html', {
        'surveys': surveys_count,
        'average_age': round(sum_ages/ surveys_count, 1),
        'olderst_person': oldest_person[0].age,
        'youngest_person': youngest_person[0].age,
        'pizza_likes_percentage':round((pizza_likes_count / surveys_count)*100,1),
        'pasta_likes_percentage':round((pasta_likes_count / surveys_count)*100,1),
        'pap_and_wors_likes_percentage':round((pap_and_wors_likes_count / surveys_count)*100,1),
        'eats_out_average':round((eats_out_rating_total / eats_out_rating_total_diviser)*100,1),
        'average_watch_movies_rating':round((watch_movies_rating_total / watch_movies_rating_total_diviser)*100,1),
        'average_watch_tv_rating':round((watch_tv_rating_total / watch_tv_rating_total_diviser)*100,1),
        'average_listens_to_radio_rating':round((listens_to_radi_rating_total / listens_to_radi_rating_total_diviser)*100,1),
    })

def submit_survey(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            post =form.save(commit=False)
            post.is_deleted = 0
            fav_foods = request.POST.getlist('favourite_food')
            post.favourite_food = ', '.join(fav_foods)
            post.save()
            messages.success(request, 'Thank you for taking the time to complete this survey')
            return redirect('survey')
        
        else:
            form_errors = ''
            for error in form.errors.values():
                form_errors+=error

            messages.warning(request, form_errors)
            return redirect('take_survey')
    else:
        messages.warning(request, 'Invalid request')
        return redirect('take_survey')