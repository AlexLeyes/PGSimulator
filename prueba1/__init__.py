import pygame, sys
from pygame.locals import *
from random import randint
#GLOBALS
ancho = 1080
alto = 607

celeste = (30, 144, 255)
verde_pasto = (83, 187, 26)

ventana = pygame.display.set_mode((ancho,alto))
imagenFondo = pygame.image.load("Images/backgroundTest.png")
pygame.display.set_caption("Prueba2")



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
            self.rect.centerx += self.velocidad
            self.ImagenPersonaje = pygame.image.load("Images/nene1.png")
        if self.retardo == 10:
            self.rect.centerx += self.velocidad
            self.ImagenPersonaje = pygame.image.load("Images/nene2.png")
        if self.retardo == 15:
            self.rect.centerx += self.velocidad
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
            

def PgsSimulator():
   
    pygame.key.set_repeat(3)
    
    nene = personaje()
    jugador = perro()
    enJuego = True  
    
    
    
    
    while True:      
        nene.restringeMovimiento()
        nene.animarCaminar()
        
        
        if nene.rect.colliderect(jugador.rect):
            print "Chocan en posicion estatica"
            nene.rect.centerx +=-1
            nene.ImagenPersonaje = pygame.image.load("Images/nene1.png") 
        
        
        for evento in pygame.event.get(): #mainPrincipal    
            
            
            if evento.type == QUIT:# salir del juego
                pygame.quit()
                sys.exit()
                
            jugador.restringeMovimiento()
            
            if enJuego == True:
                 if evento.type == pygame.KEYDOWN:
                    print "Tecla presionada" 
                    if evento.key == K_LEFT:
                        print "Perro a la izquierda"
                        jugador.rect.centerx -= jugador.velocidad
                        
                        if jugador.posCamina <= 5:
                            jugador.ImagenPerro = pygame.transform.flip(pygame.image.load("Images/dog1.png"),True,False)
                            jugador.posCamina +=1
                            if nene.rect.colliderect(jugador.rect):
                                print "Empuja nene a la izquierda"
                                nene.rect.centerx +=0
                                jugador.rect.centerx +=8    
                            
                        elif jugador.posCamina > 5:
                            jugador.ImagenPerro = pygame.transform.flip(pygame.image.load("Images/dog2.png"),True,False)
                            jugador.posCamina -=1
                            if nene.rect.colliderect(jugador.rect):
                                print "Empuja nene a la izquierda"
                                nene.rect.centerx -=1
                                jugador.rect.centerx +=8   
                        
                        if jugador.posCamina > 10:
                            jugador.ImagenPerro = pygame.transform.flip(pygame.image.load("Images/dog1.png"),True,False)
                            jugador.posCamina = 0
                            if nene.rect.colliderect(jugador.rect):
                                print "Empuja nene a la izquierda"
                                nene.rect.centerx -=1
                                jugador.rect.centerx +=8    
                                                
                        
                    elif evento.key == K_RIGHT:
                        print "Perro a la dercha"
                        jugador.rect.centerx += jugador.velocidad
                                                
                        if jugador.posCamina <= 5:
                            jugador.ImagenPerro = pygame.image.load("Images/dog1.png")
                            jugador.posCamina +=1
                        elif jugador.posCamina > 5:
                            jugador.ImagenPerro = pygame.image.load("Images/dog2.png")
                            jugador.posCamina +=1
                        
                        if jugador.posCamina > 10:
                            jugador.ImagenPerro = pygame.image.load("Images/dog1.png")
                            jugador.posCamina = 0
                            
                        if nene.rect.colliderect(jugador.rect):
                            print "Empuja nene a la derecha"
                            nene.rect.centerx +=2
                            jugador.rect.centerx -=5          
                        
                        
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
        #cielo
        ventana.fill(celeste) 
        #pasto
        pygame.draw.polygon(ventana, verde_pasto,((0,300),(0,alto),(ancho,alto),(ancho,300)))
        #Carga FOndo
        ventana.blit(imagenFondo, (0,82)) 
         
        nene.dibujar(ventana)          
        jugador.dibujar(ventana)
        pygame.display.update() 
        
        
PgsSimulator()
