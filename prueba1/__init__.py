import pygame
from pygame.locals import *
import sys
from random import randint
from turtle import right



#GLOBALS
ancho = 1080
alto = 607


celeste = (30, 144, 255)
piso = (128, 128, 128)

ventana = pygame.display.set_mode((ancho,alto))
imagenFondo = pygame.image.load("Images/backgroundTest.png")
pygame.display.set_caption("Prueba2")
pygame.mixer.init(44100, -16,2,2048)
sonido = pygame.mixer.Sound("sounds/efecto.wav") 

class Caja(pygame.sprite.Sprite):
    "Clase Enemigo"
    def __init__(self, ):
        pygame.sprite.Sprite.__init__(self)
        
        self.Imagen = pygame.image.load("Images/enemigos/caja.png")    
        self.rect = self.Imagen.get_rect()
        x = randint(1000,6000)
        y = randint(300, alto)
        self.rect.centerx = x
        self.rect.centery = y
        
    def dibujar(self, superficie):
        ventana.blit(self.Imagen, self.rect) 
       
    def empujado(self, evento):
        print "Caja Empujada"
        if evento.key == K_RIGHT:
            self.rect.centerx += 1     
        elif evento.key == K_LEFT:
            self.rect.centerx -= 0.5
        elif evento.key == K_UP:
            self.rect.centery -= 0.5
        elif evento.key == K_DOWN:
            self.rect.centery += 1
           

class EnemigoBrian(pygame.sprite.Sprite):
    "Clase Enemigo"
    def __init__(self, ):
        pygame.sprite.Sprite.__init__(self)
        
        self.ImagenEnemigo = pygame.image.load("Images/enemigos/braian.png")    
        self.rect = self.ImagenEnemigo.get_rect()
        x = randint(1000,6000)
        y = randint(300, alto-65)
        self.rect.centerx = x
        self.rect.centery = y
        
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
                
            elif self.rect.top < 335:
                self.rect.top = 335
                print "Restringe borde Superior"
            
            elif self.rect.bottom > alto-30:
                self.rect.bottom = alto-30
                print "Restringe borde Inferior"        
            

class perro(pygame.sprite.Sprite):
    """Clase del Perro"""
    
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenPerro = pygame.image.load("Images/perro/dog1.png")
        
        self.rect = self.ImagenPerro.get_rect()
        self.rect.centerx = ancho/2
        self.rect.centery = alto-100
                
        self.salud = 5
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
                print "Restringe borde Derecho, Vida menos"
                
           
            elif self.rect.right < 0:
                print "Restringe borde Izquierdo"
                self.Vida = False
                
            elif self.rect.top < 279:
                self.rect.top = 279
                print "Restringe borde Superior"
            
            elif self.rect.bottom > alto+20:
                self.rect.bottom = alto+20
                print "Restringe borde Inferior"
  
    def animar(self,pos):    
        if pos == 0:
            self.Animacion = self.listaImagenes[self.posImagen]
            ventana.blit(self.Animacion, self.rect)

        if pos == 1:
            self.Animacion2 = pygame.transform.flip(self.Animacion,True,False)
            ventana.blit(self.Animacion2, self.rect)    
            
    def colisonaCaja(self, evento):
        print "Jugador Colisiona Con Caja"
        if evento.key == K_RIGHT:
            self.ImagenPerro = pygame.image.load("Images/perro/dog1.png")
            self.rect.centerx -= 5
            
        elif evento.key == K_LEFT:
            self.ImagenPerro = pygame.transform.flip(pygame.image.load("Images/perro/dog1.png"),True,False) 
            self.rect.centerx += 2
            
        elif evento.key == K_UP:
            self.ImagenPerro = pygame.transform.flip(pygame.image.load("Images/perro/dogBack.png"),True,False) 
            self.rect.centery += 5
        
        elif evento.key == K_DOWN:
            self.ImagenPerro = pygame.transform.flip(pygame.image.load("Images/perro/dogFront.png"),True,False) 
            self.rect.centery -= 5
        
             
            
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
            loop()

