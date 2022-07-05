import pygame as pg
import sys
import random

def main():
    clock = pg.time.Clock()
    #問1　スクリーンと背景画像
    pg.display.set_caption("逃げろ!こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900))          #Surface
    screen_rct = screen_sfc.get_rect()                     #Rect
    bgimg_sfc  = pg.image.load("fig/pg_bg.jpg")            #Surface
    bgimg_rct  = bgimg_sfc.get_rect()                      #Rect
    screen_sfc.blit(bgimg_sfc, bgimg_rct)

    #問3　こうかとん
    kkimg_sfc = pg.image.load("fig/3.png")                 #Surface
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)   #Surface
    kkimg_rct = kkimg_sfc.get_rect()                       #Rect
    kkimg_rct.center = 900, 400

    #問5 爆弾
    bomimg_sfc = pg.Surface((20, 20))                      #Surface
    bomimg_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomimg_sfc, (255, 0, 0), (10,10), 10)
    #pg.draw.circle(bomimg_sfc, (191, 0, 0), (10,10), 40)
    #pg.draw.circle(bomimg_sfc, (127, 0, 0), (10,10), 30)
    #pg.draw.circle(bomimg_sfc, ( 63, 0, 0), (10,10), 20)
    #pg.draw.circle(bomimg_sfc, (  0, 0, 0), (10,10), 10)

    bomimg_rct = bomimg_sfc.get_rect()
    bomimg_rct.centerx = random.randint(0, screen_rct.width)
    bomimg_rct.centery = random.randint(0, screen_rct.height)
    vx, vy = +1, +1

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
        if check_bound(kkimg_rct, screen_rct) != (1, 1):                 #領域外ならば
            if key_states[pg.K_UP]    == True: kkimg_rct.centery +=1         #y座標を-1
            if key_states[pg.K_DOWN]  == True: kkimg_rct.centery -=1         #y座標を+1
            if key_states[pg.K_LEFT]  == True: kkimg_rct.centerx +=1         #x座標を-1
            if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx -=1         #x座標を+1
        screen_sfc.blit(kkimg_sfc, kkimg_rct)

        #問6
        bomimg_rct.move_ip(vx, vy)
        #問5
        screen_sfc.blit(bomimg_sfc, bomimg_rct)
        #問7
        yoko, tate = check_bound(bomimg_rct, screen_rct)
        vx *= yoko
        vy *= tate

        pg.display.update()  
        clock.tick(1000)

#問7
def check_bound(rct, scr_rct):
    #[1] rct: こうかとん　or 爆弾のRect
    #[2] scr_rct: スクリーンのRect

    yoko, tate = +1, +1 #領域内を表す
    if rct.left < scr_rct.left or scr_rct.right  < rct.right: yoko = -1
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1
    return yoko, tate

if __name__ == "__main__":
    pg.init()
    main()     #実装するゲーム内容
    pg.quit()
    sys.exit()