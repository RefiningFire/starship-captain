import pygame

class Background():
    def __init__(self):
        self.bg_img = pygame.image.load('sprites/Starfield.png')
        self.bg_img_rect = self.bg_img.get_rect()

        self.bg_origin1_x = 0
        self.bg_origin1_y = 0

        self.bg_origin2_x = 0
        self.bg_origin2_y = self.bg_img_rect.height

        self.bg_origin3_x = self.bg_img_rect.width
        self.bg_origin3_y = 0

        self.bg_origin4_x = self.bg_img_rect.width
        self.bg_origin4_y = self.bg_img_rect.height

    def update(self, player_movement_x, player_movement_y):
        self.player_movement_x = player_movement_x
        self.player_movement_y = player_movement_y

        self.bg_origin1_x -= player_movement_x
        self.bg_origin2_x -= player_movement_x
        self.bg_origin3_x -= player_movement_x
        self.bg_origin4_x -= player_movement_x

        self.bg_origin1_y += player_movement_y
        self.bg_origin2_y += player_movement_y
        self.bg_origin3_y += player_movement_y
        self.bg_origin4_y += player_movement_y

        if self.bg_origin1_x <= -self.bg_img_rect.width:
            self.bg_origin1_x = self.bg_img_rect.width
        elif self.bg_origin1_x >= self.bg_img_rect.width:
            self.bg_origin1_x = -self.bg_img_rect.width

        if self.bg_origin2_x <= -self.bg_img_rect.width:
            self.bg_origin2_x = self.bg_img_rect.width
        elif self.bg_origin2_x >= self.bg_img_rect.width:
            self.bg_origin2_x = -self.bg_img_rect.width

        if self.bg_origin3_x <= -self.bg_img_rect.width:
            self.bg_origin3_x = self.bg_img_rect.width
        elif self.bg_origin3_x >= self.bg_img_rect.width:
            self.bg_origin3_x = -self.bg_img_rect.width

        if self.bg_origin4_x <= -self.bg_img_rect.width:
            self.bg_origin4_x = self.bg_img_rect.width
        elif self.bg_origin4_x >= self.bg_img_rect.width:
            self.bg_origin4_x = -self.bg_img_rect.width

        if self.bg_origin1_y <= -self.bg_img_rect.height:
            self.bg_origin1_y = self.bg_img_rect.height
        elif self.bg_origin1_y >= self.bg_img_rect.height:
            self.bg_origin1_y = -self.bg_img_rect.height

        if self.bg_origin2_y <= -self.bg_img_rect.height:
            self.bg_origin2_y = self.bg_img_rect.height
        elif self.bg_origin2_y >= self.bg_img_rect.height:
            self.bg_origin2_y = -self.bg_img_rect.height

        if self.bg_origin3_y <= -self.bg_img_rect.height:
            self.bg_origin3_y = self.bg_img_rect.height
        elif self.bg_origin3_y >= self.bg_img_rect.height:
            self.bg_origin3_y = -self.bg_img_rect.height

        if self.bg_origin4_y <= -self.bg_img_rect.height:
            self.bg_origin4_y = self.bg_img_rect.height
        elif self.bg_origin4_y >= self.bg_img_rect.height:
            self.bg_origin4_y = -self.bg_img_rect.height


    def render(self, background):
        background.blit(self.bg_img, (self.bg_origin1_x, self.bg_origin1_y))
        background.blit(self.bg_img, (self.bg_origin2_x, self.bg_origin2_y))
        background.blit(self.bg_img, (self.bg_origin3_x, self.bg_origin3_y))
        background.blit(self.bg_img, (self.bg_origin4_x, self.bg_origin4_y))
