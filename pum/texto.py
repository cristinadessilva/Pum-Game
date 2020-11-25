from config import *
import time

class Texto():
    def text_objects(self, text, font):
        textSurface = font.render(text, True, branco)
        return textSurface, textSurface.get_rect()

    def message_display(self,text):
        largeText = pygame.font.Font('freesansbold.ttf',30)
        TextSurface, TextRect = self.text_objects(text, largeText)
        TextRect.center = ((TELA_LARGURA/2),(TELA_ALTURA/2))
        tela.blit(TextSurface,TextRect)

        pygame.display.update()

        time.sleep(2)
        
        "game_loop()"

    def alimentacao(self):
        Texto.message_display(self,'Você alimentou pum!')
    
    def cheio(self):
        Texto.message_display(self,'To cheio!')

    def lavamento(self):
        Texto.message_display(self,'Você lavou pum!')


