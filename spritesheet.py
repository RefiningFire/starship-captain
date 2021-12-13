import pygame
import json

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

    def frame_sheet(self,frame_index):
        self.frame_index = frame_index

        # Sheet = [self.parse_sprite(f'{self.name}1.png),       self.parse_sprite(f'{self.name}2.png'), self.parse_sprite(f'{self.name}3.png')] etc
        sheet = [self.parse_sprite(f'{self.name}{i+1}.png') for i in range(36)]
        return sheet

class Starship(Spritesheet):
    def set_stats(self, mass, momentum, acceleration, top_speed, current_speed):
        self.mass = mass
        self.momentum = momentum
        self.acceleration = acceleration
        self.top_speed = top_speed
        self.current_speed = current_speed

    def move_forward(self):
        pass
