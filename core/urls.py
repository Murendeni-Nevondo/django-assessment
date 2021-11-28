"""core URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from survey.views import index

urlpatterns = [
    path('', index, name='home'),
    path('home/', index, name='home'),
    path('', include("survey.urls")),
    path('admin/', admin.site.urls),
]


