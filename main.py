import pygame
import pygame_gui
from spritesheet import Spritesheet

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




my_spritesheet = Spritesheet('sprites/meowx/Terran/Fighter/40 X 32.png')

fighter_loc_x = 200
fighter_loc_y = 200

fighter = [my_spritesheet.parse_sprite('fighter1.png'),                 my_spritesheet.parse_sprite('fighter2.png'),    my_spritesheet.parse_sprite('fighter3.png'), my_spritesheet.parse_sprite('fighter4.png'), my_spritesheet.parse_sprite('fighter5.png'), my_spritesheet.parse_sprite('fighter6.png'),
my_spritesheet.parse_sprite('fighter7.png'),
my_spritesheet.parse_sprite('fighter8.png'),
my_spritesheet.parse_sprite('fighter9.png'),

my_spritesheet.parse_sprite('fighter10.png'),
my_spritesheet.parse_sprite('fighter11.png'),
my_spritesheet.parse_sprite('fighter12.png'),
my_spritesheet.parse_sprite('fighter13.png'),
my_spritesheet.parse_sprite('fighter14.png'),
my_spritesheet.parse_sprite('fighter15.png'),
my_spritesheet.parse_sprite('fighter16.png'),
my_spritesheet.parse_sprite('fighter17.png'),
my_spritesheet.parse_sprite('fighter18.png'),

my_spritesheet.parse_sprite('fighter19.png'),
my_spritesheet.parse_sprite('fighter20.png'),
my_spritesheet.parse_sprite('fighter21.png'),
my_spritesheet.parse_sprite('fighter22.png'),
my_spritesheet.parse_sprite('fighter23.png'),
my_spritesheet.parse_sprite('fighter24.png'),
my_spritesheet.parse_sprite('fighter25.png'),
my_spritesheet.parse_sprite('fighter26.png'),
my_spritesheet.parse_sprite('fighter27.png'),

my_spritesheet.parse_sprite('fighter28.png'),
my_spritesheet.parse_sprite('fighter29.png'),
my_spritesheet.parse_sprite('fighter30.png'),
my_spritesheet.parse_sprite('fighter31.png'),
my_spritesheet.parse_sprite('fighter32.png'),
my_spritesheet.parse_sprite('fighter33.png'),
my_spritesheet.parse_sprite('fighter34.png'),
my_spritesheet.parse_sprite('fighter35.png'),
my_spritesheet.parse_sprite('fighter36.png')]

index = 0


clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                index = (index + 1) % len(fighter)
            elif event.key == pygame.K_LEFT:
                index = (index - 1) % len(fighter)
            if event.key == pygame.K_UP:
                fighter_loc_x += 1
            elif event.key == pygame.K_DOWN:
                fighter_loc_x -= 1


        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == hello_button:
                    text_window.set_text('Hello World!')
                elif event.ui_element == subtract_button:
                    count -= 1s
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
    background.fill((0, 0, 0))
    background.blit(fighter[index], (fighter_loc_x, fighter_loc_y))
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
