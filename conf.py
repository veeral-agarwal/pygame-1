import pygame
pygame.init()

t_c1=0
t_c2=0
var =0
time_past1 =0 
time_past2 =0
Width  = 800
Height = 768
play1_img=pygame.image.load('boat.png')
play2_img=pygame.image.load('sail.png')
fixedenemy_img=pygame.image.load('danger.png')
movingenemy_img=pygame.image.load('shark.png')
speed  = 10
flag = 1
score2 =0
score1 = 0
YELLOW = ((214, 204, 13))
BLUE = ((0,0,255))
orange = ((34,11,34))
inc=0
dec=0
check =0 
counter =0
ymin = 608
ymax=64
p1=0
p2=0
j=0
roundp_1 = []
roundp_2 = []
Green = (5, 92, 28)
myFont = pygame.font.SysFont("monospace",35)

pygame.display.set_caption("River Cross")   
player_size = 32
enemy_size  = 64

