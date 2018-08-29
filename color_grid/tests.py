from django.test import TestCase, Client
import color_grid.views as views
from django.http import HttpRequest
from django.urls import reverse


class TestRandomIntegerArrayView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_response_200(self):
        response = self.client.get(reverse('colorgrid', kwargs={'perfect_square': 2}))
        self.assertEqual(response.status_code, 200)

    def test_page_returns_404_less_than_2(self):
        response = self.client.get(reverse('colorgrid', kwargs={'perfect_square': 0}))
        self.assertEqual(response.status_code, 404)

    def test_correct_length_of_random_list(self):
        response = self.client.get(reverse('colorgrid', kwargs={'perfect_square': 3}))
        self.assertEqual(sum(len(x) for x in response.context['random_list']), 9)

    def test_correct_length_of_flat_random_list(self):
        response = self.client.get(reverse('colorgrid', kwargs={'perfect_square': 4}))
        self.assertEqual(len(response.context['flat_random_list']), 16)

    def test_template_renders_correct_table_cells(self):
        request = HttpRequest()
        response = views.random_integer_array(request,3)
        html = response.content.decode('utf8')
        self.assertEqual(html.count("<td class='random-color-cell'"), 9)

    def test_template_renders_correct_table_rows(self):
        request = HttpRequest()
        response = views.random_integer_array(request,3)
        html = response.content.decode('utf8')
        self.assertEqual(html.count("<tr>"), 3)


class TestCoiledRandomIntegerArrayView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_response_200(self):
        response = self.client.get(reverse('coiledcolorgrid', kwargs={'perfect_square': 2}))
        self.assertEqual(response.status_code, 200)

    def test_page_returns_404_less_than_2(self):
        response = self.client.get(reverse('coiledcolorgrid', kwargs={'perfect_square': 0}))
        self.assertEqual(response.status_code, 404)

    def test_correct_length_of_random_list(self):
        response = self.client.get(reverse('coiledcolorgrid', kwargs={'perfect_square': 3}))
        self.assertEqual(sum(len(x) for x in response.context['random_list']), 9)

    def test_correct_length_of_flat_random_list(self):
        response = self.client.get(reverse('coiledcolorgrid', kwargs={'perfect_square': 4}))
        self.assertEqual(len(response.context['flat_random_list']), 16)

    def test_correct_value_of_flat_coiled_cell_ids_even_perfect_square(self):
        response = self.client.get(reverse('coiledcolorgrid', kwargs={'perfect_square': 4}))
        self.assertEqual(response.context['flat_cell_ids'],
        [0,1,2,3,11,12,13,4,10,15,14,5,9,8,7,6])

    def test_correct_value_of_flat_coiled_cell_ids_odd_perfect_square(self):
        response = self.client.get(reverse('coiledcolorgrid', kwargs={'perfect_square': 3}))
        self.assertEqual(response.context['flat_cell_ids'],
        [0,1,2,7,8,3,6,5,4])

    def test_template_renders_correct_table_cells(self):
        request = HttpRequest()
        response = views.coiled_random_integer_array(request,3)
        html = response.content.decode('utf8')
        self.assertEqual(html.count("<td class='random-color-cell'"), 9)

    def test_template_renders_correct_table_rows(self):
        request = HttpRequest()
        response = views.coiled_random_integer_array(request,3)
        html = response.content.decode('utf8')
        self.assertEqual(html.count("<tr>"), 3)
