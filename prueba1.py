import pygame, sys
from pygame.locals import *
import pygame.sprite as sprite

pygame.init()
pygame.display.set_caption("Juego")

pantalla=pygame.display.set_mode((300,300))

class background(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.fondo = pygame.image.load("Imagenes/fondo1.jpg")
		self.rect_fondo = self.fondo.get_rect()
		pantalla = pygame.display.set_mode((800,600))
	
	def dibujar (self):
		pantalla.blit(self.fondo,self.rect_fondo)

	def actualizar(self,pantalla,vx,vy):
		self.rect_fondo.move_ip(-vx,-vy)	
		pantalla.blit(self.fondo,self.rect_fondo)

class personaje(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.nene = pygame.image.load("Imagenes/walk1.jpg").convert_alpha()
		self.nene2 = pygame.image.load("Imagenes/walk2.jpg").convert_alpha()
		self.listaImagenes = [self.nene, self.nene2]
		self.posImagen = 0
		
		self.Animacion = self.listaImagenes [self.posImagen]
		
		self.rect = self.Animacion.get_rect()

		self.rect.centerx = 200
		self.rect.centery = 500
		
	def dibujar(self):
		self.Animacion = self.listaImagenes[self.posImagen]
		pantalla.blit(self.Animacion, self.rect)
	def caminar (self):
		tecla = pygame.key.get_pressed()
		self.rect.centerx+=1

		if tecla[pygame.K_RIGHT]:				
			self.rect.centerx-=1
			
			self.posImagen += 1
			if self.posImagen > len(self.listaImagenes)-1:
				self.posImagen = 0
						
	def mover (self):
		tecla = pygame.key.get_pressed()
		dist = 2
		if tecla[pygame.K_DOWN]:
			if self.rect.centery < 500:
				self.rect.centery+=50	
		if tecla[pygame.K_UP]:
			if self.rect.centery > 400: 
				self.rect.centery-=50
		if tecla[pygame.K_RIGHT]:
			self.rect.centerx+=dist 
		if tecla[pygame.K_LEFT]:
			self.rect.centerx -=dist
		
		
class perro(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.imagenPerrito = pygame.image.load("Imagenes/perrito1.png").convert_alpha()
		self.perrito2 = pygame.image.load("Imagenes/perrito2.png").convert_alpha()
		
		self.listaImagenes = [self.imagenPerrito, self.perrito2]
		self.posImagen = 0
		
		self.Animacion = self.listaImagenes [self.posImagen]
		
		self.rect = self.Animacion.get_rect()
		self.rect.centerx = 100
		self.rect.centery = 500
				
	def dibujar(self):
		self.Animacion = self.listaImagenes[self.posImagen]
		pantalla.blit(self.Animacion, self.rect)
		
	def actualizar(self,pos):	
		if pos == 0:
			self.Animacion = self.listaImagenes[self.posImagen]
			pantalla.blit(self.Animacion, self.rect)

		if pos == 1:
			self.Animacion2 = pygame.transform.flip(self.Animacion,True,False)
			pantalla.blit(self.Animacion2, self.rect)						

	def caminar(self):
		tecla = pygame.key.get_pressed()
		dist = 2	
		#Derecha		
		if tecla[pygame.K_RIGHT]:
			#Movimiento
			if self.rect.centerx < 300:
				self.rect.centerx+=dist 
				
			#Animacion	
			self.posImagen += 1
			if self.posImagen > len(self.listaImagenes)-1:
				self.posImagen = 0
					
		#Izquierda	
		if tecla[pygame.K_LEFT]:
			#Movimiento
			if self.rect.centerx > 0:
				self.rect.centerx -=dist
			
			#Animacion (flip)	
			self.Animacion2 = pygame.transform.flip(self.Animacion,True,False)
			pantalla.blit(self.Animacion2, self.rect)			
			self.posImagen += 1

			if self.posImagen > len(self.listaImagenes)-1:
				self.posImagen = 0				

		#Arriba	
		if tecla[pygame.K_UP]:
			#Movimiento
			if self.rect.centery > 400: 
				self.rect.centery-=50
			#Animacion	
			self.posImagen += 1
			if self.posImagen > len(self.listaImagenes)-1:
				self.posImagen = 0		
						
		#Abajo
		if tecla[pygame.K_DOWN]:
			#Movimiento
			if self.rect.centery < 500:
				self.rect.centery+=50							
			#Animacion
			self.posImagen += 1
			if self.posImagen > len(self.listaImagenes)-1:
				self.posImagen = 0						
  
	def saltar(self):	
		if self.rect.centery > 400:
			self.rect.centery -= 15

	def pararse(self):
		if self.rect.centery < 500:
			self.rect.centery += 15

	def mover(self, personaje):
		if self.rect.colliderect(persona):
			persona.mover()

class enemigo(pygame.sprite.Sprite):
	def __init__ (self): 
		pygame.sprite.Sprite.__init__(self)
		self.enermigo = pygame.image.load("Imagenes/alien1.png")
		self.rect = self.enemigo.get_rect()
		
	
persona = personaje()
perrito = perro()
fondo01 = background()
reloj1= pygame.time.Clock()
vx =0
vy =0
velocidad = 7
pos = 0
caminar = 0

while True:
	
	tiempo = pygame.time.get_ticks()/1000
	pantalla.fill((0,200,255))
	
	#Fondo
	fondo01.dibujar()
	fondo01.update(vx,vy)
	
	#Nenito
	persona.dibujar()
	persona.caminar()
	
	#Perro
	perrito.dibujar()
		
	for event in pygame.event.get():

		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			perrito.caminar()
			perrito.mover(persona)
			vx=-velocidad
			pos = 1
			
		if event.key == pygame.K_RIGHT:
			persona.caminar()
			perrito.caminar()
			vx=velocidad
			pos = 0
			
		if event.key== pygame.K_UP:
			perrito.caminar()
			perrito.mover(persona)

		if event.key == pygame.K_DOWN:
			perrito.caminar()
			perrito.mover(persona)

		if event.key == pygame.K_SPACE:
			perrito.saltar()
			
	if event.type == pygame.KEYUP:
		if event.key == pygame.K_LEFT:
			vx=0
			pos = 1
			perrito.actualizar(pos)

		if event.key == pygame.K_RIGHT:
			vx=0
			pos = 0
			perrito.actualizar(pos)

		if event.key == pygame.K_SPACE:
			perrito.pararse()
	
	#Fondo		
	fondo01.dibujar()		
	fondo01.actualizar(pantalla,vx,vy)
	
	#Nenito
	persona.dibujar()
	persona.caminar()
	
	#Perro
	perrito.actualizar(pos)
	
	reloj1.tick(10)
	pygame.display.update()
