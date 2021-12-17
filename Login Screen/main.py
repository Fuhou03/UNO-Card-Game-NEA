import pygame
from button import Button
from login import Login

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

login = Login()
login.create_button_list()
#register = Register()

running = True
while running:
    screen.fill((0, 0, 0))  # Put it before you blit so it doesn't cover the text/images

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        mouse_pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in login.button_list:  # Goes through all buttons
                button.change_colour(mouse_pos)  # Colour of box will be grey until clicked on
                if button == login.register_rect:   # If they click on the register button
                    pass


        if event.type == pygame.KEYDOWN:  # Press a key
            for button in login.button_list:
                if button.active == True:  # If the button has been clicked on
                    button.get_text(screen, event)
    
    
    login.draw_label(screen)
    

    for b in login.button_list:
        if b == login.register_rect or b == login.login_rect:
            b.draw2(screen)  # So it doesn't have the same functionalities as the text input boxes
        else:
            b.draw(screen)  # To put the rectangles onto the screen

    pygame.display.flip()
    clock.tick(60)
