# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
width = 800
height = 600
dimen = (width, height)
initvel = 0.5
acc = 0.25
frict = 0.025
score = 0
lives = 3
time = 0
rotation = 0.05
missile_factor = 5.0
inputs = [(initvel, 0), (0, -rotation), (0, rotation)]
directions = ['up', 'left', 'right']
keyinput = {}
lives_pos = [10, 25]
score_pos = [width - 100, 25]
started = False
timer_tick = 0
draw_tick = 0

for dir in directions: 
    keyinput[simplegui.KEY_MAP[dir]] = inputs[directions.index(dir)]


# Class for image information
class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot1.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image1 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")
asteroid_image2 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_brown.png")
asteroid_image3 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blend.png")
asteroids = [asteroid_image1, asteroid_image2, asteroid_image3]

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image1 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_blue2.png")
explosion_image2 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_orange.png")
explosion_image3 = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")
explosions = [explosion_image1, explosion_image2, explosion_image3]

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

# Updating the ship image        
    def update(self):
        for index in range(2):
            vect = angle_to_vector(self.angle)
            if self.thrust: 
                ship_thrust_sound.play()
                self.vel[index] += acc * vect[index]
            
            self.vel[index] *= 1 - frict
            self.pos[index] += self.vel[index]
            self.pos[index] = self.pos[index] % dimen[index]    
                
        self.angle += self.angle_vel

# Shooting a missile
    def shoot(self, missile):        
        vect = angle_to_vector(self.angle)
        for ind in range(2): 
            missile.pos[ind] = self.radius * vect[ind] + self.pos[ind]
            missile.pos[ind] = missile.pos[ind] % dimen[ind]
            missile.vel[ind] = self.vel[ind] + missile_factor * vect[ind]
        missile_group.add(missile)
            
# Get the position
    def get_position(self):
        return self.pos
    
# Get the radius
    def get_radius(self):
        return self.radius
            
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
            sound.set_volume(0.3)
   
    def draw(self, canvas):
        global time
        if self.animated:
            canvas.draw_image(self.image, 
                [self.image_center[0] + self.age * self.image_size[0], 
                self.image_center[1]], self.image_size, self.pos, self.image_size)
        else:    
            canvas.draw_image(self.image, self.image_center, self.image_size, 
                self.pos, self.image_size, self.angle)

# Updating rocks/missile appearances
    def update(self):        
        for index in range(2):
            self.pos[index] += self.vel[index]
            self.pos[index] = self.pos[index] % dimen[index]
        
        self.angle += self.angle_vel
        self.age += 1
        if self.age < self.lifespan:
            return True
        else:
            return False
        
# Get the position
    def get_position(self):
        return self.pos
    
# Get the radius
    def get_radius(self):
        return self.radius
            
# Checking for collisions
    def collide(self, other_object):

        if dist(self.get_position(), other_object.get_position())\
            < self.get_radius() + other_object.get_radius():
                return True
        else:
                return False
        
# The key handlers for 'up', 'left', 'right', 'space'        
def keydown(key):
    
    if key in keyinput.keys():           
        if keyinput[key][1] == 0:
            vect = angle_to_vector(my_ship.angle)
            my_ship.thrust = True
            my_ship.image_center[0] += my_ship.image_size[0]
            for ind in range(2): my_ship.vel[ind] += keyinput[key][0] * vect[ind] 
        else:
            my_ship.angle_vel += keyinput[key][1] 
            
    if key == simplegui.KEY_MAP['space']:
        if started: my_ship.shoot(Sprite(my_ship.get_position(), [0, 0], 0, 0, missile_image, missile_info, missile_sound))
    
def keyup(key):
   
    if key == simplegui.KEY_MAP['space']:
        missile_sound.rewind()
    else:
        my_ship.angle_vel = 0
        if my_ship.thrust and keyinput[key][1] == 0: 
            my_ship.thrust = False
            my_ship.image_center[0] -= my_ship.image_size[0]
            ship_thrust_sound.rewind()
    
# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global started, lives, score, draw_tick, timer_tick
    center = [width / 2, height / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
        lives = 3
        score = 0
        draw_tick = timer_tick + 2
    
def draw(canvas):
    global time, lives, score, started, draw_tick
    global rock_group, missile_group, explosion_group
    
    # animiate background
    time += 1
    center = debris_info.get_center()
    size = debris_info.get_size()
    wtime = (time / 8) % center[0]
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [width/2, height/2], [width, height])
    canvas.draw_image(debris_image, [center[0]-wtime, center[1]], [size[0]-2*wtime, size[1]], 
                                [width/2+1.25*wtime, height/2], [width-2.5*wtime, height])
    canvas.draw_image(debris_image, [size[0]-wtime, center[1]], [2*wtime, size[1]], 
                                [1.25*wtime, height/2], [2.5*wtime, height])
    
    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [width/2, height/2], 
                          splash_info.get_size())
        rock_group = set([])
        explosion_group = set([])
        my_ship.pos = [width / 2, height / 2]
        my_ship.vel = [0, 0]
        my_ship.angle = 0
        missile_group = set([])
        soundtrack.rewind()
    else:
        # draw ship and sprites
        my_ship.draw(canvas)
        sprite_helper(rock_group, canvas)
        sprite_helper(missile_group, canvas)
        soundtrack.play()
    
        # update ship
        my_ship.update()
    
        # check for collisions with ship
        num_coll = group_collide(rock_group, my_ship)
        if num_coll > 0:
            lives -= 1
        if lives == 0: started = False
        score += group_group_collide(rock_group, missile_group)
        draw_tick += 1
        sprite_helper(explosion_group, canvas)
    
    # draw lives/score
    canvas.draw_text("Lives: " + str(lives), lives_pos, 20, "Silver")
    canvas.draw_text("Score: " + str(score), score_pos, 20, "Silver")
    
# timer handler that spawns a rock    
def rock_spawner():
    
    pos = my_ship.get_position()
    if len(rock_group) < 12 and started:
        while dist(pos, my_ship.get_position()) < 3.0 * my_ship.get_radius():
            pos = []
            vel = []
            for ind in range(2): 
                pos.append(random.random() * dimen[ind])
                vel.append((5.0 + score/5.0)* (random.random() - initvel) * initvel)
        
        angle_vel = 3.0 * rotation * (random.random() - initvel)    
        astype = random.randrange(0, 3)
        rock_group.add(Sprite(pos, vel, 0, angle_vel, asteroids[astype], asteroid_info))
    
def sprite_helper(set_sprites, canvas):    
    for sprite in set_sprites:
        sprite.draw(canvas)
        removal = sprite.update()
        if not removal: set_sprites.remove(sprite)
        
def group_collide(set_sprites, other_object):
    num_coll = 0
    for coll in set_sprites:
        if coll.collide(other_object): 
            num_coll += 1
            set_sprites.remove(coll)
            expltype = random.randrange(0, 3)
            explosion_group.add(Sprite(coll.get_position(), [0, 0], 0, 0, 
                explosions[expltype], explosion_info, explosion_sound))
    return num_coll

def group_group_collide(set_sprites, set_others):
    
    num_hits = 0
    for hit in set_others:
        num_hits += group_collide(set_sprites, hit)
        if num_hits > 0: set_others.remove(hit)
    
    return num_hits
        
def check():
    global draw_tick, timer_tick, started
    
    if started: 
        timer_tick += 1
        frame_timer.start()
    
    if timer_tick > draw_tick:
        soundtrack.pause()
        frame_timer.stop()
    else:
        timer_tick = draw_tick
    
# initialize frame
frame = simplegui.create_frame("Asteroids", width, height)

# initialize ship
my_ship = Ship([width / 2, height / 2], [0, 0], 0, ship_image, ship_info)

# initialize rock group
rock_group = set([])

# initialize missile group
missile_group = set([])

# initialize explosion group
explosion_group = set([])

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)

rock_timer = simplegui.create_timer(1000.0, rock_spawner)
frame_timer = simplegui.create_timer(19.0, check)

# get things rolling
rock_timer.start()
frame_timer.start()
frame.start()