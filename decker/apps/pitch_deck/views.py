
from django.shortcuts import render
from .models import PitchDeck
from .ai.data_analysis import analyze_data
from .ai.deck_generator import generate_deck

def create_deck(request):
    if request.method == 'POST':
        influencer_data = request.POST.get('influencer_data')
        brand_requirements = request.POST.get('brand_requirements')

        analysis_result = analyze_data(influencer_data, brand_requirements)
        deck = generate_deck(analysis_result)

        new_deck = PitchDeck.objects.create(
            user=request.user,
            deck=deck
        )
        new_deck.save()

        return render(request, 'pitch_deck/view_deck.html', {'deck': new_deck})

    return render(request, 'pitch_deck/create_deck.html')

def view_deck(request, deck_id):
    deck = PitchDeck.objects.get(id=deck_id)
    return render(request, 'pitch_deck/view_deck.html', {'deck': deck})
