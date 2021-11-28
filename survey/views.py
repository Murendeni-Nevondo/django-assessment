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
    return render(request, 'survey/survey_results.html', {
        'name': 'Survey Results'
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