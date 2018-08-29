# Color Grid #

Expose Django URL to Create a Color Grid. I chose to send the data formatted to the frontend in an rgb(x,y,z) format.

Have a frontend display the colors in a square grid. With the ability to rotate the cells in a clockwise and coiled clockwise manner.

Sample URLs:
  /coiledcolorgrid/7/
  /colorgrid/7/

## Requirements ##

Made with Python 3.7 and Django 2.1

Virtual Environment Recommended

pip install -r requirements.txt

python manage.py runserver

### TODO: ###
- [ ] Test jQuery functionality on rotation.js.
- [ ] Test runtime for big arrays, front and back.
- [ ] Reduce code repetition between random_integer_array and coiled_andom_integer_array.
- [ ] Refactor and optimize coiled algorithm in coiled_andom_integer_array view.
