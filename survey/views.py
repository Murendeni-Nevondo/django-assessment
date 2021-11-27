from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'survey/index.html', {
        'name': 'Murendeni Nevondo'
    })


def take_survey(request):
    return render(request, 'survey/take_survey.html', {
        'name': 'Take Survey'
    })