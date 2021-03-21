import pygame
import sys 
import random
import time
from conf import *
# var = pygame.time.get_ticks()
# time_past = pygame.time.get_ticks() - var

pygame.init()
 
def player_won1():
	screen.fill((50,168,82))
	text ="PLayer1 won:"
	label = myFont.render(text,1,YELLOW)
	screen.blit(label, (Width-400,Height-400))
	time.sleep(2)

def player_won2():
	screen.fill((121,50,168))	
	text ="Player2 won:"
	label = myFont.render(text,1,YELLOW)
	screen.blit(label, (Width-300,Height-400))
	time.sleep(2)

def set_level(j):
	speed =10 + 5*j
	return speed
clock = pygame.time.Clock()

class enemy:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.enemy_pos = [x,y]


class p_t:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.p_t = [x,y]

list = []
part = []
count = [1,2,3,4,5]
for i in count:
	width = random.randrange(50, 650)
	if i==5 :
		width = 200
	if i==1 :
		width = 100
	list.append(enemy(width,128*i-64))
	part.append(p_t(0,128*i-64))
mylist = []
count1 = [1,2,3,4]
for i in count1:
	width = random.randrange(50,550)
	mylist.append(enemy(width,128*i))

def detect_collision1(player_pos1,list,mylist):
	p_x = player_pos1[0]
	p_y = player_pos1[1]
	for obj in list:
		e_x = obj.enemy_pos[0]
		e_y = obj.enemy_pos[1]
		if (e_x >= p_x and e_x < (p_x + player_size))\
		   or (p_x >= e_x and p_x < (e_x + enemy_size)):
			if (e_y >= p_y and e_y < (p_y + player_size))\
			   or (p_y >= e_y and p_y < (e_y + enemy_size)):
				return True
	for obj in mylist:
		e_x = obj.enemy_pos[0]
		e_y = obj.enemy_pos[1]
		if (e_x >= p_x and e_x < (p_x + player_size))\
		 or (p_x >= e_x and p_x < (e_x + enemy_size)):
			if (e_y >= p_y and e_y < (p_y + player_size))\
			 or (p_y >= e_y and p_y < (e_y + enemy_size)):
				return True
	return False

def detect_collision2(player_pos2,list,mylist):
	p_x = player_pos2[0]
	p_y = player_pos2[1]
	for obj in list:
		e_x = obj.enemy_pos[0]
		e_y = obj.enemy_pos[1]
		if (e_x >= p_x and e_x < (p_x + player_size))\
		   or (p_x >= e_x and p_x < (e_x + enemy_size)):
			if (e_y >= p_y and e_y < (p_y + player_size))\
			   or (p_y >= e_y and p_y < (e_y + enemy_size)):
				return True
	for obj in mylist:
		e_x = obj.enemy_pos[0]
		e_y = obj.enemy_pos[1]
		if (e_x >= p_x and e_x < (p_x + player_size))\
		   or (p_x >= e_x and p_x < (e_x + enemy_size)):
			if (e_y >= p_y and e_y < (p_y + player_size))\
			   or (p_y >= e_y and p_y < (e_y + enemy_size)):
				return True
	return False

screen = pygame.display.set_mode((Width,Height))

red = (255,0,0)

	
game_over  = False

#players 
player_pos1 = [Width/2,Height-5*player_size]
player_pos2 = [Width/2,2*player_size]


background_color = (33, 131, 173)

var = pygame.time.get_ticks()

