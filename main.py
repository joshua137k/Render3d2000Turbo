import pygame
import sys
import numpy as np
from entities import *


class Cam:
	def __init__(self, pos = (0,0,0),rot=(0,0)):
		self.pos = list(pos)
		self.rot = list(rot)


	def events(self,event):
		if event.type == pygame.MOUSEMOTION:
			x,y = event.rel
			#200 issensivity			
			x/=200;y/=200
			self.rot[0]+=y;self.rot[1]+=x



	def update(self,dt,key):
		s = dt*10

		if key[pygame.K_q]: self.pos[1]-=s
		if key[pygame.K_e]: self.pos[1]+=s

		x,y = s*math.sin(self.rot[1]), s*math.cos(self.rot[1])
		if key[pygame.K_w]: self.pos[0]+=x;self.pos[2]+=y
		if key[pygame.K_s]: self.pos[0]-=x;self.pos[2]-=y

		if key[pygame.K_a]: self.pos[0]-=y;self.pos[2]+=x
		if key[pygame.K_d]: self.pos[0]+=y;self.pos[2]-=x



def drawFaces(entities):

	faces_list = [];faces_color = [];depth = []
	for obj in entities:
		
		vert_list,screen_coords=obj.get_verts(cam.pos,cam.rot)


		for f in range(len(obj.faces)):

			face = obj.faces[f]



			on_screen = True

			for i in face:

				cx,cy,cz=vert_list[i]
				if distance((cx,cy,cz),cam.pos)>100:
					on_screen=False
					break
				x,y = screen_coords[i]
				if not(vert_list[i][2]>0 and (x>-80 and x<w+80) and (y>-80 and y<h+80)):
					on_screen=False
					break

			if on_screen:
				coords = [screen_coords[i] for i in face]
				faces_list +=[coords]

				faces_color += [obj.colors[f]]

				depth += [sum(sum(vert_list[j][i] for j in face)**2 for i in range(3))]
		#Final Draw 
	
	order = sorted(range(len(faces_list)),key=lambda i: depth[i],reverse=True)
	for i in order:
		try:pygame.draw.polygon(screen,faces_color[i],faces_list[i])
		except:pass




pygame.init()
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()

cubes=[]

f=open("cords.txt","r")
letra=eval(f.read())
f.close()
for i in letra:
	cubes.append(Cube(i))


#cubes.append(Model3D("roo.obj",(0,0,0),(0,0,0)))

pygame.event.get();pygame.mouse.get_rel()
pygame.mouse.set_visible(0); pygame.event.set_grab(1);
cam = Cam((0,0,-5))

while True:
	dt = clock.tick()/1000
	for event in pygame.event.get():
		if event.type == pygame.QUIT: pygame.quit(); sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:pygame.quit();sys.exit()
		cam.events(event)

	screen.fill((20, 100,100))


	drawFaces(cubes)






	pygame.display.flip()

	key = pygame.key.get_pressed()
	cam.update(dt,key)
