import pygame
from pygame.locals import *

Screen=pygame.display.set_mode((800,700))
pygame.display.set_caption('Tic Tac Toe')

surface = pygame.Surface((100, 100),SRCALPHA)
clock = pygame.time.Clock()

color = (0,0,0)
x = 300
y = 250
count=0
column_list=[]
Player1Columns=[]
Player2Columns=[]
Game="START"
#pygame.mixer.init(44100, -16,2,2048)
#pygame.mixer.music.load('Titli.mp3')
#pygame.mixer.music.play(0)

image=pygame.image.load('python.png')

pygame.font.init()
font = pygame.font.SysFont("comicsansms", 52)
text1 = font.render("Welcome to Tic Toc", True, (0, 128, 0))
text2 = font.render("Player1", True, (250, 0, 0))
text3 = font.render("Player2", True, (0, 0, 250))
text4 = font.render("X", True, (0, 128, 0))
text5 = font.render("O", True, (0, 128, 0))
textempty = font.render("Player1",True, (255,255,255))
textempty1 = font.render("Player2",True, (255,255,255))
text6 = font.render("Already Marked", True, (0, 128, 0))
text6empty = font.render("Already Marked", True, (255, 255, 255))
text7 = font.render("Player1 Won!!", True, (250, 0, 0))
text8 = font.render("Player2 Won!!", True, (0, 0, 250))
text9 = font.render("No one Won!!", True, (0, 128, 0))

def text_objects(text, font):
    textSurface = font.render(text, True, (0,128,0))
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(Screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(Screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    Screen.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def PlayerMark(column):
    global count
    Screen.blit(text6empty, (350, 150))
    Screen.blit(textempty, (350, 90))
    Screen.blit(textempty1, (350, 90))
    if count % 2 == 1:
        if DrawSymbol(column,2):
            Screen.blit(text2, (350, 90))
            count += 1
    else:
        if DrawSymbol(column,1):
            Screen.blit(text3, (350, 90))
            count += 1

def DrawSymbol(column,player):
    global column_list
    global Player1Columns
    global Player2Columns
    global Game

    if column not in column_list:
        column_list.append(column)
        if player == 1:
            Screen.blit(text4, column)
            Player1Columns.append(column)
            markcountx = 0
            markcounty = 0
            for i in range(len(Player1Columns)):
                if Player1Columns[i][0] == column[0]:
                    markcountx += 1
                if Player1Columns[i][1] == column[1]:
                    markcounty += 1
            if markcountx == 3:
                Screen.blit(text7, (350, 150))
                Game="STOP"
                return False
            elif markcounty == 3:
                Screen.blit(text7, (350, 150))
                Game = "STOP"
                return False
            elif (330,270) in Player1Columns and ((430,370) in Player1Columns and ((530,470) in Player1Columns)):
                Screen.blit(text7, (350, 150))
                Game = "STOP"
                return False
            elif (530,270) in Player1Columns and ((430,370) in Player1Columns and ((330,470) in Player1Columns)):
                Screen.blit(text7, (350, 150))
                Game = "STOP"
                return False
            else:
                if len(column_list)>=9:
                    Screen.blit(text9, (350, 150))
                    Game="STOP"
                    return False


        else:
            Screen.blit(text5, column)
            Player2Columns.append(column)
            markcountx = 0
            markcounty = 0
            for i in range(len(Player2Columns)):
                if Player2Columns[i][0] == column[0]:
                    markcountx += 1
                if Player2Columns[i][1] == column[1]:
                    markcounty += 1
            if markcountx == 3:
                Screen.blit(text8, (350, 150))
                Game = "STOP"
                return False
            elif markcounty == 3:
                Screen.blit(text8, (350, 150))
                Game = "STOP"
                return False
            elif (330, 270) in Player2Columns and ((430, 370) in Player2Columns and ((530, 470) in Player2Columns)):
                Screen.blit(text8, (350, 150))
                Game = "STOP"
                return False
            elif (530, 270) in Player2Columns and ((430, 370) in Player2Columns and ((330, 470) in Player2Columns)):
                Screen.blit(text8, (350, 150))
                Game = "STOP"
                return False
            else:
                if len(column_list)>=9:
                    Screen.blit(text9, (350, 150))
                    Game="STOP"
                    return False
        return True
    else:
        Screen.blit(text6, (350, 150))
        if player == 1:
            Screen.blit(text2, (350, 90))
        else:
            Screen.blit(text3, (350, 90))
        return False
def gameloop():
    Screen.fill((255, 255, 255))
    Screen.blit(image, (20, 20))
    Screen.blit(text1, (250, 20))
    Screen.blit(text2, (350, 90))
    pygame.draw.rect(Screen, color, pygame.Rect(x, y, 300, 300), 10)
    pygame.draw.line(Screen, color, (400, 250), (400, 550), 10)
    pygame.draw.line(Screen, color, (500, 250), (500, 550), 10)
    pygame.draw.line(Screen, color, (300, 350), (600, 350), 10)
    pygame.draw.line(Screen, color, (300, 450), (600, 450), 10)
    global column_list
    column_list = []
    global Player1Columns
    Player1Columns = []
    global Player2Columns
    Player2Columns = []
    global Game
    Game = "START"
    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type==QUIT or (event.type==KEYDOWN and (event.key==K_ESCAPE) ):
                pygame.quit()
                quit()
            elif event.type==KEYDOWN and (event.key==K_s):
                pygame.mixer.music.stop()


            if Game=="START":
                if (event.type==MOUSEBUTTONDOWN and (event.button==1)):
                    pos=event.pos
                    if(pos[0]>300 and pos[0]<400) and (pos[1]>250 and pos[1]<350):
                        PlayerMark((330,270))
                    elif (pos[0]>400 and pos[0]<500) and (pos[1]>250 and pos[1]<350):
                        PlayerMark((430,270))
                    elif (pos[0]>500 and pos[0]<600) and (pos[1]>250 and pos[1]<350):
                        PlayerMark((530,270))
                    elif (pos[0]>300 and pos[0]<400) and (pos[1]>350 and pos[1]<450):
                        PlayerMark((330,370))
                    elif (pos[0]>400 and pos[0]<500) and (pos[1]>350 and pos[1]<450):
                        PlayerMark((430,370))
                    elif (pos[0]>500 and pos[0]<600) and (pos[1]>350 and pos[1]<450):
                        PlayerMark((530,370))
                    elif (pos[0]>300 and pos[0]<400) and (pos[1]>450 and pos[1]<550):
                        PlayerMark((330,470))
                    elif (pos[0]>400 and pos[0]<500) and (pos[1]>450 and pos[1]<550):
                        PlayerMark((430,470))
                    elif (pos[0]>500 and pos[0]<600) and (pos[1]>450 and pos[1]<550):
                        PlayerMark((530,470))

            else:
                button("Play Again!", 150, 600, 100, 50, (0, 200, 0), (0, 255, 0), gameloop)
                button("Quit", 550, 600, 100, 50, (255, 0, 0), (200, 0, 0), quitgame)

        pygame.display.update()
        clock.tick(60)

gameloop()
pygame.quit()
quit()





