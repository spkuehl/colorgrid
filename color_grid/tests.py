from django.test import TestCase
import color_grid.views as views
from django.http import HttpRequest


class TestRandomIntegerArrayView(TestCase):
    def test_page_returns_404_less_than_2(self):
        request = HttpRequest()
        response = views.random_integer_array(request, 1)
        self.assertEqual(response.status_code, 404)

    def test_page_renders_correct_table_cells(self):
        request = HttpRequest()
        response = views.random_integer_array(request,3)
        html = response.content.decode('utf8')
        self.assertEqual(html.count("<td"), 9)
