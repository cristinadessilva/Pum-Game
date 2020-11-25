import pygame
from config import *
from texto import Texto

class Pet():

    def __init__(self,x,y,fartura,sujeira):
        self.x = x
        self.y = y
        self.fartura = fartura
        self.sujeira = sujeira
         
    def pet(self):
        petImg = pygame.image.load('alien.png')
        tela.blit(petImg, (self.x,self.y))

    def alimentar(self):
        self.fartura = self.fartura + 1
        self.sujeira = 1
        print (self.fartura)
        if self.fartura == 2:
            self.fartura = self.fartura - 1 
            print("Pum está cheio") 

    def lavar(self):
        self.sujeira = self.sujeira - 1
        self.fartura = 0
        print(self.sujeira)
        if self.sujeira == -1:
            self.sujeira = self.sujeira + 1
            print("Pum já está limpo")

