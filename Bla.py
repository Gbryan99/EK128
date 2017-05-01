import os
import pygame
import time
import pygame, pygame.font, pygame.event, pygame.draw
import random

from pygame.locals import *

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))  # This creates a 800x600 pixel display
pygame.display.set_caption('EK 128 Flashcard Project')  # Our game title

clock = pygame.time.Clock()

# Define the colors we use for our screen display
yellow = (255, 255, 0)
green = (50, 205, 50)
white = (255, 255, 255)
blue = (175, 238, 238)
orange = (255, 165, 0)
purple = (123, 104, 238)
red = (255, 0, 0)
black = (0, 0, 0)

bright_orange = (238, 232, 170)
bright_purple = (230, 230, 250)
bright_yellow = (238, 221, 130)
bright_red = (255, 192, 203)

display_width = 800
display_height = 600


mouse_x = None
mouse_y = None
mouse_clicked = False

# load answer info from file
answers = {}
lines = []
with open('answer_key.txt', 'rb') as afile:
    lines = afile.readlines()
for line in lines:
    sline = line.rstrip()
    values = sline.split(',')
    answers[values[0]] = values[1]


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width * 0.5), (display_height * 0.5))
    gameDisplay.blit(TextSurf, TextRect)

    time.sleep(2)

    game_loop()


# This button function will allow the buttons on the screen to be interactive
def button(msg, x, y, w, h, inactColor, actColor, action=None):
    """msg = button message
    x = x coordinates of button location
    y = y coordinates of button location
    Buttons are all rectangles in this game with width w and height h
    inactColor = inactive color
    actColor = active color
    action = the function that is executed when the button is clicked"""

    # mouse[0] gives the x coordinates of the mouse location
    # mouse[1] gives the y coordinates of the mouse location

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:  # This defines the boundary of our w x h button
        pygame.draw.rect(gameDisplay, actColor, (x, y, w, h))  # button lights up
        if click[0] == 1 and action != None:  # click[0] is the left mouse click
            action()


    else:
        pygame.draw.rect(gameDisplay, inactColor, (x, y, w, h))  # button (normal: does not light up)

    smallText = pygame.font.Font("freesansbold.ttf", 25)  # Size 25 font
    textSurface, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w * 0.5)), (y + (h * 0.5)))  # Position the text inside the button
    gameDisplay.blit(textSurface, textRect)


def button_small(msg, x, y, w, h, inactColor, actColor,
                 action=None):  # same as button function but for buttons with smaller texts (ie size 10 fonts)

    """msg = button message
    x = x coordinates of button location
    y = y coordinates of button location
    Buttons are all rectangles in this game with width w and height h
    inactColor = inactive color
    actColor = active color
    action = the function that is executed when the button is clicked"""

    # mouse[0] gives the x coordinates of the mouse location
    # mouse[1] gives the y coordinates of the mouse location

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:  # This defines the boundary of our w x h button
        pygame.draw.rect(gameDisplay, actColor, (x, y, w, h))  # button lights up
        if click[0] == 1 and action != None:  # click[0] is the left mouse click
            action()

    else:
        pygame.draw.rect(gameDisplay, inactColor, (x, y, w, h))  # button (normal: does not light up)

    smallText = pygame.font.Font("freesansbold.ttf", 10)  # Size 10 font
    textSurface, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w * 0.5)), (y + (h * 0.5)))  # Position the text inside the button
    gameDisplay.blit(textSurface, textRect)


def game_intro():  # Game intro page (Like a main menu page)

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(blue)  # Makes intro page background blue
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf, TextRect = text_objects("Your Personal Flashcards", largeText)
        TextRect.center = ((display_width * 0.5), (display_height * 0.5))
        gameDisplay.blit(TextSurf, TextRect)

        button("START", 150, 450, 100, 50, orange, bright_orange, game_loop)
        button_small("About the Game", 550, 450, 100, 50, purple, bright_purple, userinput)

        mouse = pygame.mouse.get_pos()

        pygame.display.update()
        clock.tick(15)


def userinput():
    userinp = True

    while userinp:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()

        clock.tick(15)


def aboutpage():  # This will be the page that provides informationabout the game
    gameEx = False
    while not gameEx:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameEx = True


file = open("termfile.txt", "w+")


def game_loop():
    gameExit = False
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True


        # pick question
        question = '' # should be randomly selected from answers keys
        # pick answers
        user_answers = ['uno', 'dos', 'tres', 'cuatro']
        # correct answer = answers[question]

        # pick 3 random incorrect answers


        # shuffle answers
        # random.shuffle(answers)




        gameDisplay.fill((255, 255, 255))  # This sets the background of the display to plain white color

        # assign an answer to each button
        gameDisplay.fill(yellow,
                         rect=[30, 30, 150, 150])  # This draws a yellow box (which will act as a flashcard) AnsOption1
        gameDisplay.fill(yellow, rect=[230, 30, 150, 150])  # This flashcard is an answer option. AnsOption2
        gameDisplay.fill(yellow, rect=[430, 30, 150, 150])  # AnsOption 3
        gameDisplay.fill(yellow, rect=[630, 30, 150, 150])  # AnsOption 4
        gameDisplay.fill(green, rect=[330, 330, 150, 150])  # This flashcard displays the term. Termcard

        # get value of answer from button click (0, 1, 2, 3)
        button_number = 0
        
        # select users's answer from answers list using input #
        given_answer = user_answers[button_number]
        
        # check if correct
        if answers[question] == given_answer:
            #congratulate the user
            pass
        else:
            #dispense punishment
            pass

        button("Main Menu", 30, 530, 150, 50, red, bright_red, game_intro)  # Main Menu

        pygame.display.update()


game_intro()
userinput()
game_loop()
pygame.quit()
quit()
