
from django.contrib import admin
from .models import PitchDeck, InfluencerData, BrandRequirement

# Register your models here.
@admin.register(PitchDeck)
class PitchDeckAdmin(admin.ModelAdmin):
    list_display = ('id', 'influencer', 'brand', 'created_at')

@admin.register(InfluencerData)
class InfluencerDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'influencer', 'followers', 'engagement_rate')

@admin.register(BrandRequirement)
class BrandRequirementAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'target_audience', 'budget')
