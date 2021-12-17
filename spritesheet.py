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
    def set_stats(self, mass, manuverability, acceleration, speed, rotation_momentum=0.0, forward_momentum=0.0, current_rotation=0, current_direction=0, slow_turn_counter=0):
        self.mass = mass
        self.manuverability = manuverability
        self.acceleration = acceleration
        self.speed = speed

        self.rotation_momentum = rotation_momentum
        self.forward_momentum = forward_momentum
        self.current_rotation = current_rotation
        self.current_direction = current_direction

        self.slow_turn_counter = slow_turn_counter

    def make_turn(self, passed_rotation):

        # If momentum is in opposite direction of powered movement, decrease the turning momentum, but keep turning in the direction of momentum.
        if passed_rotation != self.current_rotation:
            self.rotation_momentum -= self.manuverability / math.sqrt(self.mass)

        # Checks for a slow turner. Must use incrementing because modulo in self.frame_index turning doesn't work.
        if self.slow_turn_counter < 1 and self.rotation_momentum < 1:
            self.slow_turn_counter += self.rotation_momentum

        # If rotation_momentum is fast enough execute normal turn.
        elif self.rotation_momentum >= 1:
            self.frame_index = (self.frame_index + int(self.current_rotation * self.rotation_momentum)) % len(self.sheet)

            self.slow_turn_counter = 0

        # if continuing in same direction, & a slow turner, execute a slow turn.
        else:
            self.frame_index = (self.frame_index + int(self.current_rotation * self.slow_turn_counter)) % len(self.sheet)

            self.slow_turn_counter = 0

    def powered_turn(self, passed_rotation):
        # A new turn from 0 or continuing along with rotation_momentum
        if passed_rotation == self.current_rotation or self.current_rotation == 0:

            # Increase momentum because of powered turn.
            if self.rotation_momentum < self.manuverability:
                self.rotation_momentum += self.manuverability / math.sqrt(self.mass)

            self.make_turn(passed_rotation)

            # This keeps momentum going in the same direction.
            self.current_rotation = passed_rotation

        elif self.rotation_momentum > 0:
            self.make_turn(passed_rotation)
        elif self.rotation_momentum <= 0:
            self.current_rotation = 0
        else:
            print('powered_turn else statement triggered')



    def make_move(self, passed_direction):

        # If momentum is in opposite direction of powered movement, decrease the forward_momentum, but keep moving in the direction of momentum.
        if passed_direction != self.current_direction:
            self.forward_momentum -= (self.acceleration + self.manuverability) / math.sqrt(self.mass)

        # Set the change this frame as a separate variable, so that other parts like the moving background can more easily access it.
        self.change_x = (self.forward_momentum * math.sin(math.radians(self.frame_index)) * self.current_direction)
        self.change_y = (self.forward_momentum * math.cos(math.radians(self.frame_index)) * self.current_direction)

        # Move in the direction of forward_momentum.
        self.loc_x += self.change_x
        self.loc_y -= self.change_y

    def powered_move(self, passed_direction):
        # A new move from 0 or continuing along with forward_momentum.
        if passed_direction == self.current_direction or self.current_direction == 0:
            # Increase momentum because of powered move, up to max speed.
            if self.forward_momentum < self.speed:
                self.forward_momentum += self.acceleration / math.sqrt(self.mass)

            self.make_move(passed_direction)

            # This keeps momentum going in the same direction.
            self.current_direction= passed_direction

        elif self.forward_momentum > 0:
            self.make_move(passed_direction)
        elif self.forward_momentum <= 0:
            self.current_direction = 0
            self.forward_momentum = 0
        else:
            print('powered_move else statement triggered')
