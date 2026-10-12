
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math
import os

# GLOBAL SETTINGS

GRID_LENGTH = 600
TILE_SIZE = 60
TILE_COUNT = 20
BOUNDARY_LIMIT = GRID_LENGTH - 45

player_x, player_z = 0, -250
player_angle = 0
is_game_over = False
is_game_won = False
game_paused = False
cheat_mode = False
cheat_timer = 0  
camera_mode = 0  # 0 for 3rd person, 1 for 1st person

shroom_health = 100  
score = 0            
snails = []
snail_speed = 0.8
bullets = []
bullet_speed = 18

slime_paths = []
turtle_pos = [200, 200]
turtle_active = False
turtle_uses = 2

# GAME CONTROL LOGIC

def restart_game():
    global player_x, player_z, player_angle, is_game_over, is_game_won, shroom_health, score, snails, bullets, slime_paths, turtle_active, turtle_uses, game_paused, cheat_mode, camera_mode
    player_x, player_z = 0, -250
    player_angle = 0
    is_game_over = False
    is_game_won = False
    game_paused = False
    cheat_mode = False
    camera_mode = 0
    shroom_health = 100
    score = 0
    snails = []
    bullets = []
    slime_paths = []
    turtle_active = False
    turtle_uses = 2
    for _ in range(5): spawn_snail()


# MANUAL TEXT DRAWING

