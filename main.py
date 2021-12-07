import pygame
import pygame_gui

count = 0

pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600), 'theme.json')

hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    (250, 275), (100, 50)),
    text='Say Hello',
    manager=manager)

bye_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    (450, 275), (100, 50)),
    text='Say Bye-Bye',
    manager=manager)

add_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    (250, 375), (100, 50)),
    text='Add One',
    manager=manager)

total_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(
    (450, 375), (100, 50)),
    text='Print Count',
    manager=manager)

text_window = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(
    (250, 100), (300, 50)),
    text=f'This is will display the input.' ,
    manager=manager)


clock = pygame.time.Clock()
is_running = True


while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == hello_button:
                    text_window.set_text('Hello World!')
                elif event.ui_element == bye_button:
                    text_window.set_text('Bye Bye.')
                elif event.ui_element == add_button:
                    count += 1
                    text_window.set_text('Adding...')
                elif event.ui_element == total_button:
                    text_window.set_text(f'This is the current count: {count}')

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
