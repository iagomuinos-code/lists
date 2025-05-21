import pgzrun
import random


WIDTH = 1000
HEIGHT = 1000

TITLE = "Rectangles & Patterns"


def draw():
    height1=350
    width1=300
    screen.draw.filled_circle((250, 250), 50, (255, 0, 0))  # Center, radius, color (green)
    # for i in range(20):
    #     r= random.randint(1,255)
    #     g= random.randint(1,255)
    #     b= random.randint(1,255)
    
    #     rect = Rect((100,100),(height1,width1))
    #     rect.center = 150,300
    #     screen.draw.rect(rect,(r,g,b))
    #     height1= height1-15
    #     width1=width1+10


pgzrun.go()