class Menu:    
    def __init__(self, opciones):
        self.opciones = []
        fuente = pygame.font.Font('dejavu.ttf',40)
        x = 450
        y = 303
        paridad = 1
        

        self.cursor = Cursor(x - 90, y, 90)

        for titulo, funcion in opciones:
            self.opciones.append(Opcion(fuente, titulo, x, y, paridad, funcion))
            y += 90
            if paridad == 1:
                paridad = -1
            else:
                paridad = 1

        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):

      k = pygame.key.get_pressed()
       
      if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
                sonido.play()
            elif k[K_DOWN]:
                self.seleccionado += 1
                sonido.play()
            elif k[K_RETURN]:
                self.opciones[self.seleccionado].activar()
                

      if self.seleccionado < 0:
            self.seleccionado = 0
      elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

		
      self.cursor.seleccionar(self.seleccionado)
       
      self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]
      self.cursor.actualizar()
       
      for o in self.opciones:
            o.actualizar()

    def imprimir(self, screen):

        self.cursor.imprimir(screen)

        for opcion in self.opciones:
            opcion.imprimir(screen)        
    
def herido(jugador):
    "pygame.mixer.Channel("")"
    growl = pygame.mixer.Sound("Sounds/dog_growl.mp3")
    growl.play()
    
   
    contHerido = 0
    jugador.salud -= 1
    jugador.ImagenPerro = pygame.image.load("Images/perro/hurtDogFront.png")
    jugador.dibujar(ventana)
    pygame.display.update()
    
      
    print "Cambia IMagen Herido"
   
    while (contHerido < 25000):
        
        
        print  "Estoy herido"
        print  contHerido       
        contHerido +=1
                 
    
    jugador.rect.centerx -=200
    jugador.ImagenPerro = pygame.image.load("Images/perro/dog1.png")    

class Cursor:
    def __init__(self, x, y, dy):
        self.image = pygame.image.load('images/cursor 2.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.y_inicial = y
        self.dy = dy
        self.y = 0
        self.seleccionar(0)

    def actualizar(self):
        self.y += (self.to_y - self.y) / 10.0
        self.rect.y = int(self.y)

    def seleccionar(self, indice):
        self.to_y = self.y_inicial + indice * self.dy

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)

def pausa():
    pygame.mixer_music.pause()
    pygame.key.set_repeat(100)
    print "Presionda P <<Poniendo en pausa>>"
    pausa = True
    retardoPausa = 0
    
    while pausa == True:
        
        print "Juego Pausado"
        print retardoPausa 
        
        if retardoPausa <= 500:
            retardoPausa+=1
                                             
            ventana.blit(pygame.image.load("Images/pausa.png"),(ancho/2-64, alto/2+30))
       
        if retardoPausa > 500:
            retardoPausa+=1   
            ventana.blit(pygame.image.load("Images/pausa2.png"),(ancho/2-64, alto/2+30))
                                         
        if retardoPausa == 1000:
            retardoPausa = 0
                                   
                                    
        pygame.display.update()                                                      
    
        
        for evento in pygame.event.get():
            salir(evento)
            if evento.type == pygame.KEYDOWN:
                
                if evento.key == K_p or evento.key==K_ESCAPE:
                    pausa = False
                 
                 
    pygame.key.set_repeat(3)
    pygame.mixer_music.unpause()        

