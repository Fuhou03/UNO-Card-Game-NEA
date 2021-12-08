import pygame
from button import Button

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

user_rect = Button(210, 90, 140, 32)  # (x, y, width, height)
pass_rect = Button(210, 140, 140, 32)  # width becomes 200 later
# email_rect = Button(210, 190, 140, 32)
register_rect = Button(100, 210, 210, 32)
login_rect = Button(350, 210, 210, 32)

button_list = []  # So we can loop through all buttons easily
button_list.append(user_rect)
button_list.append(pass_rect)
button_list.append(register_rect)
button_list.append(login_rect)
# button_list.append(email_rect)


running = True
while running:
    screen.fill((0, 0, 0))  # Put it before you blit so it doesn't cover the text/images

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        mouse_pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in button_list:  # Goes through all buttons
                button.change_colour(mouse_pos)  # Colour of box will be grey until clicked on

        if event.type == pygame.KEYDOWN:  # Press a key
            for button in button_list:
                if button.active == True:  # If the button has been clicked on
                    button.get_text(screen, event)

    # Put labels onto screen
    username = font.render("Username", True, (255, 255, 255))
    screen.blit(username, (100, 100))
    password = font.render("Password", True, (255, 255, 255))
    screen.blit(password, (100, 150))
    register = font.render("Register", True, (255, 255, 255))
    screen.blit(register, (157, 217))
    login = font.render("Login", True, (255, 255, 255))
    screen.blit(login, (417, 217))
    # email = font.render("Email", True, (255, 255, 255))
    # screen.blit(email, (100, 200))

    for b in button_list:
        if b == register_rect or b == login_rect:
            b.draw2(screen)  # So it doesn't have the same functionalities as the text input boxes
        else:
            b.draw(screen)  # To put the rectangles onto the screen

    pygame.display.flip()
    clock.tick(60)
