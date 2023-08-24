import sys
import pygame
import textwrap
from pygame.locals import*
from PIL import Image, ImageSequence

from button import Button
import time
import random

pygame.init()

# Stopwatch
stopwatch_font = pygame.font.Font(None, 36)  # Choose a font and size
stopwatch_start_time = pygame.time.get_ticks()
stopwatch_running = False
stopwatch_value = 0

#Screen Size:
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SPEED = 5

#Color variables
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Creating Screen Object
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("TzTok Jad Prayer Flicking Practice")

#main menu background image
mmbackground = pygame.image.load("C:\\Users\\presi\\PycharmProjects\\TzTokJadPrayerFlickingGame\\venv\\images\\mainmenu background.png")
mmbackground = pygame.transform.scale(mmbackground, (1280, 720))

#gameover background image
gameoverbackground = pygame.image.load("C:\\Users\\presi\\PycharmProjects\\TzTokJadPrayerFlickingGame\\venv\\images\\Lumbridge.png")
gameoverbackground = pygame.transform.scale(gameoverbackground, (1280, 720))

#Rendering Buttons and scaling them to size for main menu
playbutton = pygame.image.load("C:\\Users\\presi\\PycharmProjects\TzTokJadPrayerFlickingGame\\venv\\images\\play button.png")
playbutton = pygame.transform.scale(playbutton, (185, 105))
instructionsbutton = pygame.image.load("C:\\Users\\presi\\PycharmProjects\\TzTokJadPrayerFlickingGame\\venv\\images\\instructions button.png")
instructionsbutton = pygame.transform.scale(instructionsbutton, (185, 105))
exitbutton = pygame.image.load("C:\\Users\\presi\\PycharmProjects\\TzTokJadPrayerFlickingGame\\venv\\images\\exit button.png")
exitbutton = pygame.transform.scale(exitbutton, (425, 100))

#Rendering background for instructions
instructionsbackground = pygame.image.load("C:\\Users\\presi\\PycharmProjects\TzTokJadPrayerFlickingGame\\venv\\images\\instructions background.png")
instructionsbackground = pygame.transform.scale(instructionsbackground, (1280, 300))

#Rendering Play background
playbackground = pygame.image.load("C:\\Users\\presi\\PycharmProjects\TzTokJadPrayerFlickingGame\\venv\\images\\playFightCavesBG.PNG")
playbackground = pygame.transform.scale(playbackground, (1280, 720))

#render tooltips for play
tooltip = pygame.image.load("C:\\Users\\presi\\PycharmProjects\TzTokJadPrayerFlickingGame\\venv\\images\\tooltip.PNG")
tooltip_range = pygame.image.load("C:\\Users\\presi\\PycharmProjects\TzTokJadPrayerFlickingGame\\venv\\images\\tooltiprange.PNG")
tooltip_mage = pygame.image.load("C:\\Users\\presi\\PycharmProjects\TzTokJadPrayerFlickingGame\\venv\\images\\tooltipmage.PNG")

#render button for prayer and ranged in tooltip
prayerOnbutton = pygame.image.load("C:\\Users\\presi\\PycharmProjects\TzTokJadPrayerFlickingGame\\venv\\images\\prayerOn.png")
prayerOffbutton = pygame.image.load("C:\\Users\\presi\\PycharmProjects\TzTokJadPrayerFlickingGame\\venv\\images\\prayerOff.png")
rangedOnbutton = pygame.image.load("C:\\Users\\presi\\PycharmProjects\TzTokJadPrayerFlickingGame\\venv\\images\\rangedOn.PNG")
rangedOffbutton = pygame.image.load("C:\\Users\\presi\\PycharmProjects\TzTokJadPrayerFlickingGame\\venv\\images\\rangedOff.png")

#render in player sprite
playersprite = pygame.image.load("C:\\Users\\presi\\PycharmProjects\TzTokJadPrayerFlickingGame\\venv\\images\\Wise_Old_Man.png")
playersprite = pygame.transform.scale(playersprite, (75, 150))

def get_font(size):
    return pygame.font.Font("C:\\Users\\presi\\PycharmProjects\\TzTokJadPrayerFlickingGame\\venv\\images\\font.ttf",
                            size)

