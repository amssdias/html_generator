from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.views.generic import RedirectView

from generator.views import GeneratorView

# Create your tests here.
class TestUrls(SimpleTestCase):

    def test_main_url_resolves(self):
        url = reverse('generator')
        no_path = '/'
        self.assertEqual(resolve(url).func.view_class, GeneratorView)
        self.assertEqual(resolve(no_path).func.view_class, RedirectView)