def PgsSimulator():
    
    velocidadScroll = 1
   
    pygame.key.set_repeat(3)
    posInicialX = 0 #Psocion del fondo para scroll a la derecha
    nene = personaje()
    jugador = perro()
    enJuego = True
    goBrian = False
    goCaja = False
    tiempo = 0

    aux = 1
    
    #Iniciador de fuetes
    pygame.font.init()
    fuente = pygame.font.SysFont("Consolas", 30) 
    puntuacion = fuente.render("Ptos: "+ str(0),0,(255,255,255)) 
    
    #Iniciador de sonido
    pygame.mixer.init()
    pygame.mixer.music.load("Sounds/music.mp3")
    pygame.mixer.music.play(5)
    #enemigos crear
    brian0 = EnemigoBrian()
    brian1 = EnemigoBrian()
    brian2 = EnemigoBrian()
    brian3 = EnemigoBrian()
    
    
    caja0 = Caja()
    caja1 = Caja()
    caja2 = Caja()
    caja3 = Caja()
    
    
    
    
    
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
            
            
        for evento in pygame.event.get(): #mainPrincipal    
            
            salir(evento)
                                
            
            if enJuego == True:
                if evento.type == pygame.KEYDOWN:
                    print "Tecla presionada" 
                    
                    
                    if evento.key == K_p or evento.key==K_ESCAPE:
                        pausa()
                         
                    
                    if evento.key == K_LEFT:
                        print "Perro a la izquierda"
                        jugador.rect.centerx -= 3
                        jugador.posCamina +=1
                        
                        if jugador.posCamina == 0:
                            jugador.ImagenPerro = pygame.transform.flip(pygame.image.load("Images/perro/dog1.png"),True,False)   
                        elif jugador.posCamina == 5:
                            jugador.ImagenPerro = pygame.transform.flip(pygame.image.load("Images/perro/dog2.png"),True,False)  
                        elif jugador.posCamina == 10:
                            jugador.ImagenPerro = pygame.transform.flip(pygame.image.load("Images/perro/dog1.png"),True,False)  
                        elif jugador.posCamina == 15:
                            jugador.ImagenPerro = pygame.transform.flip(pygame.image.load("Images/perro/dog3.png"),True,False)  
                        elif jugador.posCamina == 20:
                            jugador.ImagenPerro = pygame.transform.flip(pygame.image.load("Images/perro/dog1.png"),True,False)  
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
                            jugador.ImagenPerro = pygame.image.load("Images/perro/dog1.png")   
                        elif jugador.posCamina == 5:
                            jugador.ImagenPerro = pygame.image.load("Images/perro/dog2.png")
                        elif jugador.posCamina == 10:
                            jugador.ImagenPerro = pygame.image.load("Images/perro/dog1.png")
                        elif jugador.posCamina == 15:
                            jugador.ImagenPerro = pygame.image.load("Images/perro/dog3.png")
                        elif jugador.posCamina == 20:
                            jugador.ImagenPerro = pygame.image.load("Images/perro/dog1.png")
                            jugador.posCamina = 0
                            
                        if nene.rect.colliderect(jugador.rect):
                            print "Empuja nene a la derecha"
                            jugador.rect.centerx -= 4
                                   
                        
                        
                    elif evento.key == K_UP:
                        print "Perro arriba"
                        jugador.rect.centery -= jugador.velocidad
                        if jugador.posCamina <= 5:
                            jugador.ImagenPerro = pygame.image.load("Images/perro/dogBack.png")
                            jugador.posCamina +=1
                        elif jugador.posCamina > 5:
                            jugador.ImagenPerro = pygame.transform.flip(pygame.image.load("Images/perro/dogBack.png"),True,False)
                            jugador.posCamina +=1
                        
                        if jugador.posCamina > 10:
                            jugador.ImagenPerro = pygame.image.load("Images/perro/dogBack.png")
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
                            jugador.ImagenPerro = pygame.image.load("Images/perro/dogFront.png")
                            jugador.posCamina +=1
                        elif jugador.posCamina > 5:
                            jugador.ImagenPerro = pygame.transform.flip(pygame.image.load("Images/perro/dogFront.png"),True,False)
                            jugador.posCamina +=1
                        
                        if jugador.posCamina > 10:
                            jugador.ImagenPerro = pygame.image.load("Images/perro/dogFront.png")
                            jugador.posCamina = 0   
                            
                            #EMPUJAR AL NENE ARRIBA
                        if nene.rect.colliderect(jugador.rect):
                            print "Empuja nene abajo"
                            nene.rect.centery +=5
                            jugador.rect.centery -=5 
                            
        
        
        
        #Colisiones con ENEMIGOS# Personaje
        if brian0.rect.colliderect(nene.rect):
            goBrian = True
        elif brian1.rect.colliderect(nene.rect):
            goBrian = True     
        elif brian2.rect.colliderect(nene.rect):
            goBrian = True     
        elif brian3.rect.colliderect(nene.rect):
            goBrian = True
           
        
        
        
        
            
        if caja0.rect.colliderect(nene.rect):
            goCaja = True
        elif caja1.rect.colliderect(nene.rect):
            goCaja = True     
        elif caja2.rect.colliderect(nene.rect):
            goCaja = True     
        elif caja3.rect.colliderect(nene.rect):
            goCaja = True
            
            
       
       
                
        if brian0.rect.colliderect(jugador.rect):
            herido(jugador)    
        elif brian1.rect.colliderect(jugador.rect):
            herido(jugador)       
        elif brian2.rect.colliderect(jugador.rect):
            herido(jugador)   
        elif brian3.rect.colliderect(jugador.rect):
            herido(jugador)
         
            
        #Colisiones con ENEMIGOS# PERRO
        
        # if evento.type == pygame.KEYDOWN:
            
     
        if caja0.rect.colliderect(jugador.rect):
            jugador.colisonaCaja(evento)
            caja0.empujado(evento)
        elif caja1.rect.colliderect(jugador.rect):
            jugador.colisonaCaja(evento)
            caja1.empujado(evento) 
        elif caja2.rect.colliderect(jugador.rect):
            jugador.colisonaCaja(evento)
            caja2.empujado(evento)
        elif caja3.rect.colliderect(jugador.rect):
            jugador.colisonaCaja(evento)
            caja3.empujado(evento)
            
            
            
        
                         
        #cielo
        ventana.fill(celeste) 
        #pasto
        pygame.draw.polygon(ventana, piso,((0,300),(0,alto),(ancho,alto),(ancho,300)))
        
        #Carga FOndo y lo mueve            
        posInicialX -= velocidadScroll
        #print posInicialX;
        ventana.blit(imagenFondo,(posInicialX,-15))  #se mueve el fondo
        brian0.rect.centerx -=velocidadScroll;
        brian1.rect.centerx -=velocidadScroll;
        brian2.rect.centerx -=velocidadScroll;
        brian3.rect.centerx -=velocidadScroll;
        
        
        
        caja0.rect.centerx -=velocidadScroll;
        caja1.rect.centerx -=velocidadScroll;
        caja2.rect.centerx -=velocidadScroll;
        caja3.rect.centerx -=velocidadScroll;
        
        
        #El perro se queda en le lungar
        jugador.rect.centerx -=velocidadScroll
                 
        nene.dibujar(ventana)

        caja0.dibujar(ventana)
        caja1.dibujar(ventana)  
        caja2.dibujar(ventana)  
        caja3.dibujar(ventana)          
                       
        brian0.dibujar(ventana)
        brian1.dibujar(ventana)  
        brian2.dibujar(ventana)  
        brian3.dibujar(ventana)  
        
        
        
        jugador.dibujar(ventana)
        #*******************TIEMPO/Puntuacion***************************
        tiempo += 1     
        puntos = tiempo/5 
        if aux == puntos: 
            aux+=1
            print puntos
            puntuacion = fuente.render("Ptos: "+ str(puntos),0,(255,255,255))
        ventana.blit(puntuacion,(20,20))
        #***************************************************************  
        pygame.display.update()            
        
            
        
        
        if jugador.Vida == False:
            ventana.fill((255,0,0))
            gameOver(ventana)
        
        if jugador.salud == 0:
            ventana.fill((255,150,0))
            gameOver(ventana)
            
            
        if goBrian == True:
            ventana.blit(pygame.image.load("Images/goBrian.png"),(ancho/2-250,alto/2-157))
            gameOver(ventana)
            
        if goCaja == True:
            ventana.fill((0,0,0))
            ventana.blit(pygame.image.load("Images/enemigos/caja.png"),(ancho/2,alto/2+100))
            gameOver(ventana)
            
            
            """Nilvel TERMINADO"""
        if posInicialX == -8000+1080: 
            ventana.fill((0,255,0))
            gameOver(ventana)
        
