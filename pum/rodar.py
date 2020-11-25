import pygame
from pet import *
from texto import Texto
import os
from config import *
import time

class Window():
    
    def __init__(self):
        self.tela = tela
        self.intro = True      
        self.texto = Texto()
        self.pet = Pet(-30,10,0,1)

    def button(self,msg,x,y,w,h,ic,ac,action):
        #botoes menu
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x+w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(tela, ac, (x,y,w,h))
            
            if click[0] == 1 and action !=None:
                
                if action == "jogar":
                    self.game_loop()

                elif action == "alimentar":
                    self.texto.alimentacao()
                    self.pet.alimentar()

                elif action == "lavar":
                    self.texto.lavamento()
                    self.pet.lavar()

                elif action == "soltar":
                    pygame.mixer.music.play()
                    time.sleep(1.5)
                    quit()
                    
                elif action == "menu_ida":
                    self.novapag()

                elif action == "menu_volta":
                    self.game_loop()
        else:
            pygame.draw.rect(tela, ic, (x,y,w,h))
            
        smallText = pygame.font.SysFont('Bodoni MT Black',30)
        TextSurface, TextRect = self.texto.text_objects(msg, smallText)
        TextRect.center = ( (x+(w/2)), (y + (h/2)) )
        tela.blit(TextSurface,TextRect)

    def rodar(self):
        while self.intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            self.atualizar()
            self.desenhar_tela()
            
            
    def desenhar_tela(self):
        self.tela.fill(cinza)
        largeText = pygame.font.SysFont('freesansbold',100)
        background = pygame.image.load("background.JpG")
        tela.blit(background, (0, 0))
        logoimg = pygame.image.load('pumpng.png')
        tela.blit(logoimg, (110,220))
        self.button("Jogar",150,400,100,50,verde_escuro,cinza_escuro,"jogar")

        pygame.display.update()
        clock.tick(15)

    def atualizar(self):
        pass

    def game_loop(self):
        gameExit = False
        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            tela.fill(cinza_escuro)
            self.button("Alimentar",70,500,110,50,verde_escuro,cinza,"alimentar")
            self.button("Lavar Pum",230,500,110,50,verde_escuro,cinza,"lavar")
            self.button("X",370,5,22,22,vermelho_escuro,cinza,"soltar")
            self.button(">",355,515,22,22,amarelo_esquesito,cinza,"menu_ida")
            self.pet.pet()
            pygame.display.update()
            clock.tick(60)

    def novapag(self):
        gameExit = False
        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            tela.fill(cinza_escuro)
            self.button("Soltar Pum!",150,500,120,50,verde_escuro,cinza,"soltar")
            self.button("X",370,5,22,22,vermelho_escuro,cinza,"soltar")
            self.button("<",200,560,22,22,amarelo_esquesito,cinza,"menu_volta")
            self.pet.pet()
            pygame.display.update()
            clock.tick(60)


simulador = Window()
simulador.rodar()

