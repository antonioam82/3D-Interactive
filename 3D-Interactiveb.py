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

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1)
    )

floor_verts = [
    [20, -1, -20],
    [-20, -1, -20],
    [20, -1, 20],
    [-20, -1, 20],
    ]

floor_edges = (
    (0,1),
    (1,3),
    (3,2),
    (2,0)
    )

floor_surface = (
    (0,1,2,3),
    )

def floor():
    glBegin(GL_QUAD_STRIP)
    for surface in floor_surface:
        for vertex in surface:
            glColor3fv((0,1,1))
            glVertex3fv(floor_verts[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in floor_edges:
        for vertex in edge:
            glVertex3fv(floor_verts[vertex])
    glEnd()

    

def Cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        x=0
        for vertex in surface:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(verticies[vertex])
    glEnd()
    
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
    gluPerspective(60, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0,-5)
    #glRotatef(0, 0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        

        if keys[pygame.K_a]:
            glTranslatef(-0.1,0.0,0.0)
        if keys[pygame.K_s]:
            glTranslatef(0.1,0.0,0.0)
        if keys[pygame.K_q]:
            glTranslatef(0.0,-0.1,0.0)
        if keys[pygame.K_w]:
            glTranslatef(0.0,0.1,0.0)
        if keys[pygame.K_z]:
            glTranslatef(0.0,0.0,-0.1)
        if keys[pygame.K_x]:
            glTranslatef(0.0,0.0,0.1)
        if keys[pygame.K_RIGHT]:
            verticies[2][0] += 0.09 #2
            verticies[3][0] += 0.09
            verticies[6][0] += 0.09
            verticies[7][0] += 0.09
            verticies[0][0] += 0.09 #2
            verticies[1][0] += 0.09
            verticies[5][0] += 0.09
            verticies[4][0] += 0.09
        if keys[pygame.K_LEFT]:
            verticies[2][0] -= 0.09 #2
            verticies[3][0] -= 0.09
            verticies[6][0] -= 0.09
            verticies[7][0] -= 0.09
            verticies[0][0] -= 0.09 #2
            verticies[1][0] -= 0.09
            verticies[5][0] -= 0.09
            verticies[4][0] -= 0.09
        if keys[pygame.K_DOWN]:
            verticies[4][2] += 0.09 
            verticies[5][2] += 0.09
            verticies[6][2] += 0.09
            verticies[7][2] += 0.09
            verticies[0][2] += 0.09 
            verticies[1][2] += 0.09
            verticies[2][2] += 0.09
            verticies[3][2] += 0.09
        if keys[pygame.K_UP]:
            verticies[4][2] -= 0.09 
            verticies[5][2] -= 0.09
            verticies[6][2] -= 0.09
            verticies[7][2] -= 0.09
            verticies[0][2] -= 0.09 
            verticies[1][2] -= 0.09
            verticies[2][2] -= 0.09
            verticies[3][2] -= 0.09            
        
            
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        floor()
        Cube()
        
        pygame.display.flip()
        pygame.time.wait(10)

main()
