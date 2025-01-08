from django.test import TestCase
from django.urls import reverse
from ..common.models import Song

from django.test import TestCase
from django.urls import reverse
# DJANGO_SETTINGS_MODULE = "C:\\Users\\eng_s\\Documents\\Learning\\Django\\karaoke\\karaoke\\karaoke\\settings.py"

class SongsViewTest(TestCase):
    def test_songs_list_view(self):
        response = self.client.get(reverse('songs_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_app/songs_list.html')

