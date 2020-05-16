import getpass
Username = getpass.getuser()
print(Username)

#Test Commit


"""I wanted to devolep a portable game that did not need any sprits or sounds to be downloaded and not have to be compiled"""
import random, pygame, math, sys
from random import seed
from random import randint
import os.path
from os import path
import winsound


beep = tone.create('C1', 0.1) #// a few sounds i will use other than winsouds
beep.set_volume(1)
beep2 = tone.create('F#3', 0.1) #// a few sounds i will use other than winsouds
beep2.set_volume(1)
beep3 = tone.create('D3', 0.1) #// a few sounds i will use other than winsouds
beep3.set_volume(1)
#music.queue(beep)
Time_Then_Red = 0
Time_Then_Blue = 0
txt = ('.txt')


#// a few test
# pygame.display.update() / pygame.display.flip() gameDisplay.fill() keys = pygame.key.get_pressed() pygame.draw.line(gameDisplay, color, start_position, end_position, width)
#def draw(self):
#self.screen.fill(self.color)# clear screen
#self.draw(self.screen)# draw updated screen

# pygame.init()

#// colours (colors) (r,g,b)
white = (255,255,255)
white_o = (255,255,255)
black = (0,0,0)
red = ( 255,0,0)
green = ( 0,255,0)
blue = (0,0,255)
brown = (150,75,0)
gray = (112.95,112.95,112.95)
yellow = (255,255,0)

#// Display Settings
display_width, display_height = 1366, 768
gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)  #// I found that you could actually put the name of the game at the top of the screen
pygame.display.set_caption("Counter Strike Global Blocks")

menu = True  #// setting varible to true

fps = pygame.time.Clock()   #// can read measure ticks by time

font = pygame.font.Font(("C:\\Users\\"+Username+"\\AppData\\Local\\Microsoft\\Windows\\Fonts\\IBMPlexSans-Regular.ttf"), 40)   #// small font       #// Imported Font that i like
fontGameEnd = pygame.font.Font(("C:\\Users\\"+Username+"\\AppData\\Local\\Microsoft\\Windows\\Fonts\\IBMPlexSans-Regular.ttf"), 200) #// Big font

def title(msg, color):      #// this defines functions used to draw a title
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [1, 10])
def controls_one(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [100, 200])
def controls_two(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [100, 300])
def escape_control(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [100, 400])
def bluescore(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [1035, 10])
def redscore(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [1115, 10])
def GameOver(msg, color):
    screen_text = fontGameEnd.render(msg, True, color)
    gameDisplay.blit(screen_text, [150, 200])
def LastWinnerTitle(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [100, 500])
def LastWinner(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [100, 550])
def LastScoreTitleBlue (msg, color):
    screen_text = font.render(str(msg), True, color)
    gameDisplay.blit(screen_text, [200, 550])
def LastScoreBreak (msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [300, 550])
def LastScoreTitleRed (msg, color):
    screen_text = font.render(str(msg), True, color)
    gameDisplay.blit(screen_text, [350, 550])


    #// for winning menus buttons
def replay_button(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [200, 600])
def exit_button(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [850, 600])
def menu_button(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [525, 600])


def mainMenu():
    while menu:
        #[x, y], [1, 0, 0]
        gameDisplay.fill(brown)     #// Fills Background
        pygame.draw.line(gameDisplay, gray, (0, 0), (0, 800), 200)  #// play button and GUI/Menu screen
        pygame.draw.circle(gameDisplay, white_o, (50, 150), 30)
        pygame.draw.polygon(gameDisplay, gray, [(37,137), (37,163), (70,150)], 0)
        title("CSGB", black)    #//Refers back to functions for colour and x, y
        controls_one ("Up, Down, Left, Right to move player one and slash to shoot", red)
        controls_two ("W, A, S, D to move player two and E to shoot", blue)
        escape_control ("If at any point you need to quit press esc.", white)
        existing_game = path.exists("WinnerColourData"+txt)
        if existing_game == True:
            LastWinnerTitle ("Last Winner:", black)
            with open("WinnerColourData"+txt, "r") as rwcdf:
                with open ("LastScoreTitleBlueData"+txt, "r") as rlstbdf:       #// prints previous score
                    with open ("LastScoreTitleRedData"+txt, "r") as rlstrdf:
                        LastScoreBlue = rlstbdf.readlines()
                        LastScoreRed = rlstrdf.readlines()
                        WinnerColour = rwcdf.readlines()
                        LastScoreTitleBlue (LastScoreBlue, blue)
                        LastScoreBreak ("-", black)
                        LastScoreTitleRed (LastScoreRed, red)
                        if (WinnerColour[0]) == "Red":
                            LastWinner ((WinnerColour[0]), red)
                        if (WinnerColour[0]) == "Blue":
                            LastWinner ((WinnerColour[0]), blue)
                        else:
                            pass

        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
            pygame.quit()
            sys.exit()

        for event in pygame.event.get():  #// Listens if event game is quited to quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        pygame.display.update()     #// Looking to see were mouse is clicked and if on button
        pos, pressed = pygame.mouse.get_pos(), pygame.mouse.get_pressed()
        if 20 <= pos[0] <= 80 and 120 <= pos[1] <= 180 and pressed[0] == 1:
            winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
            gameSystem() #// runs function

    fps.tick(120)   #// changes tick speed
    pygame.display.update() #// runs function

