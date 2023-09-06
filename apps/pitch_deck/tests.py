
from django.test import TestCase
from .models import PitchDeck
from .ai import data_analysis, deck_generator

class PitchDeckModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        PitchDeck.objects.create(title='Test Deck', influencer='Test Influencer')

    def test_title_content(self):
        deck = PitchDeck.objects.get(id=1)
        expected_object_name = f'{deck.title}'
        self.assertEquals(expected_object_name, 'Test Deck')

class DataAnalysisTest(TestCase):
    def test_analyze_influencer_data(self):
        data = {'followers': 10000, 'engagement_rate': 5.0}
        result = data_analysis.analyze_influencer_data(data)
        self.assertIsNotNone(result)

class DeckGeneratorTest(TestCase):
    def test_generate_deck(self):
        influencer_data = {'followers': 10000, 'engagement_rate': 5.0}
        brand_requirements = {'target_audience': '18-24', 'campaign_goals': 'Brand Awareness'}
        result = deck_generator.generate_deck(influencer_data, brand_requirements)
        self.assertIsNotNone(result)