def draw_digit(digit, x, y):
    glBegin(GL_LINES)
    if digit == 'S' or digit == 5:
        glVertex2f(x, y+20); glVertex2f(x+15, y+20) 
        glVertex2f(x, y+10); glVertex2f(x, y+20)    
        glVertex2f(x, y+10); glVertex2f(x+15, y+10) 
        glVertex2f(x+15, y); glVertex2f(x+15, y+10) 
        glVertex2f(x, y); glVertex2f(x+15, y)       
    elif digit == 'C':
        glVertex2f(x, y+20); glVertex2f(x+15, y+20) 
        glVertex2f(x, y); glVertex2f(x, y+20)       
        glVertex2f(x, y); glVertex2f(x+15, y)       
    elif digit == 'O' or digit == 0:
        glVertex2f(x, y); glVertex2f(x+15, y)       
        glVertex2f(x, y+20); glVertex2f(x+15, y+20) 
        glVertex2f(x, y); glVertex2f(x, y+20)       
        glVertex2f(x+15, y); glVertex2f(x+15, y+20) 
    elif digit == 'R':
        glVertex2f(x, y); glVertex2f(x, y+20)       
        glVertex2f(x, y+20); glVertex2f(x+15, y+20) 
        glVertex2f(x+15, y+10); glVertex2f(x+15, y+20) 
        glVertex2f(x, y+10); glVertex2f(x+15, y+10) 
        glVertex2f(x, y+10); glVertex2f(x+15, y)    
    elif digit == 'E':
        glVertex2f(x, y); glVertex2f(x, y+20)       
        glVertex2f(x, y+20); glVertex2f(x+15, y+20) 
        glVertex2f(x, y+10); glVertex2f(x+15, y+10) 
        glVertex2f(x, y); glVertex2f(x+15, y)       
    elif digit == 'G':
        glVertex2f(x, y+20); glVertex2f(x+15, y+20) 
        glVertex2f(x, y); glVertex2f(x, y+20)       
        glVertex2f(x, y); glVertex2f(x+15, y)       
        glVertex2f(x+15, y); glVertex2f(x+15, y+10) 
        glVertex2f(x+7, y+10); glVertex2f(x+15, y+10) 
    elif digit == 'A':
        glVertex2f(x, y); glVertex2f(x, y+20)       
        glVertex2f(x+15, y); glVertex2f(x+15, y+20) 
        glVertex2f(x, y+20); glVertex2f(x+15, y+20) 
        glVertex2f(x, y+10); glVertex2f(x+15, y+10) 
    elif digit == 'M':
        glVertex2f(x, y); glVertex2f(x, y+20)       
        glVertex2f(x+15, y); glVertex2f(x+15, y+20) 
        glVertex2f(x, y+20); glVertex2f(x+7, y+10)  
        glVertex2f(x+7, y+10); glVertex2f(x+15, y+20) 
    elif digit == 'V':
        glVertex2f(x, y+20); glVertex2f(x+7, y)     
        glVertex2f(x+7, y); glVertex2f(x+15, y+20)  
    elif digit == 'H':
        glVertex2f(x, y); glVertex2f(x, y+20)
        glVertex2f(x+15, y); glVertex2f(x+15, y+20)
        glVertex2f(x, y+10); glVertex2f(x+15, y+10)
    elif digit == 'L':
        glVertex2f(x, y); glVertex2f(x, y+20)
        glVertex2f(x, y); glVertex2f(x+15, y)
    elif digit == 'T':
        glVertex2f(x, y+20); glVertex2f(x+15, y+20)
        glVertex2f(x+7, y); glVertex2f(x+7, y+20)
    elif digit == '!':
        glVertex2f(x+7, y+5); glVertex2f(x+7, y+20) 
        glVertex2f(x+7, y); glVertex2f(x+7, y+2)    
    elif digit == 1:
        glVertex2f(x+15, y); glVertex2f(x+15, y+20)
    elif digit == 2:
        glVertex2f(x, y+20); glVertex2f(x+15, y+20); glVertex2f(x+15, y+10); glVertex2f(x+15, y+20)
        glVertex2f(x, y+10); glVertex2f(x+15, y+10); glVertex2f(x, y); glVertex2f(x, y+10)
        glVertex2f(x, y); glVertex2f(x+15, y)
    elif digit == 3:
        glVertex2f(x, y+20); glVertex2f(x+15, y+20); glVertex2f(x+15, y); glVertex2f(x+15, y+20)
        glVertex2f(x, y+10); glVertex2f(x+15, y+10); glVertex2f(x, y); glVertex2f(x+15, y)
    elif digit == 4:
        glVertex2f(x, y+10); glVertex2f(x, y+20); glVertex2f(x+15, y); glVertex2f(x+15, y+20)
        glVertex2f(x, y+10); glVertex2f(x+15, y+10)
    elif digit == 6:
        glVertex2f(x, y); glVertex2f(x, y+20); glVertex2f(x, y+10); glVertex2f(x+15, y+10)
        glVertex2f(x+15, y); glVertex2f(x+15, y+10); glVertex2f(x, y); glVertex2f(x+15, y)
    elif digit == 7:
        glVertex2f(x, y+20); glVertex2f(x+15, y+20); glVertex2f(x+15, y); glVertex2f(x+15, y+20)
    elif digit == 8:
        glVertex2f(x, y); glVertex2f(x, y+20); glVertex2f(x+15, y); glVertex2f(x+15, y+20)
        glVertex2f(x, y+20); glVertex2f(x+15, y+20); glVertex2f(x, y+10); glVertex2f(x+15, y+10)
        glVertex2f(x, y); glVertex2f(x+15, y)
    elif digit == 9:
        glVertex2f(x, y+10); glVertex2f(x, y+20); glVertex2f(x+15, y); glVertex2f(x+15, y+20)
        glVertex2f(x, y+20); glVertex2f(x+15, y+20); glVertex2f(x, y+10); glVertex2f(x+15, y+10)
    glEnd()

def draw_string_manual(x, y, text, color=(1, 1, 0)):
    glDisable(GL_LIGHTING)
    glMatrixMode(GL_PROJECTION); glPushMatrix(); glLoadIdentity(); gluOrtho2D(0, 1000, 0, 800)
    glMatrixMode(GL_MODELVIEW); glPushMatrix(); glLoadIdentity()
    glLineWidth(3); glColor3f(color[0], color[1], color[2])
    offset = 0
    for char in text.upper():
        if char == ' ': offset += 30; continue
        try:
            val = int(char) if char.isdigit() else char
            draw_digit(val, x + offset, y)
        except: pass
        offset += 25
    glPopMatrix(); glMatrixMode(GL_PROJECTION); glPopMatrix(); glMatrixMode(GL_MODELVIEW); glEnable(GL_LIGHTING)


# DRAWING FUNCTIONS

