import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def main():
    pygame.init()
    size = (1000, 650)
    pygame.display.set_mode(size, DOUBLEBUF|OPENGL)

    pygame.display.flip()
    pygame.time.wait(10)

main()
