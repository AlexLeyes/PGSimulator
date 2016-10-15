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
        self.velocidad = 1      
        #cosas para animar
        self.posCamina = 0
        self.retardo = 0
    
    def dibujar(self, superficie):
       ventana.blit(self.ImagenPersonaje, self.rect)


class perro(pygame.sprite.Sprite):
    """Clase del Perro"""
    
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenPerro = pygame.image.load("Images/dog1.png")
        
              
        #self.caminaArriba = (pygame.image.load("Images/dog1.png"), pygame.image.load("Images/dog2.png"))
        #self.caminaAbajo = (pygame.image.load("Images/dog1.png"), pygame.image.load("Images/dog2.png"))
        
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
        
        
        nene.rect.centerx += nene.velocidad
        
        
          
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
                            
                        elif jugador.posCamina > 5:
                            jugador.ImagenPerro = pygame.transform.flip(pygame.image.load("Images/dog2.png"),True,False)
                            jugador.posCamina +=1
                        
                        if jugador.posCamina > 10:
                            jugador.ImagenPerro = pygame.transform.flip(pygame.image.load("Images/dog1.png"),True,False)
                            jugador.posCamina = 0
                        
                                                
                        
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
                        
                        
                    elif evento.key == K_UP:
                        print "Perro a la dercha"
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
                        
                    elif evento.key == K_DOWN:
                        print "Perro a la dercha"
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
