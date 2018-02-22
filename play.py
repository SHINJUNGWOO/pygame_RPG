from draw import map1def,mapdraw,map2def,map3def
from excution import execution
from object import move
import pygame, sys

execution()
screen = pygame.display.set_mode((1024,512))
#map1def return[allpicture ,allpicture rect,object_num,doorpositon]

map1return=map1def()
map2return=map2def()
map3return=map3def()
hero = move()
fly=move()
fly.x = 50
fly.y = 50
fly.speed=0.25
fly.picture=pygame.image.load("graphic/fly.png")
while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill((0,0,0))

    move.playmove(hero, hero.crashcheck)


    if move.linecheck(hero):
        hero.crashcheck=1
    if move.linecheck(fly):
        fly.crashcheck=1
    if hero.crashcheck==1:
        move.moveback(hero)
        hero.crashcheck=0
    if fly.crashcheck==1:
        move.moveback(fly)
        hero.crashcheck=0
    picturechange="graphic/hero/hero"+str(hero.pressedcode%4)+"type"+str((int(hero.runcode/4))%3)+".png"
    hero.picture=pygame.image.load(picturechange)




#map choose section
    if hero.map==1:

        if hero.picturerect.colliderect(map1return[1][1]):
            hero.map = 3
            hero.x=450
            hero.y=420

        screen.fill((86,156,68))
        mapdraw(screen,hero,map1return[0],map1return[1],map1return[2])

    if hero.map==2:


        move.follow(fly,hero)
        screen.blit(fly.picture, fly.picturerect)
        mapdraw(screen,hero,map2return[0],map2return[1],map2return[2])

    if hero.map==3:
        if hero.picturerect.colliderect(map3return[1][0]):
            hero.map = 1
        if hero.picturerect.colliderect(map3return[1][1]):
            hero.map = 2
        if hero.picturerect.colliderect(map3return[1][2]):
            hero.map = 1
        if hero.picturerect.colliderect(map3return[1][3]):
            hero.map = 2
        if hero.picturerect.colliderect(map3return[1][10]):
            hero.map =1
            hero.x=450
            hero.y=16
        for i in range(6,10):
            if hero.picturerect.colliderect(map3return[1][i]):
                hero.crashcheck = 1



        screen.fill((86,156,68))
        mapdraw(screen,hero,map3return[0],map3return[1],map3return[2])
    pygame.display.flip()
