import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def verts():
    global verticies
    verticies = [
    [1, -1, -1],#det inf der
    [1, 1, -1],#det sup der
    [-1, 1, -1],#det sup iz
    [-1, -1, -1],#det inf iz
    [1, -1, 1],#del inf der
    [1, 1, 1],#del sup der
    [-1, -1, 1],#del inf der
    [-1, 1, 1]#del sup iz
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
    
def main():
    global verticies
    pygame.init()
    display = (1000, 650)
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
            glRotatef(1, 1, 0, 0)
        if keys[pygame.K_DOWN]:
            glRotatef(1, -1, 0, 0)
        if keys[pygame.K_RIGHT]:
            glRotatef(1, 0, 1, 0)
        if keys[pygame.K_LEFT]:
            glRotatef(1, 0, -1, 0)
        if keys[pygame.K_c]:
            verts()
        if keys[pygame.K_b]:
            verticies[1][1] += 0.09
            verticies[2][1] += 0.09
            verticies[5][1] += 0.09
            verticies[7][1] += 0.09
        if keys[pygame.K_a]:
            verticies[1][1] -= 0.09
            verticies[2][1] -= 0.09
            verticies[5][1] -= 0.09
            verticies[7][1] -= 0.09
            
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)    
        Cube()
        
        pygame.display.flip()
        pygame.time.wait(10)

main()
