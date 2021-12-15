import pygame
import pygame_gui
import math
from spritesheet import Spritesheet, Starship

void_drag = 100 # To give empty space a feeling of heft and resistance.

count = 0

FPS = 60
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




player_ship = Starship('Terran','fighter','sprites/meowx/Terran/Fighter/40 X 32.png')

fighter_ship = (10.5,2.3,0.8,10.0)
carrier_ship = (100000,0.3,0.4,2.4)

player_ship.set_stats(*carrier_ship
 # Mass, measured in tons? F-16 10.5 tons, Carrier 101,196 tons
 # manuverability, RPM? F-16 180 in 13 sec (2.3 rpm), Carrier 3-5 min (0.3 - 0.2)
 # acceleration, how quickly can reach speed.
 # Speed

 # rotation_momentum=0.0
 # forward_momentum=0.0
 # current_rotation=0
 # current_direction=0
 # slow_turn_counter=0
)

# Create the players ship(index, loc_x, loc_y)
player_sprite = player_ship.set_frame_sheet(90, 200, 100)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0

    keys = pygame.key.get_pressed()  #checking pressed keys
    if keys[pygame.K_RIGHT]:
        player_ship.powered_turn(1)
    elif keys[pygame.K_LEFT]:
        player_ship.powered_turn(-1)
    elif player_ship.rotation_momentum > 0:
        player_ship.make_turn(player_ship.current_rotation)
        # Larger ships take longer to slow down, mitigated by manuverability and void_drag
        player_ship.rotation_momentum -= player_ship.manuverability / math.sqrt(player_ship.mass)
    elif player_ship.rotation_momentum < 0:
        player_ship.rotation_momentum, player_ship.slow_turn_counter = 0, 0


    if keys[pygame.K_UP]:
        #player_ship.power_forward()
        player_ship.powered_move(1)
    elif keys[pygame.K_DOWN]:
        #player_ship.move_backward()
        player_ship.powered_move(-1)
    elif player_ship.forward_momentum > 0:

        # Larger ships take longer to slow down, mitigated by manuverability and void_drag
        # If no forward power is applied, but there is still forward_momentum, slow the ship down.
        player_ship.forward_momentum -= player_ship.manuverability / math.sqrt(player_ship.mass)

        player_ship.make_move(player_ship.current_direction)

    elif player_ship.forward_momentum < 0:
        player_ship.forward_momentum = 0


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
    background.blit(player_sprite[player_ship.frame_index], (player_ship.loc_x, player_ship.loc_y))
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
    clock.tick(FPS)
