import pygame
import math 
pygame.init()
screen = pygame.display.set_mode((1000,800))
total = 0
ship1_x=250
ship2_x=450
ship3_x=650
ship4_x=250
ship5_x=450
ship6_x=650
ship1_y=250
ship2_y=250
ship3_y=250
ship4_y=550
ship5_y=550
ship6_y=550
player_1_x = 400
player_1_y = 750
score = 0
level = 1
change = 1

def score_player_1():
    global score
    if player_1_y <= 150:
        score += 5
    if player_1_y <= 250:
        score += 10
    if player_1_y <= 350:
        score += 5
    if player_1_y <= 450:
        score += 5
    if player_1_y <= 550:
        score += 10
    if player_1_y <= 650:
        score += 5
    return True
    

def collosion():
    if math.sqrt(math.pow(ship1_x-player_1_x,2)+math.pow(ship1_y-player_1_y,2)) < 20:
        return True
    elif math.sqrt(math.pow(ship2_x-player_1_x,2)+math.pow(ship2_y-player_1_y,2)) < 20:
        return True
    elif math.sqrt(math.pow(ship3_x-player_1_x,2)+math.pow(ship3_y-player_1_y,2)) < 20:
        return True
    elif math.sqrt(math.pow(ship4_x-player_1_x,2)+math.pow(ship4_y-player_1_y,2)) < 20:
        return True
    elif math.sqrt(math.pow(ship5_x-player_1_x,2)+math.pow(ship5_x-player_1_y,2)) < 20:
        return True
    elif math.sqrt(math.pow(ship6_x-player_1_x,2)+math.pow(ship6_y-player_1_y,2)) < 20:
        return True
    elif math.sqrt(math.pow(200-player_1_x,2)+math.pow(150-player_1_y,2)) < 20:
        return True
    elif math.sqrt(math.pow(200-player_1_x,2)+math.pow(350-player_1_y,2)) < 20:
        return True
    elif math.sqrt(math.pow(200-player_1_x,2)+math.pow(450-player_1_y,2)) < 20:
        return True
    elif math.sqrt(math.pow(200-player_1_x,2)+math.pow(650-player_1_y,2)) < 20:
        return True
    elif math.sqrt(math.pow(400-player_1_x,2)+math.pow(150-player_1_y,2)) < 20:
        return True
    elif math.sqrt(math.pow(400-player_1_x,2)+math.pow(350-player_1_y,2)) < 20:
        return True
    elif math.sqrt(math.pow(400-player_1_x,2)+math.pow(450-player_1_y,2)) < 20:
        return True
    elif math.sqrt(math.pow(400-player_1_x,2)+math.pow(650-player_1_y,2)) < 20:
        return True
    elif math.sqrt(math.pow(600-player_1_x,2)+math.pow(150-player_1_y,2)) < 20:
        return True
    elif math.sqrt(math.pow(600-player_1_x,2)+math.pow(350-player_1_y,2)) < 20:
        return True
    elif math.sqrt(math.pow(600-player_1_x,2)+math.pow(450-player_1_y,2)) < 20:
        return True
    elif math.sqrt(math.pow(600-player_1_x,2)+math.pow(650-player_1_y,2)) < 20:
        return True
    elif math.sqrt(math.pow(800-player_1_x,2)+math.pow(150-player_1_y,2)) < 20:
        return True
    elif math.sqrt(math.pow(800-player_1_x,2)+math.pow(350-player_1_y,2)) < 20:
        return True
    elif math.sqrt(math.pow(800-player_1_x,2)+math.pow(450-player_1_y,2)) < 20:
        return True
    elif math.sqrt(math.pow(800-player_1_x,2)+math.pow(650-player_1_y,2)) < 20:
        return True
    else:
        False

run = True
while run:
    if level == 5:
        break
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    river = pygame.draw.rect(screen, (0,0,255),(0,200,1000,100))
    river = pygame.draw.rect(screen, (0,0,255),(0,400,1000,40))
    river = pygame.draw.rect(screen, (0,0,255),(0,500,1000,100))
    river = pygame.draw.rect(screen, (0,0,255),(0,700,1000,40))

    score = 0
    change = level*0.5+1

    mountain = pygame.image.load('beach.png')
    ship1 = pygame.image.load('4.png')
    ship2 = pygame.image.load('4.png')
    ship3 = pygame.image.load('4.png')
    ship4 = pygame.image.load('4.png')
    ship5 = pygame.image.load('4.png')
    ship6 = pygame.image.load('4.png')
    player_1 = pygame.image.load('3.png')
    
    screen.blit(player_1,(player_1_x,player_1_y))
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and player_1_x > 0:
            player_1_x -= 1
        if event.key == pygame.K_RIGHT and player_1_x < 970:
            player_1_x += 1
        if event.key == pygame.K_UP and player_1_y > 0:
            player_1_y -= 1
        if event.key == pygame.K_DOWN and player_1_y < 780:
            player_1_y += 1

    
    
    ship1_x+=change
    ship2_x+=change
    ship3_x+=change
    ship4_x+=change
    ship5_x+=change
    ship6_x+=change
    if ship1_x > 980:
        ship1_x = 10
    if ship2_x > 980:
        ship2_x = 10
    if ship3_x > 980:
        ship3_x = 10
    if ship4_x > 980:
        ship4_x = 10     
    if ship5_x > 980:
        ship5_x = 10
    if ship6_x > 980:
        ship6_x = 10
    
    
    
    screen.blit(mountain,(200,150))
    screen.blit(mountain,(200,350))
    screen.blit(mountain,(200,450))
    screen.blit(mountain,(200,650))
    screen.blit(mountain,(400,150))
    screen.blit(mountain,(400,350))
    screen.blit(mountain,(400,450))
    screen.blit(mountain,(400,650))
    screen.blit(mountain,(600,150))
    screen.blit(mountain,(600,350))
    screen.blit(mountain,(600,450))
    screen.blit(mountain,(600,650))
    screen.blit(mountain,(800,150))
    screen.blit(mountain,(800,350))
    screen.blit(mountain,(800,450))
    screen.blit(mountain,(800,650))
    screen.blit(ship1,(ship1_x,250))
    screen.blit(ship2,(ship2_x,250))
    screen.blit(ship3,(ship3_x,250))
    screen.blit(ship4,(ship4_x,550))
    screen.blit(ship5,(ship5_x,550))
    screen.blit(ship6,(ship6_x,550))


    if collosion():
        player_1_x = 400
        player_1_y = 750
    if player_1_y == 50:
        player_1_x = 400
        player_1_y = 750
    if player_1_y == 52 :
        level += 1
    score_player_1()
    total += score


    font1 = pygame.font.SysFont("Times New Roman",16)
    vrvrvr = font1.render("score : " + str(score) , 1 , (255,0,255))
    screen.blit(vrvrvr,(10,10))

    font2 = pygame.font.SysFont("Times New Roman",16)
    vrvr = font2.render("level : " + str(level) , 1 , (255,0,255))
    screen.blit(vrvr,(900,10))
    pygame.display.update()

while run:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    font3 = pygame.font.SysFont("Times New Roman",96)
    vrvrvrv = font3.render("Total score : 200"  , 1 , (255,0,255))
    screen.blit(vrvrvrv,(300,375))
    pygame.display.update()
pygame.quit()