def init_lighting():
    glEnable(GL_LIGHTING); glEnable(GL_LIGHT0); glEnable(GL_DEPTH_TEST); glEnable(GL_NORMALIZE)
    glLightfv(GL_LIGHT0, GL_POSITION, [0.0, 500.0, 200.0, 1.0])
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.4, 0.4, 0.4, 1.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.8, 0.8, 0.8, 1.0])
    glEnable(GL_COLOR_MATERIAL); glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

def draw_slime():
    glDisable(GL_LIGHTING); glColor4f(0.0, 1.0, 0.0, 0.4)
    for pos in slime_paths:
        glPushMatrix(); glTranslatef(pos[0], 1, pos[1]); glBegin(GL_POLYGON)
        for i in range(8):
            theta = 2.0 * 3.1415926 * i / 8
            glVertex3f(12 * math.cos(theta), 0, 12 * math.sin(theta))
        glEnd(); glPopMatrix()
    glEnable(GL_LIGHTING)

def draw_tile_grid():
    glDisable(GL_LIGHTING); origin = -GRID_LENGTH
    for row in range(TILE_COUNT):
        for col in range(TILE_COUNT):
            x0, z0 = origin + col * TILE_SIZE, origin + row * TILE_SIZE
            if (row + col) % 2 == 0: glColor3f(0.18, 0.45, 0.15)
            else: glColor3f(0.35, 0.72, 0.25)
            glBegin(GL_QUADS); glVertex3f(x0, 0, z0); glVertex3f(x0 + TILE_SIZE, 0, z0)
            glVertex3f(x0 + TILE_SIZE, 0, z0 + TILE_SIZE); glVertex3f(x0, 0, z0 + TILE_SIZE); glEnd()
    glEnable(GL_LIGHTING)

def draw_boundaries():
    glColor3f(0.5, 0.0, 0.8); L, h = GRID_LENGTH, 60
    glBegin(GL_QUADS)
    glVertex3f(-L, 0, -L); glVertex3f(L, 0, -L); glVertex3f(L, h, -L); glVertex3f(-L, h, -L)
    glVertex3f(-L, 0, L); glVertex3f(L, 0, L); glVertex3f(L, h, L); glVertex3f(-L, h, L)
    glVertex3f(-L, 0, -L); glVertex3f(-L, 0, L); glVertex3f(-L, h, L); glVertex3f(-L, h, -L)
    glVertex3f(L, 0, -L); glVertex3f(L, 0, L); glVertex3f(L, h, L); glVertex3f(L, h, -L); glEnd()

def draw_realistic_mushroom(stem_r, stem_h, cap_r, color):
    quad = gluNewQuadric(); glColor3f(0.8, 0.7, 0.6)
    glPushMatrix(); glRotatef(-90, 1, 0, 0); gluCylinder(quad, stem_r, stem_r, stem_h, 32, 32); glPopMatrix()
    glPushMatrix(); glTranslatef(0, stem_h, 0); glColor3f(color[0], color[1], color[2])
    glScalef(1.2, 0.8, 1.2); glutSolidSphere(cap_r, 40, 40); glPopMatrix()

def draw_player():
    if camera_mode == 1: return
    glPushMatrix(); glTranslatef(player_x, 0, player_z)
    if is_game_over: glRotatef(90, 1, 0, 0); glTranslatef(0, 20, 0)
    else: glRotatef(player_angle, 0, 1, 0)
    draw_realistic_mushroom(15, 45, 35, (0.1, 0.3, 0.9))
    glColor3f(0, 0, 0)
    for s in [-1, 1]: glPushMatrix(); glTranslatef(s * 7, 30, 15); glutSolidSphere(3, 10, 10); glPopMatrix()
    glColor3f(0.8, 0.7, 0.6); glPushMatrix(); glTranslatef(25, 25, 5); glutSolidSphere(7, 12, 12)
    glColor3f(0.7, 0.7, 0.7); glTranslatef(0, 0, 5); gluCylinder(gluNewQuadric(), 6, 6, 40, 16, 16); glPopMatrix(); glPopMatrix()

