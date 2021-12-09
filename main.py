import pygame
import pygame_gui


count = 0

screen_size_x = 1280
screen_size_y = 720

button_size_x = 50
button_size_y = 50

pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((screen_size_x, screen_size_y))

background = pygame.Surface((screen_size_x, screen_size_y))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((screen_size_x, screen_size_y), 'theme.json')


class Fighter(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = pygame.image.load('sprites/meowx/Terran/Destroyer/96 X 60.png').convert_alpha()

    def image_at(self, rectangle):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)


all_sprites = pygame.sprite.Group()
image_coor = (50,50,100,100)
player = Fighter.image_at(image_coor)
all_sprites.add(player)

hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    ((screen_size_x // 2) - 100, 0), (button_size_x, button_size_y)),
    text='Hi!',
    manager=manager)

subtract_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    ((screen_size_x // 2) - 50, 0), (button_size_x, button_size_y)),
    text='-1',
    manager=manager)

add_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    ((screen_size_x // 2) + 0, 0), (button_size_x, button_size_y)),
    text='+1',
    manager=manager)

total_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    ((screen_size_x // 2) + 50, 0), (button_size_x, button_size_y)),
    text=f'{count}',
    manager=manager)

text_window = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
    ((screen_size_x // 2) - 200, (screen_size_y // 2) - 25), (400, 50)),
    text=f'This is will display the input.' ,
    manager=manager)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0

    all_sprites.draw(background)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == hello_button:
                    text_window.set_text('Hello World!')
                elif event.ui_element == subtract_button:
                    count -= 1
                    total_button.set_text(f'{count}')
                    text_window.set_text('Subtracting...')
                elif event.ui_element == add_button:
                    count += 1
                    total_button.set_text(f'{count}')
                    text_window.set_text('Adding...')
                elif event.ui_element == total_button:
                    text_window.set_text(f'This is the current count: {count}')

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
