import pygame
import ntpath
"""
Each button is a class.
The button will be in circular in  shape.
Equation of circle is then given by x^2+y^2 = r^2
"""
black = (255,255,255)
class Circle:
    def __init__(self,screen,x,y,radius,width = 3,color = (255,255,255)): #If width = 0 circle fills
        self.screen = screen
        self.x = x
        self.y = y
        self.radius = radius
        self.width = width
        self.color = color

    def draw(self):
        pygame.draw.circle(self.screen,self.color,(self.x,self.y),self.radius,self.width)

    def click(self):
        """
            In general, point x and y must satisfy (x - center_x)^2 + (y - center_y)^2 <= radius^2
        """
        current_mouse_position = pygame.mouse.get_pos()
        value_of_equation_at_current_mouse_position = (current_mouse_position[0]-self.x)**2+(current_mouse_position[1]-self.y)**2
        if (value_of_equation_at_current_mouse_position <= self.radius**2):
            if pygame.mouse.get_pressed()[0]:
                return True
        else:
            return False

class Play(Circle):
    def draw(self):
        pygame.draw.lines(self.screen,black,True, [(self.x+10,self.y),(self.x-10,self.y-10),(self.x-10,self.y+10)],2)

class Pause(Circle):
    def draw(self):
        pygame.draw.lines(self.screen,black,True, [(self.x-10,self.y-10),(self.x-10,self.y+10)],2)
        pygame.draw.lines(self.screen,black,True, [(self.x+10,self.y-10),(self.x+10,self.y+10)],2)

class Next(Circle):
    def draw(self):
        pygame.draw.lines(self.screen,black,False,[(self.x,self.y),(self.x-10,self.y-10)],3)
        pygame.draw.lines(self.screen,black,False,[(self.x,self.y),(self.x-10,self.y+10)],3)

class Previous(Circle):
    def draw(self):
        pygame.draw.lines(self.screen,black,False,[(self.x,self.y-10),(self.x-10,self.y)],3)
        pygame.draw.lines(self.screen,black,False,[(self.x-10,self.y),(self.x,self.y+10)],3)
    

class Add(Circle):
    def draw(self):
        pygame.draw.lines(self.screen,black,False,[(self.x,self.y-10),(self.x,self.y+10)],3)
        pygame.draw.lines(self.screen,black,False,[(self.x-10,self.y),(self.x+10,self.y)],3)
    

class Bar:
    def __init__(self,screen,width,height):
        self.screen = screen
        self.width = width
        self.height = height
        self.white_border = (255,255,255)
        #self.width_of_the_playBar = self.width-150

    def draw(self):
        x = 50                #Start the bar from 50px 
        y = self.height - 150 #Based on the other buttons in main.py.

        pygame.draw.rect(self.screen,self.white_border,(x,y,self.width-100,5),2)

class BarPlayed(Bar):
    def draw(self,dx):
        x = 50                #Start the bar from 50px 
        y = self.height - 150 #Based on the other buttons in main.py.
        pygame.draw.rect(self.screen,(255,255,255),(x,y,dx,5),0)
        

    
    