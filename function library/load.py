# Game intro and loading

def load():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    
    BLACK = (  0,   0,   0)
    WHITE = ( 255, 255, 255)
    RED = ( 255, 0, 0)
    pygame.mixer.music.load("WW3music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    
    def display_text_animation(string, pos1, pos2, mycolor, mysize):
        text = ''
        for i in range(len(string)):
            DISPLAYSURF.fill(BLACK)
            text += string[i]
            font=pygame.font.Font('D:/myfonts/thefont.ttf',mysize)
            text_surface = font.render(text, True, mycolor)
            text_rect = text_surface.get_rect()
            text_rect.center = (pos1, pos2)
            DISPLAYSURF.blit(text_surface, text_rect)
            pygame.display.update()
            pygame.event.get()
            pygame.time.wait(100)
        time.sleep(2)
        
    def main():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    display_text_animation("""MADLADS PRESENT""", 250, 100, (0,255,0), 30)
    display_text_animation("""WORLD WAR III """, 250, 100, (0,0,255), 30)
    display_text_animation("""You're Donald Trump, President of the US. """, 250, 100, WHITE, 10)
    display_text_animation(""" Your country is at odds with Iran, China, and Russia """, 250, 100, WHITE, 10)
    display_text_animation(""" choose the path forward wisely. """, 250, 100, WHITE, 10)
    display_text_animation(""" Loading ... """, 250, 100, RED, 20)
    display_text_animation(""" Loading ... """, 250, 100, RED, 20)
    display_text_animation(""" Loading ... """, 250, 100, RED, 20)
    display_text_animation(""" Loading ... """, 250, 100, RED, 20)
    pygame.mixer.music.stop()
    qn_temp("Somewhere in Iran", 280, 
            """1,150,000 people stand in a circle. One of them is an undercover agent. There is a sword in 
            the hand of the 1st person, he kills the 2nd person and passes on the sword to the third, 
            who kills the fourth and gives the sword to the 5th, this goes on until one person is left. 
            At what position does the spy stand to survive?""", 10, "202849", options)