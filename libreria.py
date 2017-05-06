import pygame
import time
import threading
import sys
import random


BLANCO=(255,255,255)
ROJO=(255,0,0)
NEGRO=(0,0,0)
AMARILLO=(255,219,0)

ancho=1100
alto=660

class FinalBoss(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.var_x=1
        self.var_y=0
        self.vida=100
        self.sonido1=pygame.mixer.Sound("sonidos/golpeGanon.wav")
        self.sonido2=pygame.mixer.Sound("sonidos/ganonMuriendo.wav")
        self.sonido3=pygame.mixer.Sound("sonidos/conversion.wav")
        self.sonido4=pygame.mixer.Sound("sonidos/bolaFuego.wav")
        self.sonido5=pygame.mixer.Sound("sonidos/roca.wav")
        self.sonido6=pygame.mixer.Sound("sonidos/muerteGanon.wav")
        self.sonido7=pygame.mixer.Sound("sonidos/golpeRoca.wav")

    def menosVidaBala(self):
        self.vida-=1

    def menosVidaPiedra(self):
        self.vida-=24

    def golpe1 (self):
        self.sonido1.play()
    def golpe2 (self):
        self.sonido2.play()
    def golpe3 (self):
        self.sonido3.play()
    def golpe4 (self):
        self.sonido4.play()
    def golpe5 (self):
        self.sonido5.play()
    def golpe6 (self):
        self.sonido6.play()
    def golpe7 (self):
        self.sonido7.play()


    def update(self):
        self.rect.x=self.rect.x+self.var_x

        if self.rect.x==ancho/2-30:
            self.var_x=self.var_x*-1
        elif self.rect.x==ancho/2+30:
            self.var_x=self.var_x*-1

class FinalBossM(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Arco(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Trifuerza(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Bala(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.dir=0


    def update(self):
        vel=5
        if self.dir==0:
            self.rect.x+=vel
        if self.dir==1:
            self.rect.y-=vel
        if self.dir==2:
            self.rect.x-=vel
        if self.dir==3:
            self.rect.y+=vel







class Bala2(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.dir=0
        self.contador=0
        self.linea=[]
        self.sonido7=pygame.mixer.Sound("sonidos/golpeRoca.wav")

    def update(self):
        if self.contador < len(self.linea):
          self.rect.x=self.linea[self.contador][0]
          self.rect.y=self.linea[self.contador][1]
          self.contador+=4
        else:
            self.kill()
            self.sonido7.play()

class Bala3(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.dir=0
        self.contador=0
        self.linea=[]

    def update(self):
        if self.contador < len(self.linea):
          self.rect.x=self.linea[self.contador][0]
          self.rect.y=self.linea[self.contador][1]
          self.contador+=1
        else:
            self.kill()


class Bala4(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.dir=0
        self.contador=0
        self.linea=[]

    def update(self):
        if self.contador < len(self.linea):
          self.rect.x=self.linea[self.contador][0]
          self.rect.y=self.linea[self.contador][1]
          self.contador+=7
        else:
            self.kill()

class Bala5(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.dir=0
        self.contador=0
        self.linea=[]
        self.cd=100
        self.last=pygame.time.get_ticks()


    def update(self):
        now = pygame.time.get_ticks()

        if now - self.last >= self.cd:
            self.last=now
            if self.contador < len(self.linea):
              self.rect.x=self.linea[self.contador][0]
              self.rect.y=self.linea[self.contador][1]
              self.contador+=1





class botonPresionado(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo)
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Cofre(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Contenedor(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Caballero1(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.var_x=0
        self.var_y=0

    def update(self):
        self.rect.x=self.rect.x+self.var_x
        self.rect.y=self.rect.y+self.var_y

        if self.rect.y==500 and self.rect.x==380:
            self.var_x=1
            self.var_y=1
        if self.rect.y>560  and self.rect.x>430:
            self.var_y=-1
            self.var_x=-1

class Stalfo(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.var_x=1
        self.var_y=0




    def update(self):
        self.rect.x=self.rect.x+self.var_x

        if self.rect.x==400:
            self.var_x=self.var_x*-1
        elif self.rect.x==500:
            self.var_x=self.var_x*-1

class Stalfo2(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.var_x=1
        self.var_y=0




    def update(self):
        self.rect.x=self.rect.x+self.var_x

        if self.rect.x==100:
            self.var_x=self.var_x*-1
        elif self.rect.x==500:
            self.var_x=self.var_x*-1

class Caballero2(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.var_x=0
        self.var_y=0

    def update(self):
        self.rect.x=self.rect.x+self.var_x
        self.rect.y=self.rect.y+self.var_y

        if self.rect.y==565 and self.rect.x==660:
            self.var_x=-1
            self.var_y=-1
        if self.rect.y<528  and self.rect.x<600:
            self.var_y=1
            self.var_x=1




class EnemigoOctorok(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.var_x=1
        self.var_y=0




    def update(self):
        self.rect.x=self.rect.x+self.var_x

        if self.rect.x==60:
            self.var_x=self.var_x*-1
        elif self.rect.x==18:
            self.var_x=self.var_x*-1

class EnemigoVolando(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.var_x=10
        self.var_y=0

    def update(self):
        self.rect.x=self.rect.x+self.var_x

        if self.rect.x==200:
            self.var_x=self.var_x*-1
        elif self.rect.x==500:
            self.var_x=self.var_x*-1

class Enemigo(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.var_x=0
        self.var_y=2

    def update(self):
        self.rect.y=self.rect.y+self.var_y

        if self.rect.y==432:
            self.var_y=self.var_y*-1
        elif self.rect.y==590:
            self.var_y=self.var_y*-1


class Enemigo2(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.var_x=0
        self.var_y=1

    def update(self):
        self.rect.y=self.rect.y+self.var_y

        if self.rect.y==432:
            self.var_y=self.var_y*-1
        elif self.rect.y==590:
            self.var_y=self.var_y*-1



class Cuchilla1(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.var_x=0
        self.var_y=0

    def update(self):
        self.rect.x=self.rect.x+self.var_x
        self.rect.y=self.rect.y+self.var_y

        if self.rect.y==414 and self.rect.x==350:
            self.var_x=0
            self.var_y=2
        if self.rect.y==460 and self.rect.x==350:
            self.var_y=0
            self.var_x=2

        if self.rect.y==460 and self.rect.x==470:
            self.var_y=-2
            self.var_x=0

        if self.rect.y==414 and self.rect.x==470:
            self.var_y=0
            self.var_x=-2

class Cuchilla2(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.var_x=0
        self.var_y=0

    def update(self):
        self.rect.x=self.rect.x+self.var_x
        self.rect.y=self.rect.y+self.var_y

        if self.rect.y==460 and self.rect.x==670:
            self.var_x=0
            self.var_y=-2
        if self.rect.y==414 and self.rect.x==670:
            self.var_y=0
            self.var_x=-2

        if self.rect.y==414 and self.rect.x==570:
            self.var_y=2
            self.var_x=0

        if self.rect.y==460 and self.rect.x==570:
            self.var_y=0
            self.var_x=2


class MuroBloques(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



class Muro(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Muro2(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class MuroPuerta1(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class MuroPuerta2(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class MuroPuerta3(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class MuroPuerta4(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Boton(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Boton1(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class BotonPresionado1(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Boton2(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class BotonPresionado2(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Boton3(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class BotonPresionado3(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Boton4(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class BotonPresionado4(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class llegadaNivel2(pygame.sprite.Sprite):
    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(imagen).convert_alpha()
        self.rect=self.image.get_rect()

class llegada(pygame.sprite.Sprite):
    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(imagen).convert_alpha()
        self.rect=self.image.get_rect()

class llegadaFake(pygame.sprite.Sprite):
    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(imagen).convert_alpha()
        self.rect=self.image.get_rect()



class Jugador(pygame.sprite.Sprite):

    muros=None
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.sonido1=pygame.mixer.Sound("sonidos/win.wav")
        self.sonido2=pygame.mixer.Sound("sonidos/lose.wav")
        self.sonido3=pygame.mixer.Sound("sonidos/golpeEnemigo.wav")
        self.sonido4=pygame.mixer.Sound("sonidos/abriendoPuerta.wav")
        self.sonido5=pygame.mixer.Sound("sonidos/abriendoCofre.wav")
        self.sonido7=pygame.mixer.Sound("sonidos/error.wav")
        self.sonido8=pygame.mixer.Sound("sonidos/matando.wav")
        self.sonido9=pygame.mixer.Sound("sonidos/corazon.wav")
        self.sonido10=pygame.mixer.Sound("sonidos/flecha.wav")
        self.sonido11=pygame.mixer.Sound("sonidos/corazones.wav")
        self.sonido12=pygame.mixer.Sound("sonidos/orbe.wav")
        self.var_x=0
        self.var_y=0
        self.vida=100
        self.velocidad=3

    def menosVida(self):
        self.vida-=1

    def menosVidaBala(self):
        self.vida-=10

    def menosVidaRejas(self):
        self.vida-=0.04



    def golpe1 (self):
            self.sonido1.play()

    def golpe2 (self):
        self.sonido2.play()

    def golpe3 (self):
        self.sonido3.play()

    def golpe4 (self):
        self.sonido4.play()

    def golpe5 (self):
        self.sonido5.play()


    def golpe7 (self):
        self.sonido7.play()

    def golpe8 (self):
        self.sonido8.play()

    def golpe9 (self):
        self.sonido9.play()

    def golpe10 (self):
        self.sonido10.play()

    def golpe11 (self):
        self.sonido11.play()

    def golpe12 (self):
        self.sonido12.play()

    def move(self,dx,dy):
        if dx != 0:
            self.collide(dx, 0)
        if dy != 0:
            self.collide(0, dy)

    def collide(self,dx,dy):
        self.rect.x+=dx
        self.rect.y+=dy

        ls_golpes=pygame.sprite.spritecollide(self,self.muros,False)
        for g in ls_golpes:
            if dx>0:
                self.rect.right=g.rect.left
            if dx<0:
                self.rect.left=g.rect.right
            if dy>0:
                self.rect.bottom=g.rect.top
            if dy<0:
                self.rect.top=g.rect.bottom
