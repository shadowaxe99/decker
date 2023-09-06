from django.core.management.base import BaseCommand
from myapp.social_media_integration import SocialMediaIntegration
from myapp.PitchDeck import PitchDeck


class Command(BaseCommand):
    help = 'Shares the pitch deck on social media'

    def handle(self, *args, **options):
        # Create a PitchDeck object
        pitch_deck = PitchDeck('http://example.com/pitch_deck.pdf')

        # Get the URL of the pitch deck
        url = pitch_deck.get_url()

        # Create a SocialMediaIntegration object
        from django.contrib.auth.models import User
        user = User.objects.get(username='michael.gruen9')
        smi = SocialMediaIntegration(user)

        # Share the pitch deck on social media
        smi.share_on_social_media(url, 'facebook')
        smi.share_on_social_media(url, 'twitter')