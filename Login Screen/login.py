import pygame
from button import Button

class Login():
    def __init__(self):
        # Creating the labels
        self.font = pygame.font.Font(None, 30)
        self.username_label = self.font.render("Username", True, (255, 255, 255))
        self.password_label = self.font.render("Password", True, (255, 255, 255))
        self.register_label = self.font.render("Register", True, (255, 255, 255))
        self.login_label = self.font.render("Login", True, (255, 255, 255))
        
   
        # Creating the rectangles
        self.user_rect = Button(210, 90, 140, 32)  # (x, y, width, height)
        self.pass_rect = Button(210, 140, 140, 32)  # width becomes 200 later
        #self.email_rect = Button(210, 190, 140, 32)
        self.register_rect = Button(100, 210, 210, 32)
        self.login_rect = Button(350, 210, 210, 32)
       
    def create_button_list(self):
        self.button_list = []  # So we can loop through all buttons easily
        self.button_list.append(self.user_rect)
        self.button_list.append(self.pass_rect)
        self.button_list.append(self.register_rect)
        self.button_list.append(self.login_rect)
        #self.button_list.append(self.email_rect)
 

    def draw_label(self, screen):
        # Put labels onto screen
        self.screen = screen
        screen.blit(self.username_label, (100, 100))
        screen.blit(self.password_label, (100, 150))
        screen.blit(self.register_label, (157, 217))
        screen.blit(self.login_label, (417, 217))
        #screen.blit(self.email, (100, 200))


class Register(Login):
    def __init__(self):
        super().__init__()
        self.email = self.font.render("Email", True, (255, 255, 255))

        


