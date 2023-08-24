import pygame
# Figuring out what to do:
#Need toggle button to take in one image, and change it with another
#if(buttondown press is done, function toggle(ex) will swap png of
# button with other png
#Parameters, need pos, image, self,

class ButtonToggle():
    def __init__(self, image, pos):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
        if self.image is None:
            self.image = self.text

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)

    def checkforInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeButton(self, image, screen):
        self.image = image
        screen.blit(self.image, self.rect)

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