def gameSystem():
    lead_x = 12.5 #// all of this defines speeds and changes x and y for bullets and players
    lead_y = 410
    lead_x_change = 0
    lead_y_change = 0
    lead_x2 = 968.25
    lead_y2 = 390
    lead_x2_change = 0
    lead_y2_change = 0
    redBullet_counter = 0
    redBullet_x = 0         #// Please notice each player can only have 5 bullets so everything has to be defined separately
    redBullet_y = -10
    redBullet_x2 = 0
    redBullet_y2 = -10
    redBullet_x3 = 0
    redBullet_y3 = -10
    redBullet_x4 = 0
    redBullet_y4 = -10
    redBullet_x5 = 0
    redBullet_y5 = -10
    blueBullet_counter = 0      #// Bullet counters for each player to see amount of bullets in game
    blueBullet_x = 0
    blueBullet_y = -19
    blueBullet_x2 = 0
    blueBullet_y2 = -19
    blueBullet_x3 = 0
    blueBullet_y3 = -19
    blueBullet_x4 = 0
    blueBullet_y4 = -19
    blueBullet_x5 = 0
    blueBullet_y5 = -19  #// Defines scores also defines some button positions
    blueScore = 0
    redScore = 0
    rePlay_x = 200      #// press to replay
    rePlay_y = 600
    endGame_x = 850      #// press to endgame
    endGame_y = 600
    menuButton_x = 525        #// press to go to menu
    menuButton_y = 600
    gameOn = True

    while gameOn:
        global Time_Then_Red
        global Time_Then_Blue
        gameDisplay.fill(black) #// black background
        bluescore(str(blueScore), blue) #// print blue and red score
        redscore(str(redScore), red)
        pygame.draw.line(gameDisplay, green, (1002.5,0), (1002.5, 800), 5) #// draw sideline
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP: #// A Key being let go
                if event.key == pygame.K_LEFT:  #// key left let go of?
                    lead_x2_change = 0          #// resets varible for going left
                if event.key == pygame.K_RIGHT: #// so on...
                    lead_x2_change = 0
                if event.key == pygame.K_UP:
                    lead_y2_change = 0
                if event.key == pygame.K_DOWN:
                    lead_y2_change = 0
                if event.key == pygame.K_a:
                    lead_x_change = 0
                if event.key == pygame.K_d:
                    lead_x_change = 0
                if event.key == pygame.K_w:
                    lead_y_change = 0
                if event.key == pygame.K_s:
                    lead_y_change = 0
                if event.key == pygame.K_SLASH: #// has key / been pressed?
                   beep.play()
                   beep.play()
                   beep.play()#// play bullet sound
                   if redBullet_counter == 0:#// counts bullets
                       redBullet_x = lead_x2 - 15 #// were player is + 25 x space
                       redBullet_y = lead_y2 + 8 #// were player is + 25 y space
                       redBullet_counter += 1 #// add to bullet counter
                   elif redBullet_counter == 1: #// for next bullet and so on...
                       redBullet_x2 = lead_x2 - 15
                       redBullet_y2 = lead_y2 + 8
                       redBullet_counter += 1
                   elif redBullet_counter == 2:
                       redBullet_x3 = lead_x2  - 15
                       redBullet_y3 = lead_y2 + 8
                       redBullet_counter += 1
                   elif redBullet_counter == 3:
                       redBullet_x4 = lead_x2 - 15
                       redBullet_y4 = lead_y2 + 8
                       redBullet_counter += 1
                   elif redBullet_counter == 4:
                       redBullet_x5 = lead_x2 - 15
                       redBullet_y5 = lead_y2 + 8
                       redBullet_counter = 0
                if event.key == pygame.K_e: #// has key e been pressed?
                   beep.play()
                   beep.play()
                   beep.play()#// play bullet sound
                   if blueBullet_counter == 0: #// counts bullets
                       blueBullet_x = lead_x + 25 #// were player is + 25 x space
                       blueBullet_y = lead_y + 8 #// were player is + 25 y space
                       blueBullet_counter += 1 #// add to bullet counter
                   elif blueBullet_counter == 1: #// for next bullet and so on...
                       blueBullet_x2 = lead_x + 25
                       blueBullet_y2 = lead_y + 8
                       blueBullet_counter += 1
                   elif blueBullet_counter == 2:
                       blueBullet_x3 = lead_x + 25
                       blueBullet_y3 = lead_y + 8
                       blueBullet_counter += 1
                   elif blueBullet_counter == 3:
                       blueBullet_x4 = lead_x + 25
                       blueBullet_y4 = lead_y + 8
                       blueBullet_counter += 1
                   elif blueBullet_counter == 4:
                       blueBullet_x5 = lead_x + 25
                       blueBullet_y5 = lead_y + 8
                       blueBullet_counter = 0

        blueBullet_x = blueBullet_x + 20        #//bullets moving forward
        blueBullet_x2 = blueBullet_x2 + 20
        blueBullet_x3 = blueBullet_x3 + 20
        blueBullet_x4 = blueBullet_x4 + 20
        blueBullet_x5 = blueBullet_x5 + 20

        redBullet_x = redBullet_x - 20
        redBullet_x2 = redBullet_x2 - 20
        redBullet_x3 = redBullet_x3 - 20
        redBullet_x4 = redBullet_x4 - 20
        redBullet_x5 = redBullet_x5 - 20
        #// one of player reds bullets hit blue
        if (redBullet_x >= lead_x - 4 and redBullet_x <= lead_x + 24 and redBullet_y >= lead_y - 4 and redBullet_y <= lead_y + 24 or redBullet_x2 >= lead_x - 4 and redBullet_x2 <= lead_x + 24 and redBullet_y2 >= lead_y - 4 and redBullet_y2 <= lead_y + 24 or
        redBullet_x3 >= lead_x - 4 and redBullet_x3 <= lead_x + 24 and redBullet_y3 >= lead_y - 4 and redBullet_y3 <= lead_y + 24 or redBullet_x4 >= lead_x - 4 and redBullet_x4 <= lead_x + 24 and redBullet_y4 >= lead_y - 4 and redBullet_y4 <= lead_y + 24 or
        redBullet_x5 >= lead_x - 4 and redBullet_x5 <= lead_x + 24 and redBullet_y5 >= lead_y - 4 and redBullet_y5 <= lead_y + 24):
            """ The problem i had with player red was that the bullet would hit twice and give you 2 points so i created this to stop that and becuase of that i did not add it to blue"""
            Time_Now_Red = pygame.time.get_ticks()      #//This is a falesafe so a player dosent get two points off one shot
            if Time_Now_Red - Time_Then_Red >= 200:     #// has it been 200 milliseconds since last shot
                Time_Then_Red = pygame.time.get_ticks()         #// Reset time of last hit
            else:
                redScore += 1
                pygame.time.wait(100)
                lead_x = 12.5
                lead_y = 410
                lead_x2 = 968.25
                lead_y2 = 390
                Time_Then_Red = pygame.time.get_ticks()
                beep2.play()
                beep3.play()
        #// one of player blue bullets hit red
        if (blueBullet_x >= lead_x2 - 4 and blueBullet_x <= lead_x2 + 24 and blueBullet_y >= lead_y2 - 4 and blueBullet_y <= lead_y2 + 24 or blueBullet_x2 >= lead_x2 - 4 and blueBullet_x2 <= lead_x2 + 24 and blueBullet_y2 >= lead_y2 - 4 and blueBullet_y2 <= lead_y2 + 24
        or blueBullet_x3 >= lead_x2 - 4 and blueBullet_x3 <= lead_x2 + 24 and blueBullet_y3 >= lead_y2 - 4 and blueBullet_y3 <= lead_y2 + 24 or blueBullet_x4 >= lead_x2 - 4 and blueBullet_x4 <= lead_x2 + 24 and blueBullet_y4 >= lead_y2 - 4 and blueBullet_y4 <= lead_y2 + 24
        or blueBullet_x5 >= lead_x2 - 4 and blueBullet_x5 <= lead_x2 + 24 and blueBullet_y5 >= lead_y2 - 4 and blueBullet_y5 <= lead_y2 + 24):
            blueScore += 1
            lead_x = 12.5
            lead_y = 410
            lead_x2 = 968.25
            lead_y2 = 390
            beep2.play()
            beep3.play()

        if redScore == 20:   #// when does game end
            gameDisplay.fill(black)
            GameOver("Red Wins", red)
            gameOn = False      #// ends game and sets it to false
            with open("WinnerColourData"+txt, "w") as wwcdf:        #// saves the scores and last player to win to a .txt file
                with open ("LastScoreTitleBlueData"+txt, "w") as rlstbdf:
                    with open ("LastScoreTitleRedData"+txt, "w") as rlstrdf:
                        rlstbdf.truncate(0)
                        rlstrdf.truncate(0)
                        rlstbdf.write(str(blueScore))
                        rlstrdf.write(str(redScore))
                        wwcdf.truncate(0)
                        wwcdf.write ('Red')
        if blueScore == 20:     #// when does game end
            gameDisplay.fill(black)
            GameOver("Blue Wins", blue)
            gameOn = False #// ends game and sets it to false
            with open("WinnerColourData"+txt, "w") as wwcdf:    #// saves the scores and last player to win to a .txt file
                with open ("LastScoreTitleBlueData"+txt, "w") as rlstbdf:
                    with open ("LastScoreTitleRedData"+txt, "w") as rlstrdf:
                        rlstbdf.truncate(0)
                        rlstrdf.truncate(0)
                        rlstbdf.write(str(blueScore))
                        rlstrdf.write(str(redScore))
                        wwcdf.truncate(0)
                        wwcdf.write ('Blue')


        #// player movement
        key = pygame.key.get_pressed() #// has key been pressed
        if key[ord('a')]: #// is it key a?
            lead_x_change = -13 #// move left
        if key[ord('d')]: #// so on...
            lead_x_change = 13
        if key[ord('w')]:
            lead_y_change = -9
        if key[ord('s')]:
            lead_y_change = 9
        if key[pygame.K_LEFT]:
            lead_x2_change = -13
        if key[pygame.K_RIGHT]:
            lead_x2_change = 13
        if key[pygame.K_UP]:
            lead_y2_change = -9
        if key[pygame.K_DOWN]:
            lead_y2_change = 9
        if key[pygame.K_ESCAPE]:
            winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
            pygame.quit()
            sys.exit()


        if lead_y <= 0: #// teleports to other side of screen and defines center block
            lead_y = 800
        elif lead_y >= 800:
            lead_y = 0
        if lead_y2 <= 0:
            lead_y2 = 800
        elif lead_y2 >= 800:
            lead_y2 = 0
        if lead_x <= 0:
            lead_x = 0
        if lead_x2 >= 980:
            lead_x2 = 980
        if lead_x >= 500:
            lead_x = 500
        if lead_x2 <= 500:
            lead_x2 = 500


        lead_x += lead_x_change  #// player x,y movment amounts
        lead_y += lead_y_change
        lead_x2 += lead_x2_change
        lead_y2 += lead_y2_change


        fps.tick(120) #// changes tick speed


        pygame.draw.rect(gameDisplay, blue, [ lead_x, lead_y, 20, 20]) #// draws blue player
        pygame.draw.rect(gameDisplay, red, [ lead_x2, lead_y2, 20, 20]) #// draws red player
        for bullet in [(redBullet_x, redBullet_y), (redBullet_x2, redBullet_y2), (redBullet_x3, redBullet_y3), (redBullet_x4, redBullet_y4), (redBullet_x5, redBullet_y5), #// draws all bullets
                        (blueBullet_x, blueBullet_y), (blueBullet_x2, blueBullet_y2), (blueBullet_x3, blueBullet_y3), (blueBullet_x4, blueBullet_y4), (blueBullet_x5, blueBullet_y5)]:
            pygame.draw.rect(gameDisplay, yellow, [bullet[0], bullet[1], 10, 5])
        pygame.display.update()


    while gameOn == False: #// when game ends
        if gameOn == False: #// if game ended
            pygame.draw.rect(gameDisplay, green, [rePlay_x, rePlay_y, 150, 50])     #// draws buttons in a rectangle
            pygame.draw.rect(gameDisplay, red, [endGame_x, endGame_y, 100, 50])
            pygame.draw.rect(gameDisplay, yellow, [menuButton_x, menuButton_y, 100, 50])
            replay_button("Replay", white) #// Labels Button
            exit_button("Exit", white)
            menu_button("Menu", white)

            pos, pressed = pygame.mouse.get_pos(), pygame.mouse.get_pressed() #// find mouse location and if pressed
            if endGame_x <= pos[0] <= endGame_x + 100 and endGame_y <= pos[1] <= endGame_y + 50 and pressed[0] == 1:    #//pos is the position of mouse and finds if button pressed
                winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
                pygame.quit()
                sys.exit()
            if rePlay_x <= pos[0] <= rePlay_x + 150 and rePlay_y <= pos[1] <= rePlay_y + 50 and pressed[0] == 1:
                winsound.PlaySound("SystemHand", winsound.SND_NOSTOP)
                gameSystem()

            if menuButton_x <= pos[0] <= menuButton_x + 100 and menuButton_y <= pos[1] <= menuButton_y + 50 and pressed[0] == 1:
                winsound.PlaySound("SystemHand", winsound.SND_NOSTOP)
                mainMenu()

            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
                pygame.quit()
                sys.exit()
            for event in pygame.event.get():        #// Find if quit button was pressed and if so exits game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


mainMenu()
