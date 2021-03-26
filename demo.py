import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def verts():
    global verticies
    verticies = [
    [0, 1, 0],
    [1, 0, -1],
    [-1, 0, -1],
    [1, 0, 1],
    [-1, 0, 1],
    [0, -1, 0]
    ]

edges = (
    (0,1),
    (2,1),
    (0,4),
    (0,2),
    (0,3),
    (4,2),
    (1,3),
    (4,3),
    (5,1),
    (5,4),
    (5,2),
    (5,3)
    )
    

def Triangle():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])

    glEnd()
    
def main():
    global verticies
    pygame.init()
    display = (1200, 680)#(1600,900)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    verts()
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
            glRotatef(5, 0, 1, 0)
        if keys[pygame.K_LEFT]:
            glRotatef(5, 0, -1, 0)
        if keys[pygame.K_k]:
            glRotatef(1, 0, 0, 1)
        if keys[pygame.K_l]:
            glRotatef(1, 0, 0, -1)
        if keys[pygame.K_c]:
            verts()
        if keys[pygame.K_z]:
            glTranslatef(0.0,0.0,-0.1)
        if keys[pygame.K_x]:
            glTranslatef(0.0,0.0,0.1)
        if keys[pygame.K_a]:
            glTranslatef(-0.1,0.0,0.0)
        if keys[pygame.K_s]:
            glTranslatef(0.1,0.0,0.0)
        if keys[pygame.K_q]:
            glTranslatef(0.0,-0.1,0.0)
        if keys[pygame.K_w]:
            glTranslatef(0.0,0.1,0.0)

        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)    
        Triangle()
        
        pygame.display.flip()
        pygame.time.wait(10)

main()