def draw_snail(s):
    glPushMatrix(); glTranslatef(s[0], 0, s[1]); glColor3f(0.05, 0.05, 0.05)
    glPushMatrix(); glTranslatef(0, 15, 0); glScalef(1.4, 1.0, 1.0); glutSolidSphere(20, 16, 16); glPopMatrix()
    for i in [-1, 1]:
        glPushMatrix(); glTranslatef(i * 8, 25, 12); glRotatef(-20, 1, 0, 0); gluCylinder(gluNewQuadric(), 2, 2, 12, 8, 8)
        glTranslatef(0, 0, 12); glColor3f(1, 1, 1); glutSolidSphere(3, 8, 8); glColor3f(0, 0, 0); glutSolidSphere(1.5, 5, 5); glPopMatrix()
    glPopMatrix()

def draw_turtle():
    if not turtle_active: return
    glPushMatrix(); glTranslatef(turtle_pos[0], 0, turtle_pos[1])
    glColor3f(0.0, 0.5, 0.0)
    glPushMatrix(); glScalef(1.5, 0.8, 1.2); glutSolidSphere(25, 20, 20); glPopMatrix()
    glColor3f(0.2, 0.8, 0.2)
    glPushMatrix(); glTranslatef(0, 5, 30); glutSolidSphere(10, 12, 12); glPopMatrix()
    for x_offset, z_offset in [(-15, 15), (15, 15), (-15, -15), (15, -15)]:
        glPushMatrix(); glTranslatef(x_offset, 0, z_offset); glutSolidSphere(6, 8, 8); glPopMatrix()
    glPopMatrix()


# CORE LOGIC

def spawn_snail():
    side = random.randint(0, 3)
    if side == 0: x, z = -BOUNDARY_LIMIT, random.randint(-500, 500)
    elif side == 1: x, z = BOUNDARY_LIMIT, random.randint(-500, 500)
    elif side == 2: x, z = random.randint(-500, 500), -BOUNDARY_LIMIT
    else: x, z = random.randint(-500, 500), BOUNDARY_LIMIT
    snails.append([x, z])

def fire_bullet():
    if is_game_over or is_game_won or game_paused: return
    rad = math.radians(player_angle)
    bullets.append([player_x, player_z, math.sin(rad), math.cos(rad)])

def update(value):
    global shroom_health, score, is_game_over, is_game_won, snail_speed, turtle_active, turtle_uses, game_paused, cheat_mode, cheat_timer
    if is_game_over or is_game_won or game_paused: 
        glutTimerFunc(16, update, 0)
        return

    if cheat_mode:
        cheat_timer += 1
        if cheat_timer > 10:  
            if snails:
                s = snails[0]
                score += 5
                snails.remove(s)
                spawn_snail()
            cheat_timer = 0

    if score >= 30 and turtle_uses > 0:
        turtle_active = True

    if turtle_active:
        dist_to_turtle = math.sqrt((player_x - turtle_pos[0])**2 + (player_z - turtle_pos[1])**2)
        if dist_to_turtle < 50:
            shroom_health = 100 
            turtle_uses -= 1
            turtle_active = False
            turtle_pos[0] = random.randint(-400, 400)
            turtle_pos[1] = random.randint(-400, 400)

    for s in snails[:]:
        dist_to_center = math.sqrt(s[0]**2 + s[1]**2)
        if dist_to_center > 10:
            s[0] -= (s[0]/dist_to_center) * snail_speed
            s[1] -= (s[1]/dist_to_center) * snail_speed
            if score >= 30:
                if random.random() < 0.05:
                    slime_paths.append([s[0], s[1]])
                    if len(slime_paths) > 200: slime_paths.pop(0)

        if dist_to_center < 80: 
            shroom_health -= 10
            if s in snails: snails.remove(s)
            spawn_snail()

        dist_to_player = math.sqrt((s[0]-player_x)**2 + (s[1]-player_z)**2)
        if dist_to_player < 45: is_game_over = True

    for b in bullets[:]:
        b[0] += b[2] * bullet_speed; b[1] += b[3] * bullet_speed
        if abs(b[0]) > GRID_LENGTH or abs(b[1]) > GRID_LENGTH: bullets.remove(b)
        else:
            for s in snails[:]:
                if math.sqrt((b[0]-s[0])**2 + (b[1]-s[1])**2) < 40:
                    score += 5 
                    if s in snails: snails.remove(s)
                    if b in bullets: bullets.remove(b)
                    spawn_snail(); break

    if shroom_health <= 0: shroom_health = 0; is_game_over = True
    if score >= 500: is_game_won = True

    glutPostRedisplay(); glutTimerFunc(16, update, 0)


