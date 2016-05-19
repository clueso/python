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
	return (x >= 0 and x < rows and y >= 0 and y < cols);

def write_to_image(filename, save_as_image):
	if (save_as_image == true):
		file_handle = open(filename,'wb');
		png_writer = png.Writer(rows,cols,greyscale=True);
		png_writer.write(file_handle,canvas);
		file_handle.close();

def get_start_point():
	for i in range(0,10):
		choose_side = random.random();
		one_side = random.random();
		if (choose_side < 0.5):
			if(one_side < 0.5):
				choose_col = 0;
			else:
				choose_col = cols - 1;
			choose_row = random.randint(0,rows-1);
		else:
			if(one_side < 0.5):
				choose_row = 0;
			else:
				choose_row = rows - 1;
			choose_col = random.randint(0,cols-1);
		if (canvas[choose_row][choose_col] != 255):
			return [choose_row, choose_col];
	return [-1, -1];

particles_completed = 0;

init();
set_canvas_location(120,80,occupied_value);
set_canvas_location(120,160,occupied_value);

while (particles_completed < total_particles):
	curr_loc = get_start_point();
	if (curr_loc[0] == -1 and curr_loc[1] == -1):
		print ("Could not get starting point");
		break;
	#print("Trying point x=%d, y=%d\n" % (curr_loc[0],curr_loc[1]));	
	while (check_within_bounds(curr_loc[0],curr_loc[1])):
		if (check_location_neighbours(curr_loc[0],curr_loc[1])):
			print ("Point %d anchored" % particles_completed);
			set_canvas_location(curr_loc[0],curr_loc[1],occupied_value);
			particles_completed += 1;
			break;
		curr_loc[0] += random.randint(-1,1);
		curr_loc[1] += random.randint(-1,1);

write_to_image("test.png", true);
