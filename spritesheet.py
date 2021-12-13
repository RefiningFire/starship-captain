import pygame
import json

class Spritesheet:
    def __init__(self, name, filename):
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

    def frame_sheet(self):
        sheet = [self.parse_sprite(f'{self.name}{i+1}.png') for i in range(36)]

        '''  Long form of list comprehension above
        sheet2 = [
        self.parse_sprite(f'{self.name}1.png'),
        self.parse_sprite(f'{self.name}2.png'),
        self.parse_sprite(f'{self.name}3.png'),
        self.parse_sprite(f'{self.name}4.png'),
        self.parse_sprite(f'{self.name}5.png'),
        self.parse_sprite(f'{self.name}6.png'),
        self.parse_sprite(f'{self.name}7.png'),
        self.parse_sprite(f'{self.name}8.png'),
        self.parse_sprite(f'{self.name}9.png'),
        self.parse_sprite(f'{self.name}10.png'),
        self.parse_sprite(f'{self.name}11.png'),
        self.parse_sprite(f'{self.name}12.png'),
        self.parse_sprite(f'{self.name}13.png'),
        self.parse_sprite(f'{self.name}14.png'),
        self.parse_sprite(f'{self.name}15.png'),
        self.parse_sprite(f'{self.name}16.png'),
        self.parse_sprite(f'{self.name}17.png'),
        self.parse_sprite(f'{self.name}18.png'),
        self.parse_sprite(f'{self.name}19.png'),
        self.parse_sprite(f'{self.name}20.png'),
        self.parse_sprite(f'{self.name}21.png'),
        self.parse_sprite(f'{self.name}22.png'),
        self.parse_sprite(f'{self.name}23.png'),
        self.parse_sprite(f'{self.name}24.png'),
        self.parse_sprite(f'{self.name}25.png'),
        self.parse_sprite(f'{self.name}26.png'),
        self.parse_sprite(f'{self.name}27.png'),
        self.parse_sprite(f'{self.name}28.png'),
        self.parse_sprite(f'{self.name}29.png'),
        self.parse_sprite(f'{self.name}30.png'),
        self.parse_sprite(f'{self.name}31.png'),
        self.parse_sprite(f'{self.name}32.png'),
        self.parse_sprite(f'{self.name}33.png'),
        self.parse_sprite(f'{self.name}34.png'),
        self.parse_sprite(f'{self.name}35.png'),
        self.parse_sprite(f'{self.name}36.png')
        ]
        '''
        return sheet
