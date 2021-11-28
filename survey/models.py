from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Survey(models.Model):
    surname        = models.CharField(max_length=150, blank=False, null=False)
    first_names    = models.CharField(max_length=150, blank=False, null=False)
    contact_number = models.CharField(max_length=15, blank=False, null=False)
    age            = models.PositiveSmallIntegerField(validators=[MinValueValidator(5), MaxValueValidator(120)])
    date           = models.DateField()
    favourite_food = models.CharField(max_length=255)
    likes_to_eat_out         = models.PositiveSmallIntegerField(blank=False, null=False)
    likes_to_watch_movies    = models.PositiveSmallIntegerField(blank=False, null=False)
    likes_to_watch_tv        = models.PositiveSmallIntegerField(blank=False, null=False)
    likes_listening_to_radio = models.PositiveSmallIntegerField(blank=False, null=False)
    is_deleted     = models.BooleanField(default=0)

    def __str__(self) -> str:
        return self.first_names +' '+self.surname