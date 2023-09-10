
import tensorflow as tf
from keras.models import load_model
from .data_analysis import analyze_data

class DeckGenerator:
    def __init__(self, influencer_data, brand_requirements):
        self.influencer_data = influencer_data
        self.brand_requirements = brand_requirements
        self.model = load_model('path_to_model')

    def preprocess_data(self):
        # Preprocess the data for the model
        self.influencer_data = analyze_data(self.influencer_data, self.brand_requirements)

    def generate_deck(self):
        self.preprocess_data()
        prediction = self.model.predict(self.influencer_data)
        return self.create_deck(prediction)

    def create_deck(self, prediction):
        # Create a pitch deck based on the prediction
        deck = {
            'title': 'Influencer Marketing Pitch Deck',
            'slides': [
                {
                    'title': 'Influencer Overview',
                    'content': self.influencer_data
                },
                {
                    'title': 'Brand Requirements',
                    'content': self.brand_requirements
                },
                {
                    'title': 'Proposed Collaboration',
                    'content': prediction
                }
            ]
        }
        return deck
