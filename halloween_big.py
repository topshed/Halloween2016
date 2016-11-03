
from Adafruit_LED_Backpack import BicolorMatrix8x8
from PIL import Image
from PIL import ImageDraw
import time
import random
from gpiozero import PWMLED, MotionSensor
import pygame

left = BicolorMatrix8x8.BicolorMatrix8x8()
right = BicolorMatrix8x8.BicolorMatrix8x8(address=0x72)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)
COLOURS = [RED, GREEN, YELLOW]

left.begin()
right.begin()

leds = PWMLED(21)
pir = MotionSensor(19)

def spiders():
    leds.pulse(2,2,1,True)

def both_eyes(image):
    left.set_image(image)
    right.set_image(image)
    left.write_display()
    right.write_display()

def eyes_off():
    right.clear()
    left.clear()
    left.write_display()
    right.write_display()

def eyes_centre():
    eye = Image.new('RGB',(8,8))
    d1 = ImageDraw.Draw(eye)
    d1.rectangle((3,3,4,4),outline=(255,0,0))
    d1.line((2,7,5,7), fill=RED)
    d1.line((2,0,5,0), fill=RED)
    d1.line((6,1,6,6), fill=RED)
    d1.line((1,1,1,6), fill=RED)
    both_eyes(eye)

def eyes_wink():
    leye = Image.new('RGB',(8,8))
    d1 = ImageDraw.Draw(leye)
    d1.rectangle((3,3,4,4),outline=(255,0,0))
    d1.line((2,7,5,7), fill=RED)
    d1.line((2,0,5,0), fill=RED)
    d1.line((6,1,6,6), fill=RED)
    d1.line((1,1,1,6), fill=RED)
    reye = Image.new('RGB',(8,8))
    d2 = ImageDraw.Draw(reye)
    d2.line((4,0,4,7), fill=RED)
    right.clear()
    left.clear()
    left.set_image(leye)
    right.set_image(reye)
    left.write_display()
    right.write_display()
    time.sleep(1)
    right.set_image(leye)
    right.write_display()

def eyes_right():
    eyes_right = Image.new('RGB',(8,8))
    d1 = ImageDraw.Draw(eyes_right)
    d1.rectangle((3,2,4,3),outline=(255,0,0))
    d1.line((2,7,5,7), fill=RED)
    d1.line((2,0,5,0), fill=RED)
    d1.line((6,1,6,6), fill=RED)
    d1.line((1,1,1,6), fill=RED)
    both_eyes(eyes_right)

def eyes_left():
    eyes_left = Image.new('RGB',(8,8))
    d1 = ImageDraw.Draw(eyes_left)
    d1.rectangle((3,4,4,5),outline=(255,0,0))
    d1.line((2,7,5,7), fill=RED)
    d1.line((2,0,5,0), fill=RED)
    d1.line((6,1,6,6), fill=RED)
    d1.line((1,1,1,6), fill=RED)
    both_eyes(eyes_left)


def eyes_wide():
    eye = Image.new('RGB',(8,8))
    d1 = ImageDraw.Draw(eye)
    d1.rectangle((3,3,4,4),outline=(255,0,0))
    d1.line((1,7,6,7), fill=RED)
    d1.line((1,0,6,0), fill=RED)
    d1.line((7,1,7,6), fill=RED)
    d1.line((0,1,0,6), fill=RED)
    both_eyes(eye)

def eyes_googly():
    eye = Image.new('RGB',(8,8))
    d1 = ImageDraw.Draw(eye)
    d1.line((1,7,6,7), fill=RED)
    d1.line((1,0,6,0), fill=RED)
    d1.line((7,1,7,6), fill=RED)
    d1.line((0,1,0,6), fill=RED)
    for x in range(20):

        offsetx = random.randint(-2,2)
        offsety = random.randint(-2,2)
        d1.rectangle((3+offsetx,3+offsety,4+offsetx,4+offsety),outline=(255,0,0))
        both_eyes(eye)
        time.sleep(0.2)
        d1.rectangle((1,1,6,6),outline=(0,0,0),fill=(0,0,0))
        both_eyes(eye)

def eyes_narrow():
    eye = Image.new('RGB',(8,8))
    d1 = ImageDraw.Draw(eye)
    d1.rectangle((3,3,4,4),outline=(255,0,0))
    d1.line((3,7,4,7), fill=RED)
    d1.line((3,0,4,0), fill=RED)
    d1.line((5,1,5,6), fill=RED)
    d1.line((2,1,2,6), fill=RED)
    both_eyes(eye)

def eyes_hypno(n):
    eyes_right = Image.new('RGB',(8,8))
    d1 = ImageDraw.Draw(eyes_right)
    x = 0
    while x < n:
        d1.rectangle((0,0,7,7),outline=COLOURS[x%3])
        d1.rectangle((1,1,6,6),outline=COLOURS[(x+1)%3])
        d1.rectangle((2,2,5,5),outline=COLOURS[(x+2)%3])
        d1.rectangle((3,3,4,4),outline=COLOURS[x%3])
        both_eyes(eyes_right)
        time.sleep(0.05)
        x+=1

def random_eyes():
    r = random.randint(1,8)
    t = random.randint(1,2)
    if r ==  1:
        eyes_centre()
        time.sleep(t)
    elif r == 2:
        eyes_centre()
        time.sleep(t)
        eyes_left()
        time.sleep(t)
        eyes_centre()
        time.sleep(t)
    elif r == 3:
        eyes_centre()
        time.sleep(t)
        eyes_right()
        time.sleep(t)
        eyes_centre()
        time.sleep(t)
    elif r == 4:
        eyes_hypno(10)
    elif r == 5:
        eyes_centre()
        time.sleep(t)
        eyes_narrow()
        time.sleep(t)
        eyes_centre()
        time.sleep(t)
    elif r == 6:
        eyes_centre()
        time.sleep(t)
        eyes_wide()
        time.sleep(t)
        eyes_centre()
        time.sleep(t)
    elif r == 7:
        eyes_centre()
        time.sleep(t)
        eyes_wink()
        eyes_centre()
        time.sleep(t)
    elif r == 8:
        eyes_centre()
        time.sleep(t)
        eyes_wide()
        time.sleep(t)
        eyes_centre()
        time.sleep(t)
    print(r)

def laugh():
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/laff.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        eyes_hypno(30)
    pygame.mixer.quit()

#eyes_googly()
while True:
    triggered = False
    if pir.motion_detected:
        if not triggered:
            triggered = True
            spiders()
            laugh()
            triggered = False
   random_eyes()
