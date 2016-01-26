# Takes input n and computes output named result

import simplegui

# global state

n = 0
#iteration = 0
#max_iterations = 10

# helper functions

def init(start):
    """Initializes n."""
    global n
    n = start
    print "Input is", n
    
def get_next(current):
    """???  Part of mystery computation."""
    if current % 2 ==0:
       return (current/ 2)
    else:
       return 3*current + 1


# timer callback

def update():
    """???  Part of mystery computation."""
    global n
    #iteration += 1
    # Stop iterating after max_iterations
    if n == 1:
        timer.stop()
        print "Output is", n
    else:
        n = get_next(n)
        print n

# register event handlners

timer = simplegui.create_timer(1, update)

# start program
init(217)
timer.start()
