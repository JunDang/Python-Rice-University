L = [0, 1]
 
for i in range(0,40):
    #print L[-2:]
    v = sum(L[-2:])
    #print v
    L.append(v)
print L

print 4//3

d = {'a':'m', True: 'n'}
print d
#####
a = {}
a['c'] = [1, 2]
for key, value in a.items():
    print key
    print value
    
def is_even(number):
    """Returns whether the number is even."""
    return number % 2 == 0
l=  [1, 2, 3, 4, 5]
print [is_even(number) for number in l]

####
# Demonstration of a magnifier on a map

import simplegui

# 1521x1818 pixel map of native American language
# source - Gutenberg project

image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/alphatest.png")


# Draw map and magnified region
def draw(canvas):
    # Draw map
    canvas.draw_image(image, 
            [220, 100], [100, 100], 
            [100, 100], [200, 200])

    
    
# Create frame for scaled map
frame = simplegui.create_frame("Map magnifier", 200, 200)

# register even handlers
  
frame.set_draw_handler(draw)

# Start frame
frame.start()
