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

starfield = pygame.image.load('sprites/Starfield.png')
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




my_spritesheet = Spritesheet('interceptor','sprites/meowx/Terran/Interceptor/32 X 24.png')
fighter = my_spritesheet.frame_sheet()

fighter_loc_x = 200
fighter_loc_y = 200

spritesheet_index = 0

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0

    keys = pygame.key.get_pressed()  #checking pressed keys
    if keys[pygame.K_RIGHT]:
        spritesheet_index = (spritesheet_index + 1) % len(fighter)
    if keys[pygame.K_LEFT]:
        spritesheet_index = (spritesheet_index - 1) % len(fighter)
    if keys[pygame.K_UP]:
        fighter_loc_y -= 3
    if keys[pygame.K_DOWN]:
        fighter_loc_y += 3

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
    background.fill((0, 0, 0))
    background.blit(starfield,(0,0))
    background.blit(fighter[spritesheet_index], (fighter_loc_x, fighter_loc_y))
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