def runescape_font(size):
    return pygame.font.Font("C:\\Users\\presi\\PycharmProjects\\TzTokJadPrayerFlickingGame\\venv\\images\\runescape_uf.ttf",
                            size)

def mainmenu(): #Screen that pops up when game starts: Contains button to start game and exit game, and instructions button

    pygame.display.set_caption("TzTok-Jad Prayer Flicking Mini-Game")


    while True:
        DISPLAYSURF.blit(mmbackground, (0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))


        PLAY_BUTTON = Button(image = playbutton, pos = (530, 222), text_input="Play", font = runescape_font(15),
                             base_color= "#d7fcd4", hovering_color="RED")

        INSTRUCTIONS_BUTTON = Button(image = instructionsbutton, pos=(764, 222), text_input="Instructions", font= runescape_font(15),
                             base_color="#d7fcd4", hovering_color="RED")

        EXIT_BUTTON = Button(image = exitbutton, pos=(640, 454), text_input="Exit", font= runescape_font(20),
                             base_color="#d7fcd4", hovering_color="RED")

        for button in [PLAY_BUTTON, INSTRUCTIONS_BUTTON, EXIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(DISPLAYSURF)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkforInput(MENU_MOUSE_POS):
                    playgame()
                if INSTRUCTIONS_BUTTON.checkforInput(MENU_MOUSE_POS):
                    instructions()
                if EXIT_BUTTON.checkforInput(MENU_MOUSE_POS):      #Exits out of the game
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def gameover(): #Screen pops up when you lose, displays text for gameover, score, high score, and play again

    pygame.display.set_caption("Game Over Menu")

    while True:
        DISPLAYSURF.blit(mmbackground, (0, 0))

def instructions():

    pygame.display.set_caption("Instructions Menu")

    while True:

        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        DISPLAYSURF.fill("red")
        DISPLAYSURF.blit(instructionsbackground, (0, 180))

        OPTIONS_TEXTFIRST = ("Instructions: TzTok-Jad is attacking you with magic or ranged, you must select the correct")
        OPTIONS_TEXTFIRST = runescape_font(24).render(OPTIONS_TEXTFIRST,
            True, "Black")
        OPTIONS_RECT = OPTIONS_TEXTFIRST.get_rect(center=(800, 290))
        DISPLAYSURF.blit(OPTIONS_TEXTFIRST, OPTIONS_RECT)

        OPTIONS_TEXTSECOND = ("prayer to prevent getting attacked. Switch prayers for as long as possible to keep playing. ")
        OPTIONS_TEXTSECOND = runescape_font(24).render(OPTIONS_TEXTSECOND,
            True, "Black")
        OPTIONS_RECT = OPTIONS_TEXTSECOND.get_rect(center=(805, 320))
        DISPLAYSURF.blit(OPTIONS_TEXTSECOND, OPTIONS_RECT)

        OPTIONS_TEXTTHIRD = ("If you get hit you lose. Try to go for as long as possible to prepare for fight caves!")
        OPTIONS_TEXTTHIRD = runescape_font(24).render(OPTIONS_TEXTTHIRD,
            True, "Black")
        OPTIONS_RECT = OPTIONS_TEXTTHIRD.get_rect(center=(765, 350))
        DISPLAYSURF.blit(OPTIONS_TEXTTHIRD, OPTIONS_RECT)


        OPTIONS_BACK = Button(image=None, pos=(750, 430),
                              text_input="Click Here to Continue", font=runescape_font(42), base_color="Blue", hovering_color="Red")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(DISPLAYSURF)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkforInput(OPTIONS_MOUSE_POS):
                    mainmenu()

        pygame.display.update()

def gameover(final_time):
    pygame.display.set_caption("Game Over")

    time_text = stopwatch_font.render("Final Time: " + str(final_time) + " seconds", True, RED)

    while True:

        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        DISPLAYSURF.blit(gameoverbackground, (0, 0))
        DISPLAYSURF.blit(time_text, (10, 10))

        OPTIONS_BACK = Button(image=None, pos=(670, 454),
                              text_input="Click Here to Continue", font=runescape_font(42), base_color="Blue", hovering_color="Red")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(DISPLAYSURF)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkforInput(OPTIONS_MOUSE_POS):
                    mainmenu()

        pygame.display.update()

def playgame(): #Screen is meat of the game: Displays actual game, user jumps into

    pygame.display.set_caption("TzTok-Jad Prayer Flicking Game")

    DISPLAYSURF.blit(playbackground, (0, 0))
    DISPLAYSURF.blit(tooltip, (1040, 385))

    #Render in Sprite into playgame
    DISPLAYSURF.blit(playersprite, (100,500))

    #Create buttons
    PrayerOn_BUTTON = Button(image = prayerOffbutton, pos = (1128, 560), text_input="", font = runescape_font(15),
                         base_color= "#d7fcd4", hovering_color="RED")

    RangedOn_BUTTON = Button(image = rangedOffbutton, pos = (1165, 560), text_input="", font = runescape_font(15),
                         base_color= "#d7fcd4", hovering_color="RED")

    RangedOff_BUTTON = Button(image = rangedOffbutton, pos = (1165, 560), text_input="", font = runescape_font(15),
                         base_color= "#d7fcd4", hovering_color="RED")

    PrayerOff_BUTTON = Button(image = prayerOffbutton, pos = (1128, 560), text_input="", font = runescape_font(15),
                         base_color= "#d7fcd4", hovering_color="RED")

    Rangedtoggle = False
    Prayertoggle = False

    mouse_presses = pygame.mouse.get_pressed()

    #Jad ranged attack initialization
    ranged_frames = []
    ranged_image = Image.open("C:\\Users\\presi\\PycharmProjects\\TzTokJadPrayerFlickingGame\\venv\\images\\jadrange.gif")
    #frame_width, frame_height = ranged_image.size

    for i in range(0, ranged_image.n_frames):
        ranged_image.seek(i)
        frame = ranged_image.copy()
        frame = frame.convert("RGBA")
        data = frame.getdata()

        #remove white background
        new_data = [(r, g, b, 0) if (r, g, b) == (255, 255, 255) else (r, g, b, 255) for r, g, b, _ in data]
        frame.putdata(new_data)

        ranged_frames.append(frame)

    #Jad Mage attack initialization
    mage_frames = []
    mage_image = Image.open("C:\\Users\\presi\\PycharmProjects\\TzTokJadPrayerFlickingGame\\venv\\images\\jadmage.gif")
    #frame_width, frame_height = mage_image.size
    for i in range(0, mage_image.n_frames):
        mage_image.seek(i)
        frame = mage_image.copy()
        frame = frame.convert("RGBA")
        data = frame.getdata()

        # remove white background
        new_data = [(r, g, b, 0) if (r, g, b) == (255, 255, 255) else (r, g, b, 255) for r, g, b, _ in data]
        frame.putdata(new_data)
        mage_frames.append(frame)


    clock = pygame.time.Clock()
    transparent_color = (255, 0, 255)

    # Initialize stopwatch variables
    stopwatch_font = pygame.font.Font(None, 36)  # Choose a font and size
    stopwatch_start_time = pygame.time.get_ticks()
    stopwatch_running = True
    stopwatch_value = 0

    stopwatch_active = True  # Flag to indicate whether the stopwatch is active

    frame_change_interval = 100  # Adjust this as needed
    frame_change_interval_mage = 150  # Adjust this as needed
    last_frame_change_time = pygame.time.get_ticks()
    last_frame_change_time_mage = pygame.time.get_ticks()
    current_frame = 0
    current_frame_mage = 0
    show_ranged_animation = random.choice([True, False]) # Flag to determine which animation to show
    # Other variables (frame_change_interval, last_frame_change_time, etc.)
    animation_interval = 4100  # milliseconds
    last_animation_time = pygame.time.get_ticks()

    #Constant values that multiplies by two every time a check is done
    prayerchange_time = 3000
    rangedchange_time = 2700

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        current_time = pygame.time.get_ticks()

        # Check if it's time to switch animations
        if current_time - last_animation_time >= animation_interval:
            last_animation_time = current_time
            show_ranged_animation = not show_ranged_animation

        if show_ranged_animation:
            current_frame = (current_frame + 1) % len(ranged_frames)
        else:
            current_frame_mage = (current_frame_mage + 1) % len(mage_frames)

        #Re-Put the background, this way the gif continues to work
        DISPLAYSURF.blit(playbackground, (0, 0))
        if Rangedtoggle:
            DISPLAYSURF.blit(tooltip_range, (1040, 385))
        elif Prayertoggle:
            DISPLAYSURF.blit(tooltip_mage, (1040, 385))
        else:
            DISPLAYSURF.blit(tooltip, (1040, 385))

        # Render in Sprite into playgame
        DISPLAYSURF.blit(playersprite, (100, 500))

        # Draw the animation based on the flag
        if show_ranged_animation:
            frame_surface = pygame.image.fromstring(ranged_frames[current_frame].tobytes(),
                                                    ranged_frames[current_frame].size, 'RGBA')
            frame_surface = frame_surface.convert_alpha()
            DISPLAYSURF.blit(frame_surface, (35, 325))
        else:
            frame_surface_mage = pygame.image.fromstring(mage_frames[current_frame_mage].tobytes(),
                                                         mage_frames[current_frame_mage].size, 'RGBA')
            frame_surface_mage = frame_surface_mage.convert_alpha()
            DISPLAYSURF.blit(frame_surface_mage, (35, 325))

        pygame.display.flip()
        clock.tick(14)

        #Ensures that only one prayer (ranged or mage is enabled at a time)
        if Rangedtoggle:
            Prayertoggle = False
        if Prayertoggle:
            Rangedtoggle = False

        #Checking to see right prayer is equipped, if not then its game over
        #You have about 1.5 seconds from when the animation starts to press the prayer,
        #Logic: if, from when the animation started 3 milliseconds passes, check if toggles are enabled, else gameover
        #Every time the animation changes 3 milliseconds needs to pass before checking
        time_since_animation_start = current_time - last_animation_time
        if time_since_animation_start == prayerchange_time:
            prayerchange_time = prayerchange_time * 2
        #print(str(time_since_animation_start) + "time since animation start" + str(current_time) + "Current time" + str(last_animation_time) + "last animation time")
        if time_since_animation_start >= rangedchange_time:
            if show_ranged_animation:
                if not Rangedtoggle:
                    gameover(stopwatch_value)
        if time_since_animation_start >= prayerchange_time:
            if not show_ranged_animation:
                if not Prayertoggle:
                    gameover(stopwatch_value)

        # Update the stopwatch value if it's running
        if stopwatch_running:
            stopwatch_value = (current_time - stopwatch_start_time) // 1000  # in seconds

        # Display stopwatch value at the top left
        stopwatch_text = stopwatch_font.render("Time: " + str(stopwatch_value), True, (255, 255, 255))  # White color
        DISPLAYSURF.blit(stopwatch_text, (10, 10))  # Adjust position as needed

        pygame.display.flip()

        PlAY_MOUSE_POS = pygame.mouse.get_pos()
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()

            #Ranged On
            if mouse_presses[0]:
                if RangedOff_BUTTON.checkforInput(PlAY_MOUSE_POS):
                    Rangedtoggle = True
                    for button in [RangedOn_BUTTON]:
                        button.update(DISPLAYSURF)

            #Magic On
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                if PrayerOff_BUTTON.checkforInput(PlAY_MOUSE_POS):
                    Prayertoggle = True
                    for button in [PrayerOn_BUTTON]:
                        button.update(DISPLAYSURF)

            #Magic Off
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[2]:
                    if PrayerOn_BUTTON.checkforInput(PlAY_MOUSE_POS):
                        Prayertoggle = False
                        for button in [PrayerOff_BUTTON]:
                            button.update(DISPLAYSURF)

            #Ranged Off
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[2]:
                    if RangedOn_BUTTON.checkforInput(PlAY_MOUSE_POS):
                        Rangedtoggle = False
                        for button in [RangedOff_BUTTON]:
                            button.update(DISPLAYSURF)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


mainmenu()




