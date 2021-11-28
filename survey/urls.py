# survy urls
from django.urls import path
from . import views

urlpatterns = [
    path('survey',views.index,name='survey'),
    path('take_survey',views.take_survey,name='take_survey'),
    path('submit_answers',views.submit_survey,name='submit_answers')
]