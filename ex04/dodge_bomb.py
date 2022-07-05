import re
import pygame as pg
import sys

def main():
    clock = pg.time.Clock()
    #問1
    pg.display.set_caption("逃げろ!こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900))          #Surface
    screen_rct = screen_sfc.get_rect()                     #Rect
    bgimg_sfc  = pg.image.load("fig/pg_bg.jpg")            #Surface
    bgimg_rct  = bgimg_sfc.get_rect()                      #Rect
    screen_sfc.blit(bgimg_sfc, bgimg_rct)

    #問3
    kkimg_sfc = pg.image.load("fig/3.png")                 #Surface
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)   #Surface
    kkimg_rct = kkimg_sfc.get_rect()                       #Rect
    kkimg_rct.center = 900, 400

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)
        #screen_sfc.blit(kkimg_sfc, kkimg_rct)
        
        #問2
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        #問4
        key_states = pg.key.get_pressed()                   #辞書
        if key_states[pg.K_UP]    == True: kkimg_rct.centery -=1         #y座標を-1
        if key_states[pg.K_DOWN]  == True: kkimg_rct.centery +=1         #y座標を+1
        if key_states[pg.K_LEFT]  == True: kkimg_rct.centerx -=1         #x座標を-1
        if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx +=1         #x座標を+1
        screen_sfc.blit(kkimg_sfc, kkimg_rct)

        pg.display.update()  
        clock.tick(1000)
        

if __name__ == "__main__":
    pg.init()
    main()     #実装するゲーム内容
    pg.quit()
    sys.exit()