import pygame
from pygame.locals import *
import sys
from random import randint



#GLOBALS
ancho = 1080
alto = 607


celeste = (30, 144, 255)
verde_pasto = (83, 187, 26)

ventana = pygame.display.set_mode((ancho,alto))
imagenFondo = pygame.image.load("Images/backgroundTest.png")
pygame.display.set_caption("Prueba2")


class enemigoBrian(pygame.sprite.Sprite):
    "Clase Enemigo"
    def __init__(self, imagen):
        pygame.sprite.Sprite.__init__(self)
        
        self.ImagenEnemigo = imagen    
        self.rect = self.ImagenEnemigo.get_rect()
        self.rect.centerx = 800#(randint(200,8000))
        self.rect.centery = alto - 200#(randint(300 , alto))
        
    def dibujar(self, superficie):
       ventana.blit(self.ImagenEnemigo, self.rect)    
    
           

class personaje(pygame.sprite.Sprite):
    """Clase Personaje"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenPersonaje = pygame.image.load("Images/nene1.png")
        
        self.rect = self.ImagenPersonaje.get_rect()
        self.rect.centerx = 200
        self.rect.centery = alto-100
        
        self.Vida = True
        
        #cosas para animar
        self.velocidad = 1      
        self.posCamina = 0
        self.retardo = 0
    
    def dibujar(self, superficie):
       ventana.blit(self.ImagenPersonaje, self.rect)
       
       
    def animarCaminar(self):  
        self.retardo+=1
        if self.retardo == 5:
            self.ImagenPersonaje = pygame.image.load("Images/nene1.png")
        if self.retardo == 10:
            self.ImagenPersonaje = pygame.image.load("Images/nene2.png")
        if self.retardo == 15:
            self.ImagenPersonaje = pygame.image.load("Images/nene3.png")
            self.retardo = 0
                      
    def restringeMovimiento(self):
        if self.Vida == True:
            if self.rect.left > (ancho-75):
                self.rect.left = (ancho-75)
                print "Restringe borde Izquierdo, Vida menos"
           
            elif self.rect.right < 75:
                self.rect.right = 75
                print "Restringe borde Derecho"
                
            elif self.rect.top < 315:
                self.rect.top = 315
                print "Restringe borde Superior"
            
            elif self.rect.bottom > alto-10:
                self.rect.bottom = alto-10
                print "Restringe borde Inferior"        
            

class perro(pygame.sprite.Sprite):
    """Clase del Perro"""
    
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenPerro = pygame.image.load("Images/dog1.png")
        
        self.rect = self.ImagenPerro.get_rect()
        self.rect.centerx = ancho/2
        self.rect.centery = alto-100
        
        self.Vida = True
        self.velocidad = 5
               
        #cosas para animar
        self.posCamina = 0;  
    
    def disparar(self):
        pass
        
    def dibujar(self, superficie):
       ventana.blit(self.ImagenPerro, self.rect)
     
    def restringeMovimiento(self):
        if self.Vida == True:
            if self.rect.left > (ancho-75):
                self.rect.left = (ancho-75)
                print "Restringe borde Izquierdo, Vida menos"
                
           
            elif self.rect.right < 75:
                self.rect.right = 75
                print "Restringe borde Derecho"
                self.Vida = False
                
            elif self.rect.top < 260:
                self.rect.top = 260
                print "Restringe borde Superior"
            
            elif self.rect.bottom > alto-10:
                self.rect.bottom = alto-10
                print "Restringe borde Inferior"
  
    def animar(self,pos):    
        if pos == 0:
            self.Animacion = self.listaImagenes[self.posImagen]
            ventana.blit(self.Animacion, self.rect)

        if pos == 1:
            self.Animacion2 = pygame.transform.flip(self.Animacion,True,False)
            ventana.blit(self.Animacion2, self.rect)         
            
def salir(evento):
    if evento.type == QUIT:# salir del juego
         pygame.quit()
         sys.exit()
    

def gameOver(ventana):
    espera = False
        
    while espera == False:
       ventana.blit(pygame.image.load("Images/gameOver.png"),(ancho/2-100, alto/2-25))
       pygame.display.update() 
       for evento in pygame.event.get():
           salir(evento)
        
    
    
        

def PgsSimulator():
    c = 0;
    velocidadScroll = 1
   
    pygame.key.set_repeat(3)
    posInicialX = 0 #Psocion del fondo para scroll a la derecha
    nene = personaje()
    jugador = perro()
    enJuego = True
    goBrian = False;  
    
    
    #enemigos crear
    brian = enemigoBrian(pygame.image.load("Images/enemigos/braian.png"))
    
    
    
    
    while True:
        velocidadScroll = 1     
        nene.restringeMovimiento()
        nene.animarCaminar()
        jugador.restringeMovimiento()
        
        
        if nene.rect.colliderect(jugador.rect):
            print "Chocan en posicion estatica"
            jugador.rect.centerx += 3
            jugador.rect.centery += 3 
           
            
            nene.ImagenPersonaje = pygame.image.load("Images/nene1.png") 
            c = 1;
            
            
            
        
        for evento in pygame.event.get(): #mainPrincipal    
            
            salir(evento)
                                
            
            if enJuego == True:
                if evento.type == pygame.KEYDOWN:
                    print "Tecla presionada" 
                    
                    
                    if evento.key == K_LEFT:
                        print "Perro a la izquierda"
                        jugador.rect.centerx -= 2
                        jugador.posCamina +=1
                        
                        if jugador.posCamina == 0:
                            jugador.ImagenPerro = pygame.transform.flip(pygame.image.load("Images/dog1.png"),True,False)   
                        elif jugador.posCamina == 5:
                            jugador.ImagenPerro = pygame.transform.flip(pygame.image.load("Images/dog2.png"),True,False)  
                        elif jugador.posCamina == 10:
                            jugador.ImagenPerro = pygame.transform.flip(pygame.image.load("Images/dog1.png"),True,False)  
                        elif jugador.posCamina == 15:
                            jugador.ImagenPerro = pygame.transform.flip(pygame.image.load("Images/dog3.png"),True,False)  
                        elif jugador.posCamina == 20:
                            jugador.ImagenPerro = pygame.transform.flip(pygame.image.load("Images/dog1.png"),True,False)  
                            jugador.posCamina = 0
                        
                        if nene.rect.colliderect(jugador.rect):
                                print "Empuja nene a la izquierda"                                   
                                jugador.rect.centerx += 2
                                jugador.posCamina = 0   
                        
                        
                                
                                                
                        
                    elif evento.key == K_RIGHT:
                        print "Perro a la dercha"
                        jugador.rect.centerx += jugador.velocidad
                        jugador.posCamina +=1
                                                
                        if jugador.posCamina == 0:
                            jugador.ImagenPerro = pygame.image.load("Images/dog1.png")   
                        elif jugador.posCamina == 5:
                            jugador.ImagenPerro = pygame.image.load("Images/dog2.png")
                        elif jugador.posCamina == 10:
                            jugador.ImagenPerro = pygame.image.load("Images/dog1.png")
                        elif jugador.posCamina == 15:
                            jugador.ImagenPerro = pygame.image.load("Images/dog3.png")
                        elif jugador.posCamina == 20:
                            jugador.ImagenPerro = pygame.image.load("Images/dog1.png")
                            jugador.posCamina = 0
                            
                        if nene.rect.colliderect(jugador.rect):
                            print "Empuja nene a la derecha"
                            jugador.rect.centerx -= 4
                                   
                        
                        
                    elif evento.key == K_UP:
                        print "Perro arriba"
                        jugador.rect.centery -= jugador.velocidad
                        if jugador.posCamina <= 5:
                            jugador.ImagenPerro = pygame.image.load("Images/dogBack.png")
                            jugador.posCamina +=1
                        elif jugador.posCamina > 5:
                            jugador.ImagenPerro = pygame.transform.flip(pygame.image.load("Images/dogBack.png"),True,False)
                            jugador.posCamina +=1
                        
                        if jugador.posCamina > 10:
                            jugador.ImagenPerro = pygame.image.load("Images/dogBack.png")
                            jugador.posCamina = 0    
                            
                            #EMPUJAR AL NENE ARRIBA
                        if nene.rect.colliderect(jugador.rect):
                            print "Empuja nene arriba"
                            nene.rect.centery -=5
                            jugador.rect.centery +=5     
                        
                    elif evento.key == K_DOWN:
                        print "Perro abajo"
                        jugador.rect.centery += jugador.velocidad
                        if jugador.posCamina <= 5:
                            jugador.ImagenPerro = pygame.image.load("Images/dogFront.png")
                            jugador.posCamina +=1
                        elif jugador.posCamina > 5:
                            jugador.ImagenPerro = pygame.transform.flip(pygame.image.load("Images/dogFront.png"),True,False)
                            jugador.posCamina +=1
                        
                        if jugador.posCamina > 10:
                            jugador.ImagenPerro = pygame.image.load("Images/dogFront.png")
                            jugador.posCamina = 0   
                            
                            #EMPUJAR AL NENE ARRIBA
                        if nene.rect.colliderect(jugador.rect):
                            print "Empuja nene abajo"
                            nene.rect.centery +=5
                            jugador.rect.centery -=5 
                            
        
        
        
        #Colisiones con ENEMIGOS#
        if brian.rect.colliderect(nene.rect):
            goBrian = True       
        
                         
        #cielo
        ventana.fill(celeste) 
        #pasto
        pygame.draw.polygon(ventana, verde_pasto,((0,300),(0,alto),(ancho,alto),(ancho,300)))
        
        #Carga FOndo y lo mueve            
        posInicialX -= velocidadScroll
        print posInicialX;
        ventana.blit(imagenFondo,(posInicialX,82))  #se mueve el fondo
        brian.rect.centerx -=velocidadScroll;
        
        
        #El perro se queda en le lungar
        jugador.rect.centerx -=velocidadScroll
                 
        nene.dibujar(ventana)
        brian.dibujar(ventana)           
        jugador.dibujar(ventana)
        pygame.display.update() 
            
        
        
        if jugador.Vida == False:
            ventana.fill((255,0,0))
            gameOver(ventana)
            
            
        if goBrian == True:
            ventana.blit(pygame.image.load("Images/goBrian.png"),(0,0))
            gameOver(ventana)
            
        
            
            
        
PgsSimulator()
