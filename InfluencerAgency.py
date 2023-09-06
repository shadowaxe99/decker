class InfluencerAgency:
    def __init__(self, influencers):
        self.influencers = influencers

    def generate_pitch_decks(self, pitch_deck_generator):
        for influencer in self.influencers:
            influencer.generate_pitch_deck(pitch_deck_generator)