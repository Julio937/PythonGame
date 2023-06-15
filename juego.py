#build a PyGame game about rock,paper,scissors with a menu to select the game mode and the number of rounds to play
import pygame
import random
import time
import sys
from pygame.locals import *

# Initialize PyGame
pygame.init()

# Define some colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Rock, Paper, Scissors")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Load images
rock = pygame.image.load("rock.png")
rock = pygame.transform.scale(rock, (rock.get_width() // 3, rock.get_height() // 3))
rock_rect = rock.get_rect()
rock_rect.x = 100
rock_rect.y = 250
paper = pygame.image.load("paper.png")
paper = pygame.transform.scale(paper, (paper.get_width() // 2, paper.get_height() // 2))
paper_rect = paper.get_rect()
paper_rect.x = 350
paper_rect.y = 250
scissors = pygame.image.load("scissors.png")
scissors = pygame.transform.scale(scissors, (scissors.get_width() // 5, scissors.get_height() // 5))
scissors_rect = scissors.get_rect()
scissors_rect.x = 550
scissors_rect.y = 250
rock.set_colorkey(WHITE)
paper.set_colorkey(WHITE)
scissors.set_colorkey(WHITE)

# Load fonts
font = pygame.font.SysFont('Calibri', 25, True, False)
font2 = pygame.font.SysFont('Calibri', 50, True, False)

# Define variables
player_choice = 0
computer_choice = 0
player_score = 0
computer_score = 0
rounds = 0
mode = 0
game_over = False
winner = 0
tie = False
round_count = 0
rounds_played = 0
rounds_to_play = 0

# Define functions
def show_menu():
    """ Shows the game menu """
    screen.fill(WHITE)
    text = font2.render("Rock, Paper, Scissors", True, BLACK)
    screen.blit(text, [SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT / 2 - 100])
    text = font.render("Press 1 for single player", True, BLACK)
    screen.blit(text, [SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2])
    text = font.render("Press 3 to quit", True, BLACK)
    screen.blit(text, [SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 100])  
    pygame.display.flip()


#Show singleplayer screen
def show_singleplayer():
    global player_score, computer_score
    """ Shows the single player game screen """
    screen.fill(WHITE)
    text = font.render("Player Score: " + str(player_score), True, BLACK)
    screen.blit(text, [SCREEN_WIDTH / 2 - 300, 10])
    text = font.render("Computer Score: " + str(computer_score), True, BLACK)
    screen.blit(text, [SCREEN_WIDTH / 2 + 100, 10])
    text = font.render("Player Choice: ", True, BLACK)
    screen.blit(text, [SCREEN_WIDTH / 2 - 300, SCREEN_HEIGHT - 100])
    text = font.render("Computer Choice: ", True, BLACK)
    screen.blit(text, [SCREEN_WIDTH / 2 + 20, SCREEN_HEIGHT - 100])
    #Adding the images
    #Rock
    screen.blit(rock, (100,250))
    #Paper
    screen.blit(paper, (350, 250))
    #Scissors
    screen.blit(scissors, (550, 250))
    pygame.display.flip()


#Show winner screen
def show_winner(winner):
    """ Shows the winner screen """
    screen.fill(WHITE)
    if winner == "player":
        text = font2.render("You win!", True, BLACK)
    elif winner == "computer":
        text = font2.render("You lose!", True, BLACK)
    else:
        text = font2.render("It's a tie!", True, BLACK)
    screen.blit(text, [SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2])
    text = font.render("Press 0 to go back to the menu or 1 to play again", True, BLACK)
    screen.blit(text, [SCREEN_WIDTH / 2 - 250, SCREEN_HEIGHT / 2 + 50])
    pygame.display.flip()

#Show quit screen
def show_quit():
    """ Shows the quit screen """
    screen.fill(WHITE)
    text = font2.render("Quit", True, BLACK)
    screen.blit(text, [SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2 - 100])
    text = font.render("Press 1 to go back", True, BLACK)
    screen.blit(text, [SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 150])
    pygame.display.flip()

#Show error screen
def show_error():
    """ Shows the error screen """
    screen.fill(WHITE)
    text = font2.render("Error", True, BLACK)
    screen.blit(text, [SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2 - 100])
    text = font.render("Press 0 to go back to the menu", True, BLACK)
    screen.blit(text, [SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 150])
    pygame.display.flip()

#Show main menu
def show_main_menu():
    """ Shows the main menu """
    screen.fill(WHITE)
    text = font2.render("Rock Paper Scissors", True, BLACK)
    screen.blit(text, [SCREEN_WIDTH / 2 - 220, SCREEN_HEIGHT / 2 - 100])
    text = font.render("Press 1 for singleplayer", True, BLACK)
    screen.blit(text, [SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2])
    text = font.render("Press 3 to quit", True, BLACK)
    screen.blit(text, [SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 50])
    pygame.display.flip()

#Check if player chose any element with the mouse coliision
def chose_element():
    global player_choice, computer_choice
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                if rock_rect.collidepoint(x, y):
                    player_choice = 1
                    return
                elif paper_rect.collidepoint(x, y):
                    player_choice = 2
                    return
                elif scissors_rect.collidepoint(x, y):
                    player_choice = 3
                    return
                
#Compute chose:
def computer_chose():
    global computer_choice
    #Delay
    pygame.time.delay(1000)
    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        text = font.render("Rock", True, BLACK)
        screen.blit(text, [SCREEN_WIDTH / 2 + 210, SCREEN_HEIGHT - 100])
    elif computer_choice == 2:
        text = font.render("Paper", True, BLACK)
        screen.blit(text, [SCREEN_WIDTH / 2 + 210, SCREEN_HEIGHT - 100])
    elif computer_choice == 3:
        text = font.render("Scissors", True, BLACK)
        screen.blit(text, [SCREEN_WIDTH / 2 + 210, SCREEN_HEIGHT - 100])
    pygame.display.update()
 
#Show options chose
def option_chose():
    chose_element()
    if player_choice == 1:
        text = font.render("Rock", True, BLACK)
        screen.blit(text, [SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT - 100])
    elif player_choice == 2:
        text = font.render("Paper", True, BLACK)
        screen.blit(text, [SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT - 100])
    elif player_choice == 3:
        text = font.render("Scissors", True, BLACK)
        screen.blit(text, [SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT - 100])
    pygame.display.update()


#Check winner
def check_winner():
    """ Checks the winner of the game """
    global player_score, computer_score, player_choice, computer_choice    
    if player_choice == 1 and computer_choice == 2:
        player_score += 1
        show_winner('player')
    elif player_choice == 1 and computer_choice == 3:
        computer_score += 1
        show_winner('computer')
    elif player_choice == 2 and computer_choice == 1:
        computer_score += 1
        show_winner('computer')
    elif player_choice == 2 and computer_choice == 3:
        player_score += 1
        show_winner('player')
    elif player_choice == 3 and computer_choice == 1:
        player_score += 1
        show_winner('player')
    elif player_choice == 3 and computer_choice == 2:
        computer_score += 1
        show_winner('computer')
    elif player_choice == computer_choice:
        show_winner('tie')
    else:
        show_error()

    # Update scores on screen
    text = font.render("Player Score: " + str(player_score), True, BLACK)
    screen.blit(text, [SCREEN_WIDTH / 2 - 300, 10])
    text = font.render("Computer Score: " + str(computer_score), True, BLACK)
    screen.blit(text, [SCREEN_WIDTH / 2 + 100, 10])
    pygame.display.update()

#Reload the game going back to the main menu
def reload():
    """ Reloads the game """
    global player_score, computer_score, player_choice, computer_choice, mode
    player_score = 0
    computer_score = 0
    player_choice = 0
    computer_choice = 0
    mode = 0
    show_main_menu()

#Main loop for the game with all the fuctions
def main():
    """ Main function """
    global player_score, computer_score, player_choice, computer_choice, mode
    #Main loop for the game
    while not done:
        if mode == 0:
            #Main menu
            show_main_menu()
            
        #Get input from the user
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                mode = 1
                show_singleplayer()
                option_chose()
                computer_chose()
                #Delay
                pygame.time.delay(1000)
                check_winner()
                #After check the winner cheking if the player press key 0 to go back to the menu or if he press 1 to play again
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                            reload()
                            break
                        elif event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                            mode = 1
                            show_singleplayer()
                            option_chose()
                            computer_chose()
                            #Delay
                            pygame.time.delay(1000)
                            check_winner()     
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                show_quit()
                #Time delay
                time.sleep(2)
                sys.exit()


#Run the main function
if __name__ == "__main__":
    main()

#Quit the game
pygame.quit()
sys.exit()