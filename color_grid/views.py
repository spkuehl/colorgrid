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
         'flat_cell_ids': [i for i in range(perfect_square**2)],
         'flat_random_list': [num for elem in random_list for num in elem]})
         # List comprehension above flattens the 3d list to 2d for rotation.js


def coiled_random_integer_array(request, perfect_square):
    random_list = []
    if perfect_square < 2:
        return HttpResponseNotFound('<h1>Page not found.</h1>')
    coiled_matrix = [ [0] * perfect_square for _ in range(perfect_square)] # Make the zeroed matrix.
    first_row = 0
    last_row = perfect_square -1
    first_column = 0
    last_column = perfect_square -1
    x_index = 0
    y_index = 0
    counter = 0
    while True:
        while True:
            if x_index <= last_column: # North side of outermost unassigned portion of grid.
                coiled_matrix[first_row][x_index] = counter
                x_index += 1
                counter += 1
            elif y_index < last_row: # East side of outermost unassigned portion of grid.
                y_index += 1
                coiled_matrix[y_index][last_column] = counter
                counter += 1
            else: break # North and East outermost is done.
        x_index = last_column # Set x pointer to last row to prepare South and West assignments.
        y_index = last_row # Set y pointer to last row to prepare South and West assignments.
        first_row += 1 # Set first_row to the next unassaigned top row.
        last_column -= 1 # Set last_column to the next unassaigned top row.
        while True:
            if x_index > first_column: # South side of outermost unassigned portion of grid.
                x_index -= 1
                coiled_matrix[y_index][x_index] = counter
                counter += 1
            elif y_index > first_row: # West side of outermost unassigned portion of grid.
                y_index -= 1
                coiled_matrix[y_index][first_column] = counter
                counter += 1
            else: break # South and West outermost is done.
        last_row -= 1
        first_column += 1
        x_index = first_row # Set x pointer to first row to prepare North and East assignments.
        y_index = first_column # Set y pointer to first column to prepare North and East assignments.
        if first_row >= last_row and first_column >= last_column: # Repeats for next layer unless done or at the center of the grid.
            if perfect_square % 2 == 1: # Capture the center of odd perfect squares
                coiled_matrix[y_index][x_index] = counter # Assign center cell.
            break # Coil is done.

    for i in range(perfect_square):
        row = []
        for j in range(perfect_square):
            row.append(list(numpy.random.randint(255, size=3)))
        random_list.append(row)
    return render(request, 'color_grid/grid.html',
        {'random_list': random_list,
         'flat_cell_ids': [num for elem in coiled_matrix for num in elem],
         'flat_random_list': [num for elem in random_list for num in elem]})
         # List comprehension above flattens the 3d list to 2d for rotation.js
