"""
Flagship file for the StickyJump platformer game
Proprietary content of StickyAR, 2019
Brought to you by Luke Igel, Fischer Moseley, Tim Gutterman, and Zach Rolfness
"""
import pygame as pg
from Settings import *
import subprocess

class Learn:
    def __init__(self):
        screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('Practice Mode')
        screen.fill(LIGHTPINK)
        pg.display.update()
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_a:
                        screen = pg.display.set_mode((WIDTH, HEIGHT))
                        pg.display.set_caption('Flashcard Mode') 
                        screen.fill(LIGHTPINK)
                        signletter = pg.image.load('../assets/signletters/A.png')
                        screen.blit(pg.transform.scale(signletter, (500, 500)), [255, 150])
                        pg.display.update()
                        subprocess.Popen(["say", "A"])
                    if event.key == pg.K_b:
                        screen = pg.display.set_mode((WIDTH, HEIGHT))
                        pg.display.set_caption('Flashcard Mode') 
                        screen.fill(LIGHTPINK)
                        signletter = pg.image.load('../assets/signletters/B.png')
                        screen.blit(pg.transform.scale(signletter, (500, 500)), [255, 150])
                        pg.display.update()
                        subprocess.Popen(["say", "B"])
                    if event.key == pg.K_c:
                        screen = pg.display.set_mode((WIDTH, HEIGHT))
                        pg.display.set_caption('Flashcard Mode') 
                        screen.fill(LIGHTPINK)
                        signletter = pg.image.load('../assets/signletters/C.png')
                        screen.blit(pg.transform.scale(signletter, (500, 500)), [255, 150])
                        pg.display.update()
                        subprocess.Popen(["say", "C"])
                    if event.key == pg.K_d:
                        screen = pg.display.set_mode((WIDTH, HEIGHT))
                        pg.display.set_caption('Flashcard Mode') 
                        screen.fill(LIGHTPINK)
                        signletter = pg.image.load('../assets/signletters/D.png')
                        screen.blit(pg.transform.scale(signletter, (500, 500)), [255, 150])
                        pg.display.update()
                        subprocess.Popen(["say", "D"])
                    if event.key == pg.K_e:
                        screen = pg.display.set_mode((WIDTH, HEIGHT))
                        pg.display.set_caption('Flashcard Mode') 
                        screen.fill(LIGHTPINK)
                        signletter = pg.image.load('../assets/signletters/E.png')
                        screen.blit(pg.transform.scale(signletter, (500, 500)), [255, 150])
                        pg.display.update()
                        subprocess.Popen(["say", "E"])
                    if event.key == pg.K_f:
                        screen = pg.display.set_mode((WIDTH, HEIGHT))
                        pg.display.set_caption('Flashcard Mode') 
                        screen.fill(LIGHTPINK)
                        signletter = pg.image.load('../assets/signletters/F.png')
                        screen.blit(pg.transform.scale(signletter, (500, 500)), [255, 150])
                        pg.display.update()
                        subprocess.Popen(["say", "F"])
                    if event.key == pg.K_g:
                        screen = pg.display.set_mode((WIDTH, HEIGHT))
                        pg.display.set_caption('Flashcard Mode') 
                        screen.fill(LIGHTPINK)
                        signletter = pg.image.load('../assets/signletters/G.png')
                        screen.blit(pg.transform.scale(signletter, (500, 500)), [255, 150])
                        pg.display.update()
                        subprocess.Popen(["say", "G"])
                    if event.key == pg.K_h:
                        screen = pg.display.set_mode((WIDTH, HEIGHT))
                        pg.display.set_caption('Flashcard Mode') 
                        screen.fill(LIGHTPINK)
                        signletter = pg.image.load('../assets/signletters/H.png')
                        screen.blit(pg.transform.scale(signletter, (500, 500)), [255, 150])
                        pg.display.update()
                        subprocess.Popen(["say", "H"])
                    if event.key == pg.K_i:
                        screen = pg.display.set_mode((WIDTH, HEIGHT))
                        pg.display.set_caption('Flashcard Mode') 
                        screen.fill(LIGHTPINK)
                        signletter = pg.image.load('../assets/signletters/I.png')
                        screen.blit(pg.transform.scale(signletter, (500, 500)), [255, 150])
                        pg.display.update()
                        subprocess.Popen(["say", "I"])
                    if event.key == pg.K_j:
                        screen = pg.display.set_mode((WIDTH, HEIGHT))
                        pg.display.set_caption('Flashcard Mode') 
                        signletter = pg.image.load('../assets/signletters/J.png')
                        screen.fill(LIGHTPINK)
                        screen.blit(pg.transform.scale(signletter, (500, 500)), [255, 150])
                        pg.display.update()
                        subprocess.Popen(["say", "J"])
                    if event.key == pg.K_k:
                        screen = pg.display.set_mode((WIDTH, HEIGHT))
                        pg.display.set_caption('Flashcard Mode') 
                        signletter = pg.image.load('../assets/signletters/K.png')
                        screen.fill(LIGHTPINK)
                        screen.blit(pg.transform.scale(signletter, (500, 500)), [255, 150])
                        pg.display.update()
                        subprocess.Popen(["say", "K"])
                    if event.key == pg.K_l:
                        screen = pg.display.set_mode((WIDTH, HEIGHT))
                        pg.display.set_caption('Flashcard Mode') 
                        signletter = pg.image.load('../assets/signletters/L.png')
                        screen.fill(LIGHTPINK)
                        screen.blit(pg.transform.scale(signletter, (500, 500)), [255, 150])
                        pg.display.update()
                        subprocess.Popen(["say", "L"])         
                    if event.key == pg.K_m:
                        screen = pg.display.set_mode((WIDTH, HEIGHT))
                        pg.display.set_caption('Flashcard Mode') 
                        signletter = pg.image.load('../assets/signletters/M.png')
                        screen.fill(LIGHTPINK)
                        screen.blit(pg.transform.scale(signletter, (500, 500)), [255, 150])
                        pg.display.update()
                        subprocess.Popen(["say", "M"])
                    if event.key == pg.K_n:
                        screen = pg.display.set_mode((WIDTH, HEIGHT))
                        pg.display.set_caption('Flashcard Mode') 
                        signletter = pg.image.load('../assets/signletters/N.png')
                        screen.fill(LIGHTPINK)
                        screen.blit(pg.transform.scale(signletter, (500, 500)), [255, 150])
                        pg.display.update()
                        subprocess.Popen(["say", "N"])
                    if event.key == pg.K_o:
                        screen = pg.display.set_mode((WIDTH, HEIGHT))
                        pg.display.set_caption('Flashcard Mode') 
                        signletter = pg.image.load('../assets/signletters/O.png')
                        screen.fill(LIGHTPINK)
                        screen.blit(pg.transform.scale(signletter, (500, 500)), [255, 150])
                        pg.display.update()
                        subprocess.Popen(["say", "O"])            
                    if event.key == pg.K_p:
                        screen = pg.display.set_mode((WIDTH, HEIGHT))
                        pg.display.set_caption('Flashcard Mode') 
                        signletter = pg.image.load('../assets/signletters/P.png')
                        screen.fill(LIGHTPINK)
                        screen.blit(pg.transform.scale(signletter, (500, 500)), [255, 150])
                        pg.display.update()
                        subprocess.Popen(["say", "P"])
                    if event.key == pg.K_q:
                        screen = pg.display.set_mode((WIDTH, HEIGHT))
                        pg.display.set_caption('Flashcard Mode') 
                        signletter = pg.image.load('../assets/signletters/Q.png')
                        screen.fill(LIGHTPINK)
                        screen.blit(pg.transform.scale(signletter, (500, 500)), [255, 150])
                        pg.display.update()
                        subprocess.Popen(["say", "Q"])
                    if event.key == pg.K_r:
                        screen = pg.display.set_mode((WIDTH, HEIGHT))
                        pg.display.set_caption('Flashcard Mode') 
                        signletter = pg.image.load('../assets/signletters/R.png')
                        screen.fill(LIGHTPINK)
                        screen.blit(pg.transform.scale(signletter, (500, 500)), [255, 150])
                        pg.display.update()
                        subprocess.Popen(["say", "R"])        
                    if event.key == pg.K_s:
                        screen = pg.display.set_mode((WIDTH, HEIGHT))
                        pg.display.set_caption('Flashcard Mode') 
                        signletter = pg.image.load('../assets/signletters/S.png')
                        screen.fill(LIGHTPINK)
                        screen.blit(pg.transform.scale(signletter, (500, 500)), [255, 150])
                        pg.display.update()
                        subprocess.Popen(["say", "S"])
                    if event.key == pg.K_t:
                        screen = pg.display.set_mode((WIDTH, HEIGHT))
                        pg.display.set_caption('Flashcard Mode') 
                        screen.fill(LIGHTPINK)
                        signletter = pg.image.load('../assets/signletters/T.png')
                        screen.blit(pg.transform.scale(signletter, (500, 500)), [255, 150])
                        pg.display.update()
                        subprocess.Popen(["say", "T"])
                    if event.key == pg.K_u:
                        screen = pg.display.set_mode((WIDTH, HEIGHT))
                        pg.display.set_caption('Flashcard Mode') 
                        screen.fill(LIGHTPINK)
                        signletter = pg.image.load('../assets/signletters/U.png')
                        screen.blit(pg.transform.scale(signletter, (500, 500)), [255, 150])
                        pg.display.update()
                        subprocess.Popen(["say", "U"])      
                    if event.key == pg.K_v:
                        screen = pg.display.set_mode((WIDTH, HEIGHT))
                        pg.display.set_caption('Flashcard Mode') 
                        screen.fill(LIGHTPINK)
                        signletter = pg.image.load('../assets/signletters/V.png')
                        screen.blit(pg.transform.scale(signletter, (500, 500)), [255, 150])
                        pg.display.update()
                        subprocess.Popen(["say", "V"])
                    if event.key == pg.K_w:
                        screen = pg.display.set_mode((WIDTH, HEIGHT))
                        pg.display.set_caption('Flashcard Mode') 
                        screen.fill(LIGHTPINK)
                        signletter = pg.image.load('../assets/signletters/W.png')
                        screen.blit(pg.transform.scale(signletter, (500, 500)), [255, 150])
                        pg.display.update()
                        subprocess.Popen(["say", "W"])
                    if event.key == pg.K_x:
                        screen = pg.display.set_mode((WIDTH, HEIGHT))
                        pg.display.set_caption('Flashcard Mode') 
                        screen.fill(LIGHTPINK)
                        signletter = pg.image.load('../assets/signletters/X.png')
                        screen.blit(pg.transform.scale(signletter, (500, 500)), [255, 150])
                        pg.display.update()
                        subprocess.Popen(["say", "X"])    
                    if event.key == pg.K_y:
                        screen = pg.display.set_mode((WIDTH, HEIGHT))
                        pg.display.set_caption('Flashcard Mode') 
                        screen.fill(LIGHTPINK)
                        signletter = pg.image.load('../assets/signletters/Y.png')
                        screen.blit(pg.transform.scale(signletter, (500, 500)), [255, 150])
                        pg.display.update()
                        subprocess.Popen(["say", "Y"])
                    if event.key == pg.K_z:
                        screen = pg.display.set_mode((WIDTH, HEIGHT))
                        pg.display.set_caption('Flashcard Mode') 
                        screen.fill(LIGHTPINK)
                        signletter = pg.image.load('../assets/signletters/Z.png')
                        screen.blit(pg.transform.scale(signletter, (500, 500)), [255, 150])
                        pg.display.update()
                        subprocess.Popen(["say", "Z"])
                    if event.key == pg.K_ESCAPE:
                        running = False


    
    def show_start_screen(self):
        screen = pg.display.set_mode((700, 700))
        pg.display.set_caption('Practice Mode')
        screen.fill(LIGHTPINK)
        pg.display.update()
        pass
