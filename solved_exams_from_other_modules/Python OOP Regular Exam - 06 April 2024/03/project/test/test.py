from unittest import TestCase
from project.social_media import SocialMedia


class TestSocialMedia(TestCase):
    def test_init(self):
        social_media = SocialMedia('suffer', 'Twitter', 10, 'Глупости')
        self.assertEqual(social_media._username, 'suffer')
        self.assertEqual(social_media._platform, 'Twitter')
        self.assertEqual(social_media._followers, 10)
        self.assertEqual(social_media._content_type, 'Глупости')
        self.assertEqual(social_media._posts, [])

    def test_platforms(self):
        allowed_platforms = ['Instagram', 'YouTube', 'Twitter']
        with self.assertRaises(ValueError) as ex:
            social_media = SocialMedia('suffer', 'Facebook', 10, 'Глупости')
        self.assertEqual("Platform should be one of ['Instagram', 'YouTube', 'Twitter']", str(ex.exception))

    def test_create_post(self):
        social_media = SocialMedia('suffer', 'Twitter', 10, 'Глупости')
        self.assertEqual(social_media.create_post('post'), "New Глупости post created by suffer on Twitter.")
        self.assertEqual(social_media._posts, [{'content': 'post', 'likes': 0, 'comments': []}])

    def test_followers_invalid(self):
        test = SocialMedia('suffer', 'Twitter', 0, 'Глупости')
        with self.assertRaises(ValueError) as ex:
            test._followers -= 1
        self.assertEqual("Followers cannot be negative.", str(ex.exception))