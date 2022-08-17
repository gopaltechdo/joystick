from pyjoystick.sdl2 import Key, Joystick, run_event_loop
import urx
from pymodbus.client.sync import ModbusTcpClient
import pygame
import roboiq_gripper
from pygame.locals import *
# IP_Address = '192.168.88.128'  #'192.168.1.53'
IP_Address = '192.168.137.3'  #'192.168.1.53'
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

rob = urx.Robot(IP_Address)
client = ModbusTcpClient(IP_Address)
pygame.init()
pygame.joystick.init()

print(client.connect())


def digit_out_true():
    rob.set_digital_out(1,True)


def digit_out_flase():
    rob.set_digital_out(1,False)

def print_add(joy):
    print('Added', joy)
def print_remove(joy):
    print('Removed', joy)
def key_received(key):
    print('received', key)
    if key.value == Key.HAT_UP:
        print("up")
def GRIPPER_OPEN():
    client.write_registers(129, 1)
def GRIPPER_CLOSE():
    client.write_registers(130, 1)
def move_up():
   try:
       l = 0.01
       v = 0.7
       a = 0.5
       r = 0.01
       pose = rob.getl()
       pose[2] += l
       rob.movep(pose, acc=a, vel=v, wait=False)
       while True:
           p = rob.getl(wait=True)
           if p[2] > pose[2] - 0.05:
               break
   finally:
       print('ROBOPLAY IS CLOSE')

def move_back():
   try:
       l = 0.01
       v = 0.7
       a = 0.5
       r = 0.01
       pose = rob.getl()
       pose[0] += l
       rob.movep(pose, acc=a, vel=v, wait=False)
       while True:
           p = rob.getl(wait=True)
           if p[0] > pose[0] - 0.05:
               break
   finally:
       print('ROBOPLAY IS CLOSE')

def move_front():
   try:
       l = -0.01
       v = 0.7
       a = 0.5
       r = 0.01
       pose = rob.getl()
       pose[0] += l
       rob.movep(pose, acc=a, vel=v, wait=False)
       while True:
           p = rob.getl(wait=True)
           if p[0] > pose[0] - 0.05:
               break
   finally:
       print('ROBOPLAY IS CLOSE')



def move_down():
   try:
       l =-0.01
       v = 0.7
       a = 0.5
       r = 0.01
       pose = rob.getl()
       pose[2] += l
       rob.movep(pose, acc=a, vel=v, wait=False)
       while True:
           p = rob.getl(wait=True)
           if p[2] > pose[1] - 0.05:
               break
   finally:
       print('ROBOPLAY IS CLOSE')

def move_left():
   try:
       l = 0.001
       v = 1.5
       a = 1
       r = 0.01
       pose = rob.getl()
       pose[1] += l
       rob.movep(pose, acc=a, vel=v, wait=False)
       while True:
           p = rob.getl(wait=True)
           if p[1] > pose[1] - 0.05:
               break
   finally:
       print('ROBOPLAY IS CLOSE')


def move_right():
   try:
       l =-0.01
       v = 0.7
       a = 0.5
       r = 0.1
       pose = rob.getl()
       pose[1] += l
       rob.movep(pose, acc=a, vel=v, wait=False)
       while True:
           p = rob.getl(wait=True)
           if p[1] > pose[1] - 0.05:
               break
   finally:
       print('ROBOPLAY IS CLOSE')
import pygame


# Define some colors.
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')





# This is a simple class that will help us print to the screen.
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint(object):
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def tprint(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10


pygame.init()

# Set the width and height of the screen (width, height).
screen = pygame.display.set_mode((500, 700))

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates.
clock = pygame.time.Clock()

# Initialize the joysticks.
pygame.joystick.init()

# Get ready to print.
textPrint = TextPrint()

# -------- Main Program Loop -----------
while not done:
    #
    # EVENT PROCESSING STEP
    #
    # Possible joystick actions: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
    # JOYBUTTONUP, JOYHATMOTION
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.
        elif event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed2.")
            # move_back()
        elif event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")

    #
    # DRAWING STEP
    #
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    textPrint.reset()

    # Get count of joysticks.
    joystick_count = pygame.joystick.get_count()

    textPrint.tprint(screen, "Number of joysticks: {}".format(joystick_count))
    textPrint.indent()

    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        try:
            jid = joystick.get_instance_id()
        except AttributeError:
            # get_instance_id() is an SDL2 method
            jid = joystick.get_id()
        textPrint.tprint(screen, "Joystick {}".format(jid))
        textPrint.indent()
        # Get the name from the OS for the controller/joystick.
        name = joystick.get_name()
        textPrint.tprint(screen, "Joystick name: {}".format(name))
        try:
            guid = joystick.get_guid()
        except AttributeError:
            # get_guid() is an SDL2 method
            pass
        else:
            textPrint.tprint(screen, "GUID: {}".format(guid))
        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        textPrint.tprint(screen, "Number of axes: {}".format(axes))
        textPrint.indent()
        # print(axes
        for i in range(axes):
            axis = joystick.get_axis(i)
            textPrint.tprint(screen, "Axis {} value: {:>6.3f}".format(i, axis))
        textPrint.unindent()
        # print("Axis {} value: {:>6.3f}".format(i, axis))
        if joystick.get_axis(1) == -1:
            print("gripper open")
            g = roboiq_gripper.RobotiqGripper("COM5")
            g.activate()
            g.openGripper()

        if joystick.get_axis(0) == -1:
            print("gripper close")
            g = roboiq_gripper.RobotiqGripper("COM5")
            g.activate()
            g.closeGripper()

            # GRIPPER_CLOSE()


        if joystick.get_axis(2) == -1:
            print("robot back")
            move_back()
        if joystick.get_axis(3) == -1:
            print("robot_front")
            move_front()
        buttons = joystick.get_numbuttons()
        textPrint.tprint(screen, "Number of buttons: {}".format(buttons))
        textPrint.indent()
        #print(buttons)
        for i in range(buttons):
            button = joystick.get_button(i)
            textPrint.tprint(screen,
                             "Button {:>2} value: {}".format(i, button))
        textPrint.unindent()

        hats = joystick.get_numhats()
        textPrint.tprint(screen, "Number of hats: {}".format(hats))
        textPrint.indent()
        # Hat position. All or nothing for direction, not a float like
        # get_axis(). Position is a tuple of int values (x, y).
        for i in range(hats):
            hat = joystick.get_hat(i)
            textPrint.tprint(screen, "Hat {} value: {}".format(i, str(hat)))
        textPrint.unindent()
        textPrint.unindent()
        if hat == (0, 1):
            print("up")
            move_up()
        elif hat == (1, 0):
            print("right")
            move_right()
        elif hat == (-1, 0):
            print("left")
            move_left()
            rob.send_message("hiiiii")
        elif hat == (0, -1):
            print("down")
            move_down()

            print("hiiiiiiiiiiiiiii")

    #
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    #

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second.
    clock.tick(20)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()