class Opcion:

    def __init__(self, fuente, titulo, x, y, paridad, funcion_asignada):
        self.imagen_normal = fuente.render(titulo, 1, (0, 0, 255))
        self.imagen_destacada = fuente.render(titulo, 1, (200, 0, 0))
        self.image = self.imagen_normal
        self.rect = self.image.get_rect()
        self.rect.x = 500 * paridad
        self.rect.y = y
        self.funcion_asignada = funcion_asignada
        self.x = float(self.rect.x)

    def actualizar(self):
        destino_x = 450
        self.x += (destino_x - self.x) / 5.0
        self.rect.x = int(self.x)

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)

    def destacar(self, estado):
        if estado:
            self.image = self.imagen_destacada
        else:
            self.image = self.imagen_normal

    def activar(self):
        self.funcion_asignada()        
        
def salir_del_programa():
    import sys
    print " Gracias por utilizar este programa."
    sys.exit(0)        
        
def loop ():
	       
 if __name__ == '__main__':
    
    salir = False
    opciones = [
        ("Jugar", PgsSimulator),
        ("Salir", salir)
        ]
	
    pygame.font.init()
    fondo = pygame.image.load("images/fondo2.png").convert()
    menu = Menu(opciones)

    while not salir:

        for e in pygame.event.get():
            if e.type == QUIT:
                salir = True

        ventana.blit(fondo, (0, 0))
        menu.actualizar()
        menu.imprimir(ventana)

        pygame.display.flip()
        pygame.time.delay(10)            
        
  
loop()
