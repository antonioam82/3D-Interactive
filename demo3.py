import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def verts():
    global verticies
    verticies = [
    [1, -1, -1],#inf, der, tras
    [1, 1, -1],#sup, der, tras
    [-1, 1, -1],#sup, izq, tras
    [-1, -1, -1],#inf, izq, tras
    [1, -1, 1],#inf, der, del
    [1, 1, 1],#sup, der, del
    [-1, -1, 1],#inf, izg, del
    [-1, 1, 1]#sup, izq, del
    ]

def C1_verts():
    global verticies1#hor, vert, prof
    verticies1 = [
    [4, -1, -1],#inf, der, tras
    [4, 1, -1],#sup, der, tras
    [2, 1, -1],#sup, izq, tras
    [2, -1, -1],#inf, izq, tras
    [4, -1, 1],#inf, der, del
    [4, 1, 1],#sup, der, del
    [2, -1, 1],#inf, izg, del
    [2, 1, 1]#sup, izq, del
    ]

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )
        

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])

    glEnd()

def Cube1():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies1[vertex])
    glEnd()
    
def main():
    global verticies, verticies1
    pygame.init()
    display = (1200, 680)#(1600,900)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    verts()
    C1_verts()
    
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0,-5)
    #glRotatef(0, 0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        

        if keys[pygame.K_UP]:
            glRotatef(1, -1, 0, 0)
        if keys[pygame.K_DOWN]:
            glRotatef(1, 1, 0, 0)
        if keys[pygame.K_RIGHT]:
            glRotatef(1, 0, 1, 0)
        if keys[pygame.K_LEFT]:
            glRotatef(1, 0, -1, 0)
        if keys[pygame.K_k]:
            glRotatef(1, 0, 0, 1)
        if keys[pygame.K_l]:
            glRotatef(1, 0, 0, -1)
        if keys[pygame.K_z]:
            glTranslatef(0.0,0.0,-0.1)
        if keys[pygame.K_x]:
            glTranslatef(0.0,0.0,0.1)

        
            
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)    
        Cube()
        Cube1()
        
        pygame.display.flip()
        pygame.time.wait(10)

main()
