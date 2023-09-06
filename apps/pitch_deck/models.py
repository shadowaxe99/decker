
from django.db import models
from django.contrib.auth.models import User

class Influencer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    followers = models.IntegerField()
    engagement_rate = models.FloatField()

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    target_audience = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PitchDeck(models.Model):
    influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deck_file = models.FileField(upload_to='pitch_decks/')

    def __str__(self):
        return f'{self.influencer.name} - {self.brand.name}'