# CONTROLS

def mouse_click(button, state, x, y):
    global camera_mode
    if state == GLUT_DOWN:
        if button == GLUT_LEFT_BUTTON:
            camera_mode = 1 - camera_mode 
        elif button == GLUT_RIGHT_BUTTON:
            fire_bullet()

def keyboard(key, x, y):
    global player_x, player_z, player_angle, game_paused, cheat_mode
    if key == b'p': game_paused = not game_paused
    if key == b'r': restart_game()
    if key == b'q': os._exit(0)
    if key == b'c': cheat_mode = not cheat_mode

    if is_game_over or is_game_won or game_paused: return
    
    current_speed = 25
    for slime in slime_paths:
        if math.sqrt((player_x - slime[0])**2 + (player_z - slime[1])**2) < 25: 
            current_speed = 10; break
    nx, nz = player_x, player_z
    if key == b'w': nz += current_speed; player_angle = 0
    elif key == b's': nz -= current_speed; player_angle = 180
    elif key == b'd': nx -= current_speed; player_angle = 270
    elif key == b'a': nx += current_speed; player_angle = 90
    elif key in [b' ', b'\r']: fire_bullet()
    if abs(nx) < BOUNDARY_LIMIT: player_x = nx
    if abs(nz) < BOUNDARY_LIMIT: player_z = nz


# DISPLAY
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION); glLoadIdentity(); gluPerspective(60, 1.25, 1, 4000)
    glMatrixMode(GL_MODELVIEW); glLoadIdentity()
    
    if camera_mode == 0: 
        gluLookAt(player_x, 450, player_z - 750, player_x, 0, player_z + 200, 0, 1, 0)
    else: 
        rad = math.radians(player_angle)
        gluLookAt(player_x, 45, player_z, 
                  player_x + math.sin(rad) * 100, 40, player_z + math.cos(rad) * 100, 
                  0, 1, 0)
                  
    init_lighting()
    draw_turtle()
    draw_tile_grid(); draw_slime(); draw_boundaries()
    
    # Corrected Mushroom color logic:
    # RED if 50 or above, YELLOW if below 50.
    if shroom_health >= 50: 
        m_color = (0.9, 0.1, 0.1) # Red
    else: 
        m_color = (0.9, 0.9, 0.1) # Yellow
    
    draw_realistic_mushroom(30, 100, 75, m_color)
    draw_player()
    for s in snails: draw_snail(s)
    glDisable(GL_LIGHTING); glColor3f(1, 0.9, 0)
    for b in bullets: glPushMatrix(); glTranslatef(b[0], 35, b[1]); glutSolidCube(10); glPopMatrix()

    draw_string_manual(20, 750, f"HEALTH {shroom_health}", (0, 1, 1))
    draw_string_manual(20, 715, f"SCORE {score}", (1, 1, 0))
    if cheat_mode: draw_string_manual(20, 680, "CHEAT ON", (1, 0, 1))

    if game_paused: draw_string_manual(400, 450, "PAUSED", (1, 1, 1))
    if is_game_over: draw_string_manual(380, 400, "GAME OVER!", (1, 0, 0))
    if is_game_won: draw_string_manual(400, 400, "YOU WIN!", (0, 1, 0))

    glEnable(GL_LIGHTING); glutSwapBuffers()

def main():
    glutInit(); glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1000, 800); glutCreateWindow(b"Mushroom Defense")
    init_lighting(); glEnable(GL_BLEND); glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    for _ in range(5): spawn_snail()
    glutDisplayFunc(display); glutKeyboardFunc(keyboard); glutMouseFunc(mouse_click)
    glutTimerFunc(0, update, 0); glutMainLoop()

if __name__ == "__main__":
    main()
