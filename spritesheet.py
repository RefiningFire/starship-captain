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
    def set_stats(self, mass, handling, speed, current_handling=0.0, current_speed=0.0, current_direction=0):
        self.mass = mass
        self.handling = handling
        self.speed = speed

        self.current_handling = current_handling
        self.current_speed = current_speed
        self.current_direction = current_direction

    def make_turn(self, passed_direction):
        self.frame_index = (self.frame_index + int(passed_direction * self.current_handling)) % len(self.sheet)

        # This keeps momentum going in the same direction
        self.current_direction = passed_direction

    def powered_turn(self, passed_direction):
        self.make_turn(passed_direction)
        if self.current_handling < self.handling:
            self.current_handling += self.handling / self.mass


    def move_forward(self):
        self.loc_x += self.current_speed * math.sin(math.radians(self.frame_index))
        self.loc_y -= self.current_speed * math.cos(math.radians(self.frame_index))

    def move_backward(self):
        self.loc_x += self.current_speed * math.sin(math.radians(self.frame_index))
        self.loc_y -= self.current_speed * math.cos(math.radians(self.frame_index))

    def power_forward(self):
        self.move_forward()
        if self.current_speed < self.speed:
            self.current_speed += self.handling / self.mass
