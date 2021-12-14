import pygame
import json
import math

temp_fps = 60

class Spritesheet:
    def __init__(self, faction, name, filename):
        self.faction = faction
        self.name = name
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert()
        self.meta_data = self.filename.replace('png', 'json')
        with open(self.meta_data) as f:
            self.data = json.load(f)
        f.close()

    def get_sprite(self, x, y, w, h):
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprite_sheet,(0, 0),(x, y, w, h))
        return sprite

    def parse_sprite(self, pose):
        sprite = self.data['frames'][pose]['frame']
        x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = self.get_sprite(x, y, w, h)
        return image

    def set_frame_sheet(self,frame_index, loc_x, loc_y):
        self.frame_index = frame_index
        self.loc_x = loc_x
        self.loc_y = loc_y

        # Sheet = [self.parse_sprite(f'{self.name}1.png),       self.parse_sprite(f'{self.name}2.png'), self.parse_sprite(f'{self.name}3.png')] etc
        self.sheet = [self.parse_sprite(f'{self.name}{i}.png') for i in range(360)]
        return self.sheet

class Starship(Spritesheet):
    def set_stats(self, mass, manuverability, acceleration, speed, turning_momentum=0.0, foward_momentum=0.0, current_direction=0, slow_turn_counter=0):
        self.mass = mass
        self.manuverability = manuverability
        self.acceleration = acceleration
        self.speed = speed

        self.turning_momentum = turning_momentum
        self.foward_momentum = foward_momentum
        self.current_direction = current_direction

        self.slow_turn_counter = slow_turn_counter

    def make_turn(self, passed_direction):
        # First checks for a slow turner, and if true, it uses a counter incrementer so that turns "in between the turns" are tracked. Otherwise this fails, since the modulo operator cannot work with number that is less than one.
        if self.slow_turn_counter < 1 and self.turning_momentum < 1 and passed_direction == self.current_direction:
            self.slow_turn_counter += self.turning_momentum
        # If turning_momentum is fast enough execute normal turn.
        elif self.turning_momentum >= 1:
            self.frame_index = (self.frame_index + int(passed_direction * self.turning_momentum)) % len(self.sheet)
        # Turn 1 degree and reset slow_turn_counter.
        elif passed_direction != self.current_direction:

        else:
            self.frame_index = (self.frame_index + int(passed_direction * self.slow_turn_counter)) % len(self.sheet)
            self.slow_turn_counter = 0

    def powered_turn(self, passed_direction, void_drag):
        # A new turn from 0 or continuing along with turning_momentum
        if passed_direction == self.current_direction or self.current_direction == 0:
            self.make_turn(passed_direction)
            # This keeps momentum going in the same direction
            self.current_direction = passed_direction
        elif self.turning_momentum > 0:
            self.make_turn(passed_direction)
            self.turning_momentum -= self.manuverability / void_drag
        elif self.turning_momentum <= 0:
            self.current_direction = 0
        else:
            print('fourth option')

        if self.turning_momentum < self.manuverability:
            self.turning_momentum += self.manuverability / void_drag


    def move_forward(self):
        self.loc_x += self.foward_momentum * math.sin(math.radians(self.frame_index))
        self.loc_y -= self.foward_momentum * math.cos(math.radians(self.frame_index))

    def move_backward(self):
        self.loc_x += self.foward_momentum * math.sin(math.radians(self.frame_index))
        self.loc_y -= self.foward_momentum * math.cos(math.radians(self.frame_index))

    def power_forward(self, void_drag):
        self.move_forward()
        if self.foward_momentum < self.speed:
            self.foward_momentum += self.acceleration / void_drag
