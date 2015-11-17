import png;

s = list([[255,255,0],[0,255,255],[0,0,0],[0,0,255]]);

f = open("test.png", 'wb');
w = png.Writer(3,4,greyscale=True);
w.write(f,s);
f.close();
