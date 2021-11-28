from django import forms
from django.db.models import fields

from .models import Survey

class SurveyForm(forms.ModelForm):
    surname        = forms.CharField(error_messages={'required': 'Please enter your surname'})
    first_names    = forms.CharField(error_messages={'required': 'Please enter your First Names'})
    contact_number = forms.CharField(error_messages={'required': 'Please enter your contact number'})
    age            = forms.IntegerField(required=True)
    date           = forms.DateField(required=True)
    favourite_food = forms.CharField(error_messages={'required': 'Please select atleast one favourite food'})
    likes_to_eat_out         = forms.IntegerField(error_messages={'required': 'Please choose rating'})
    likes_to_watch_movies    = forms.IntegerField(error_messages={'required': 'Please choose rating'})
    likes_to_watch_tv        = forms.IntegerField(error_messages={'required': 'Please choose rating'})
    likes_listening_to_radio = forms.IntegerField(error_messages={'required': 'Please choose rating'})

    class Meta:

        model = Survey

        fields = [
            'surname',        
            'first_names',    
            'contact_number', 
            'age',            
            'date',           
            'favourite_food', 
            'likes_to_eat_out',      
            'likes_to_watch_movies', 
            'likes_to_watch_tv',     
            'likes_listening_to_radio',
        ]