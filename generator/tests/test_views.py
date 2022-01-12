from django.test import SimpleTestCase
from django.urls import reverse, resolve

# Create your tests here.
class TestUrls(SimpleTestCase):

    def setUp(self) -> None:
        self.generate = reverse("generator")
        self.html_content = {
            "page_title": "Some title",
            "main_title": "Main title",
            "header_paragraph": "",
            "section_title": "Section title",
            "section_paragraph": "",
            "link": ""
        }
        return super().setUp()

    def test_generator_GET(self):
        response = self.client.get(self.generate)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'generator/index.html')

    def test_generator_POST(self):
        response = self.client.post(self.generate, self.html_content)
        self.assertEqual(response.status_code, 200)