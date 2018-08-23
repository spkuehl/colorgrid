from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.core import serializers
import numpy
import json

def random_integer_array(request, perfect_square):
    random_list = []
    if perfect_square < 2:
        return HttpResponseNotFound('<h1>Page not found.</h1>')
    for i in range(perfect_square):
        row = []
        for j in range(perfect_square):
            row.append(list(numpy.random.randint(255, size=3)))
        random_list.append(row)
    return render(request, 'color_grid/grid.html',
        {'random_list': random_list,
         'flat_random_list': [num for elem in random_list for num in elem]})
         # List comprehension above flattens the 3d list to 2d for rotation.js