while   not game_over :

	if flag == 1: 
		time_past1 = (-var + pygame.time.get_ticks())//1000
	if flag == 0 :
		time_past2 = (-var + pygame.time.get_ticks())//1000 

	for event in pygame.event.get():
			
		if event.type == pygame.QUIT:
				sys.exit()

		if event.type == pygame.KEYDOWN:

			if flag == 1:
			
				x=player_pos1[0]
				y=player_pos1[1]

				if event.key == pygame.K_LEFT and x > 64:
					x-=32
				elif event.key == pygame.K_RIGHT and x < Width -2*player_size:
					x+=32
				elif event.key == pygame.K_DOWN and y < Height - 5*player_size:
					y+=64
				elif event.key == pygame.K_UP and y > 32:
					y-=64



				player_pos1 = [x,y]
			
			if flag == 0:
				x2= player_pos2[0]
				y2= player_pos2[1]

				if event.key == pygame.K_w and y2 >64:
					y2-=64	
				elif event.key == pygame.K_a and x2 > 64:
					x2-=32
				elif event.key == pygame.K_d and x2 < Width - 2*player_size:
					x2+=32
				elif event.key ==  pygame.K_s and y2 < Height - player_size:
					y2+=64
				

				player_pos2 = [x2,y2]

	if player_pos1[1] < ymin:
		ymin= player_pos1[1]
		if ymin == 544:
			score1+=5
		elif ymin == 480:
			score1+=10
		elif ymin == 416:
			score1+=5
		elif ymin == 352:
			score1+=10
		elif ymin == 288:
			score1+=5


		elif ymin== 224:
			score1+=10
		elif ymin == 160:
			score1+=5
		elif ymin == 96:
			score1 +=10
	if player_pos2[1] > ymax:
		ymax= player_pos2[1]
		if ymax%128 == 64:
			score2+=10
		else:  
			score2+=5

	if score1 == 60:
		flag =0
		player_pos1[0]= Width/2
		player_pos1[1]=Height-5*player_size
		var = pygame.time.get_ticks()
		#player_pos2[0]=Width/2
		#player_pos2[1]=player_size

	if score2 == 60:
		flag=1
		#player_pos1[0]= Width/2
		#player_pos1[1]=Height-3*player_size
		player_pos2[0]=Width/2
		player_pos2[1]=2*player_size
		
		var = pygame.time.get_ticks()
	screen.fill(background_color)

	text ="Score_1:" + str(score1)
	label = myFont.render(text,1,YELLOW)
	screen.blit(label, (Width-300,Height-100))

	
	text ="Score_2:" + str(score2)
	label = myFont.render(text,1,YELLOW)
	screen.blit(label, (Width-600,Height-100))

	if score1==60:
		roundp_1.append(score1)
		score1=0
		ymin = 608

	if score2==60:
		roundp_2.append(score2)

		if roundp_1[j] > roundp_2[j]:
			p1+=1
		elif roundp_2[j] > roundp_1[j]:
			p2+=1
		elif time_past1 > time_past2:
			p2+=1
		elif time_past2 > time_past1:
			p1+=1
		else:
			p2+=1
		j+=1
		score2=0
		ymax = 64
	if detect_collision1(player_pos1,list,mylist):
		
		flag=0
		roundp_1.append(score1)
		var = pygame.time.get_ticks()
		score1=0
		ymin=608
		player_pos1[0]= Width/2
		player_pos1[1]=Height-5*player_size
		player_pos2[0]=Width/2
		player_pos2[1]=2*player_size
	if detect_collision2(player_pos2,list,mylist):
		flag=1 
		roundp_2.append(score2)
		if roundp_1[j] > roundp_2[j]:
			p1+=1
		elif roundp_2[j] > roundp_1[j]:
			p2+=1
		elif time_past1 > time_past2:
			p2+=1
		elif time_past2 > time_past1:
			p1+=1
		else:
			p2+=1
		j+=1
		score2=0
		var = pygame.time.get_ticks()
		ymax=64
		player_pos1[0]= Width/2
		player_pos1[1]=Height-5*player_size
		player_pos2[0]=Width/2
		player_pos2[1]=2*player_size


	for obj in part:
		pygame.draw.rect(screen, Green, (obj.p_t[0],obj.p_t[1],Width,64))
	if flag == 1:
		#pygame.draw.rect(screen, red, (player_pos1[0],player_pos1[1],player_size,player_size))
		screen.blit(play1_img,(player_pos1[0],player_pos1[1]))

	else:
		#pygame.draw.rect(screen, orange, (player_pos2[0],player_pos2[1],player_size,player_size))
		screen.blit(play2_img,(player_pos2[0],player_pos2[1]))	

		
	for obj in list:
		#pygame.draw.rect(screen, YELLOW, (obj.enemy_pos[0],obj.enemy_pos[1],enemy_size,enemy_size))
		screen.blit(fixedenemy_img,(obj.enemy_pos[0],obj.enemy_pos[1]))
	for obj in mylist:
		if  obj.enemy_pos[0] >= 0 and obj.enemy_pos[0] <= Width:
			obj.enemy_pos[0] +=speed
		else:
			obj.enemy_pos[0] = 0 
		#pygame.draw.rect(screen, BLUE, (obj.enemy_pos[0],obj.enemy_pos[1],enemy_size,enemy_size))
		screen.blit(movingenemy_img,(obj.enemy_pos[0],obj.enemy_pos[1]))
	if j==3 and p1 > p2:
		player_won1()
		game_over =True
	elif j==3 and p2 > p1:
		player_won2()
		game_over = True




	text ="Time_1:" + str(time_past1)
	label = myFont.render(text,1,YELLOW)
	screen.blit(label, (Width-600,0))

	text ="Time_2:" + str(time_past2)
	label = myFont.render(text,1,YELLOW)
	screen.blit(label, (Width-300,0))

	speed=set_level(j)
	clock.tick(30)
	pygame.display.update()		