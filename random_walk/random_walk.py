#!/usr/bin/python

import random;
import png;

rows = 250;
cols = 250;
canvas = [];
total_particles = 1000;
occupied_value = 255;

def init():
	random.seed();
	for i in range(rows):
		canvas.append([0]*cols);

def print_canvas():
	for i in range(rows):	
		for j in range(cols):
			print(canvas[i][j]),;
		print("\n");

def set_canvas_location(x, y, value):
	canvas[x][y] = value;

def check_location_neighbours(x, y):
	x_max = x+2;
	x_min = x-1;
	y_max = y+2;
	y_min = y-1;

	if (x_max > rows):
		x_max = rows;
	if (y_max > cols):
		y_max = cols;
	if (x_min < 0):
		x_min = 0;
	if (y_max < 0):
		y_min = 0; 

	for i in range(x_min,x_max,1):
		for j in range(y_min,y_max,1):
			if (canvas[i][j] > 0):
				return True;
	return False;

def check_within_bounds(x,y):
	return (x > 0 and x < rows and y > 0 and y < cols);

def write_to_file(filename):
	file_handle = open(filename,'wb');
	png_writer = png.Writer(rows,cols,greyscale=True);
	png_writer.write(file_handle,canvas);
	file_handle.close();

curr_x = 0;
curr_y = 0;
particles_completed = 0;

init();
set_canvas_location(120,80,occupied_value);
set_canvas_location(120,160,occupied_value);

while (particles_completed < total_particles):
	curr_x = random.randint(0,rows);
	curr_y = random.randint(0,cols);
	while (check_within_bounds(curr_x,curr_y)):
		if (check_location_neighbours(curr_x,curr_y)):
			print ("Point %d anchored" % particles_completed);
			set_canvas_location(curr_x,curr_y,occupied_value);
			particles_completed += 1;
			break;
		curr_x += random.randint(-1,1);
		curr_y += random.randint(-1,1);
write_to_file("test.png");
