import twitter
import facebook
from social_django.models import UserSocialAuth


class SocialMediaIntegration:
    def __init__(self, user):
        self.user = user

    def social_login(self, backend):
        try:
            social_user = UserSocialAuth.objects.get(user=self.user, provider=backend)
            return social_user
        except UserSocialAuth.DoesNotExist:
            return None

    def share_on_social_media(self, content, backend):
        social_user = self.social_login(backend)
        if social_user:
            if backend == 'twitter':
                api = twitter.Api(consumer_key='your-consumer-key',
                                  consumer_secret='your-consumer-secret',
                                  access_token_key=social_user.extra_data['access_token']['oauth_token'],
                                  access_token_secret=social_user.extra_data['access_token']['oauth_token_secret'])
                status = api.PostUpdate(content)
                return status
            elif backend == 'facebook':
                graph = facebook.GraphAPI(social_user.extra_data['access_token'])
                post_id = graph.put_wall_post(message=content)
                return post_id
        else:
            return 'User not logged in with ' + backend

    def fetch_data_from_social_media(self, backend):
        social_user = self.social_login(backend)
        if social_user:
            if backend == 'twitter':
                api = twitter.Api(consumer_key='your-consumer-key',
                                  consumer_secret='your-consumer-secret',
                                  access_token_key=social_user.extra_data['access_token']['oauth_token'],
                                  access_token_secret=social_user.extra_data['access_token']['oauth_token_secret'])
                statuses = api.GetUserTimeline(screen_name=social_user.username)
                return [s.text for s in statuses]
            elif backend == 'facebook':
                graph = facebook.GraphAPI(social_user.extra_data['access_token'])
                profile = graph.get_object('me')
                return profile
        else:
            return 'User not logged in with ' + backend