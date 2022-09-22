from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def MidPointLineDrawingAlgo(x1, y1, x2, y2):
    slope = 0

    if x2-x1==0:
        slope = y2 - y1
    else:
        slope = (y2 - y1)/(x2 - x1)

    if abs(slope)<1:
        if x1>x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        dx = abs(x2-x1)
        dy = abs(y2-y1)
        d = 2*dy - dx

        x = x1
        y = y1

        while x<=x2:
            glVertex2f(x, y)
            x+=1

            if d>=1:
                if slope<1:
                    y+=1
                else:
                    y-=1
                d+=2*dy-2*dx
            else:
                d+=2*dy

    if abs(slope)>=1:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        d = 2 * dy - dx

        x = x1
        y = y1

        while y <= y2:
            glVertex2f(x, y)
            y += 1

            if d >= 0:
                if slope >= 1:
                    x += 1
                else:
                    x -= 1
                d += (2 * dx) - (2 * dy)
            else:
                d += 2 * dx



def drawing_line(x1, y1, x2, y2):
    glPointSize(1)
    glBegin(GL_POINTS)
    MidPointLineDrawingAlgo(x1, y1, x2, y2)
    glEnd()



def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.5, 0.0)

    #drawing for 9
    drawing_line(100, 400, 50, 400)
    drawing_line(50,400, 50, 350)
    drawing_line(50,350, 100, 350)
    drawing_line(100, 350, 100, 400)
    drawing_line(100, 350, 100, 300)
    drawing_line(100, 300, 50, 300)


    #drawing for 4
    drawing_line(170, 400, 170, 350)
    drawing_line(170, 350, 120, 350)
    drawing_line(120, 350, 120, 400)
    drawing_line(170, 400, 170, 300)


    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Show DIGITS")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()