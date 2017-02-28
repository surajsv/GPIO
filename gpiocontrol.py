
import pygame
import time
import RPi.GPIO as GPIO
from pygame.locals import *
import glob
import sys
import os

from twython import Twython

IMG_WIDTH = "320"
IMG_HEIGHT =  "240"
IMG_NAME = "tweet-pic.jpg"


# Twitter application authentication
APP_KEY = 'bzmRIwbJXBKdTA36zJodtAZeY'
APP_SECRET = 'g941v6SMHg2QK0lUtrFwBwhFBD9o3VrsLfXWJtPgAjIYTvumu2'
OAUTH_TOKEN = '3139009678-DiiamJvvcTKhhE8RbgTE8rwze7LiXJ5Bc1Hj3NO'
OAUTH_TOKEN_SECRET = 'vd7B1vXCg8Et1Fpw7ruGzZq6eTFklUBawOBrrbfygRkfl'

snapCommand = "raspistill -w " + IMG_WIDTH +  " -h " + IMG_HEIGHT + " -o " + IMG_NAME

api = Twython(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)


os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"
screen_state = 0
#setup gpio
GPIO.setmode(GPIO.BCM)
GPIO.setup( 4, GPIO.OUT)
GPIO.setup( 5, GPIO.OUT)
GPIO.setup( 6, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
#enable pull-up resistors
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#define some colors
#color    R    G    B
white = (255, 255, 255)
red   = (255,   0,   0)
green = (  0, 255,   0)
blue  = (  0,   0, 255)
black = (  0,   0,   0)
cyan  = (  0, 255, 255)
blue2 = ( 67, 110, 238)
green2 = ( 0, 201, 87)
red2 = (238,99,99)
#initial state colors for indicators
state_color1 = red
state_color2 = red
state_color3 = red
state_color4 = red
state_color5 = red
state_color6 = red
state_color7 = red
state_color8 = red
state_color9 = red
state_color10 = red
pygame.init()
#screen size
width = 320
height = 240
size = (width, height)
screen = pygame.display.set_mode(size)
#define font
font = pygame.font.Font(None, 20)
#initial output state
gpio_state4  = False
gpio_state5  = False
gpio_state6  = False
gpio_state12 = False
gpio_state13 = False
password = 4321
temp_pass = 0 
tens = 0 
new_position=(0,0)
running = True
fflag=0
string1 = []
f = open("command.txt",'r')
old_position = (0,0)
choose_door = 0
door_output = 13
password_entered = 0
label_4 = font.render("Not authentiacated", 1, red)
while running:
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        
                        GPIO.cleanup()        
                        running = 0
                
                if event.type == pygame.KEYDOWN:
                        if event.key == K_ESCAPE:
                                pygame.quit()
                                sys.exit()
                        
                pp = 0        
                temp = f.read(1)
                
                while(temp):
                        string1.append(temp)
                        temp=f.read(1)


                        
                print string1         
                if('p' in string1):
                        print "unlocked"
                
                if(screen_state==0):         
                #if touchscreen pressed
                        
                        if(event.type == pygame.MOUSEBUTTONDOWN):
			#get position
                                
                               # pygame.draw.line(screen, blue2, (pos[0],pos[1]),(new_position[0],new_position[1]),4)    
                                pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                                print pos
                                #print "touched"
                                #print pos
                                
                                #check in which area (button) the touchscreen was touched
                                #each area/button = 55x55px
                                if 7 <= pos[0] <= 47 and 7 <= pos[1] <= 47:
                                       
                                        if(fflag==0):
                                                old_position = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                                                new_position = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                                        else:
                                                
                                                old_position = new_position
                                                new_position = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                                               
                                        
                                        
                                        fflag = 1
                                        if(choose_door == 0):
                                                temp_pass = temp_pass*10 + 1
                                                print temp_pass
                                        if(choose_door == 1):
                                                choose_door = 0
                                                door_output = 12
                                                print "door 1 selected" 
                                        time.sleep(0.2)

                                if 57 <= pos[0] <= 97 and 7 <= pos[1] <= 47:                                       
                                        if(fflag==0):
                                                old_position = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                                                new_position = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                                        else:
                                                old_position = new_position
                                                new_position = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                                                pygame.draw.line(screen,blue,old_position,new_position,4)
                                        
                                        fflag = 1
                                        temp_pass = temp_pass*10 + 2
                                        time.sleep(0.2)
                                        
                                if  107 <= pos[0] <= 147 and 7 <= pos[1] <= 47:
                                                                               
                                        if(fflag==0):
                                                old_position = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                                                new_position = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                                        else:
                                                old_position = new_position
                                                new_position = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                                                pygame.draw.line(screen,blue,old_position,new_position,4)
                                        fflag = 1
                                        temp_pass = temp_pass*10 + 3
                                        time.sleep(0.2)
                                        

                                        
                                if 245 <= pos[0] <= 300 and 5 <= pos[1] <= 60:
                                        gpio_state13 = not gpio_state13
                                        if gpio_state13 == True:
                                                GPIO.output(13, GPIO.HIGH)
                                                state_color5 = green
                                                time.sleep(0.2)
                                        else:
                                                GPIO.output(13, GPIO.LOW)
                                                state_color5 = red
                                                time.sleep(0.2)
                                                
                                if 7 <= pos[0] <= 47 and 57 <= pos[1] <= 97:                                                                               
                                        if(fflag==0):
                                                old_position = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                                                new_position = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                                        else:
                                                old_position = new_position
                                                new_position = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                                                pygame.draw.line(screen,blue,old_position,new_position,4)
                                        fflag = 1
                                        temp_pass = temp_pass*10 + 4
                                        time.sleep(0.2)
                                        
                                if 57 <= pos[0] <= 97 and 57 <= pos[1] <= 97:
                                        if(fflag==0):
                                                old_position = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                                        else:
                                                old_position = new_position
                                                new_position = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                                        fflag = 1
                                        temp_pass = temp_pass*10 + 5
                                        time.sleep(0.2)

                                if 107 <= pos[0] <= 147 and 57 <= pos[1] <= 97:
                                        if(fflag==0):
                                                old_position = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])

                                        else:
                                                old_position = new_position
                                                new_position = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                                        fflag = 1
                                        temp_pass = temp_pass*10 + 6
                                        time.sleep(0.2)
                                        
                                if 7 <= pos[0] <= 47 and 107 <= pos[1] <= 147:
                                        if(fflag==0):
                                                old_position = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])

                                        else:
                                                old_position = new_position
                                                new_position = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                                        fflag = 1
                                        temp_pass = temp_pass*10 + 7
                                        time.sleep(0.2)
                                        
                                if 57 <= pos[0] <= 97 and 107 <= pos[1] <= 147:
                                        if(fflag==0):
                                                old_position = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])

                                        else:
                                                old_position = new_position
                                                new_position = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                                        fflag = 1
                                        temp_pass = temp_pass*10 + 8
                                        time.sleep(0.2)
                                        
                                if 107 <= pos[0] <= 157 and 107 <= pos[1] <= 147:
                                        if(fflag==0):
                                                old_position = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])

                                        else:
                                                old_position = new_position
                                                new_position = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
                                        fflag = 1
                                        temp_pass = temp_pass*10 + 9
                                        print temp_pass
                                        time.sleep(0.2)

                                if  165 <= pos[0] <= 220 and 10 <= pos[1] <= 40:
                                        os.system('arecord -D plughw:1 --duration=10 -f cd test.wav')
                                if  165 <= pos[0] <= 220 and 50 <= pos[1] <= 70:
                                        os.system('aplay -D plughw:0  test.wav')

                                if  165 <= pos[0] <= 220 and 70 <= pos[1] <= 110:
                                        choose_door = 1
                                        print "changing door to"
                        print "here"
                        if event.type == pygame.MOUSEBUTTONUP:
                                label_4 = font.render("Not authentiacated", 1, red)
                                label_5 = font.render("Not authentiacated", 1, red)
                                if(password == temp_pass):                           
                                        GPIO.output(4, GPIO.HIGH)
                                        label_4 = font.render("You may enter", 1, green)
                                        screen.blit(label_5,(200,200))
                                        print("happening") 
                                else:
                                          screen.blit(label_4,(200,200))
                               # pygame.draw.circle(screen, black, (200,200), 40,8)
                                
        #nge indicator's color if input changes (LOW = red, HIGH = green)
                if GPIO.input(16) == 1:
                        
                        state_color6 = green
                else:
                
                        state_color6 = red
                if GPIO.input(19) == 1:
                        
                        state_color7 = green
                else:
                        state_color7 = red
                if GPIO.input(20) == 1:
                        
                        state_color8 = green
                else:
                        state_color8 = red
                if GPIO.input(21) == 1:
      
                        state_color9 = green
                else:
                        print "Uploading photo to twitter...\n"
                        ret = subprocess.call(snapCommand,shell=True)
                        photo = open(IMG_NAME,'rb')
                        media_status = api.upload_media(media=photo)

                        time_now = time.strftime("%H:%M:%S") # get current time
                        date_now =  time.strftime("%d/%m/%Y") # get current date
                        tweet_txt = "Photo captured by @smartdoor445 at " + time_now + " on " + date_now

                        print "Posting tweet with picture...\n"
                        api.update_status(media_ids=[media_status['media_id']], status=tweet_txt)

		#deprecated method replaced by upload_media() and update_status()
                #media_ids=[media_status['media_id']] media_ids=[media_status['media_id']]api.update_status_with_media(media_ids=[media_status['media_id']], status=tweet_txt)

		# signal program ready
                        print "Done - System ready again.\n" 
                        state_color9 = red
                if GPIO.input(26) == 1:
                        
                        state_color10 = green
                else:
                        state_color10 = red
                        
                
                
                
                        
        #lets draw some buttons and indicators
                pygame.draw.circle(screen, blue2, (27,27), 20,0)
                pygame.draw.circle(screen, blue2, (77,27), 20,0)
                pygame.draw.circle(screen, blue2, (127,27), 20,0)
                
                #pygame.draw.rect(screen, cyan , (185,   5,  55,  25))
                pygame.draw.circle(screen, blue2, (27,77), 20,0)
                pygame.draw.circle(screen, blue2, (77,77), 20,0)
                pygame.draw.circle(screen, blue2, (127,77), 20,0)
                #pygame.draw.rect(screen, cyan , (245,   5,  55,  25))


                pygame.draw.circle(screen, blue2, (27,127), 20,0)
                pygame.draw.circle(screen, blue2, (77,127), 20,0)
                pygame.draw.circle(screen, blue2, (127,127), 20,0)


                
                #pygame.draw.rect(screen, cyan , ( 65,   75,  55,  25))
                #pygame.draw.rect(screen, cyan , (125,   75,  55,  25))
                #pygame.draw.rect(screen, cyan , (185,   75,  55,  25))
                #pygame.draw.rect(screen, cyan , (245,   75,  55,  25))
        
                #pygame.draw.rect(screen, state_color1 , (  5,   30,  55,  25))
                #pygame.draw.rect(screen, state_color2 , ( 65,   30,  55,  25))
                #pygame.draw.rect(screen, state_color3 , (125,   30,  55,  25))
                #pygame.draw.rect(screen, state_color4 , (185,   30,  55,  25))
                #pygame.draw.rect(screen, state_color5 , (245,   30,  55,  25))
                #pygame.draw.rect(screen, state_color6 , (  5,   100,  55,  25))
                #pygame.draw.rect(screen, state_color7 , ( 65,   100,  55,  25))
                #pygame.draw.rect(screen, state_color8 , (125,   100,  55,  25))
                pygame.draw.rect(screen, state_color9 , (185,   100,  55,  25))
                #pygame.draw.rect(screen, state_color10 , (245,   100,  55,  25))
                #pygame.draw.circle(screen, red2, (100,145), 15,0)
                #pygame.draw.circle(screen, blue2, (135,145), 15,0)
                #pygame.draw.circle(screen, blue2, (170,145), 15,0)

            
        #create some labels for buttons
                label1 = font.render ("1", 1, black)
                label2 = font.render ("2", 1, black)
                label3 = font.render ("3", 1, black)
                label4 = font.render ("4", 1, black)
                label5 = font.render ("5", 1, black)
                label6 = font.render ("6", 1, black)
                label7 = font.render ("7", 1, black)
                label8 = font.render ("8", 1, black)
                label9 = font.render ("9", 1, black)
                label10 = font.render ("0", 1, black)
                label_1 = font.render("Record", 1, white)
                label_2 = font.render("Play message", 1, white)
                label_3 = font.render("Choose Door", 1, white)
                
        
        #display labels
                screen.blit(label1, (  22,   15))
                screen.blit(label2, ( 70,   15))
                screen.blit(label3, (125,   15))
                screen.blit(label4, (22,   65))
                screen.blit(label5, (70,   65))
                screen.blit(label6, (125,  65))
                screen.blit(label7, ( 22,  115))
                screen.blit(label8, (70,  115))
                screen.blit(label9, (125,  115))
                screen.blit(label10, (245,  75))                        
                screen.blit(label_1,(185,20))
                screen.blit(label_2,(185,45))
                screen.blit(label_3,(185,80))
              
        
        #refresh screen        
                pygame.display.update()
                time.sleep(0.01)
