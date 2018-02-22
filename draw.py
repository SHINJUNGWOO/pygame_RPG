from excution import execution

import pygame
execution()
# picture[0],picture[1] is always door list, alway clear

def map1def():


    object=[]
    objectrect=[]
    object.append(pygame.image.load("graphic/road2.png"))
    object.append(pygame.image.load("graphic/road_go.png"))
    for i in range(len(object)):
        objectrect.append(object[i].get_rect())


    objectrect[0].left=462
    objectrect[0].top=0
    objectrect[1].left=462
    objectrect[1].top=0

    object_num=len(object)
    return [object,objectrect,object_num]
    #[allpicture list,allpicturerect,allobject_num,door last list num]
def map2def():


    object=[]
    objectrect=[]

    for i in range(len(object)):
        objectrect.append(object[i].get_rect())

    object_num=len(objectrect)
    return [object,objectrect,object_num]

def map3def():
    object=[]
    objectrect=[]
    for i in range(4):
        object.append(pygame.image.load("graphic/carpet1.png"))
    object.append(pygame.image.load("graphic/road1.png"))
    object.append(pygame.image.load("graphic/road2.png"))
    for i in range(4):
        object.append(pygame.image.load("graphic/house1.png"))
    object.append(pygame.image.load("graphic/carpet1.png"))

    for i in range(len(object)):
        objectrect.append(object[i].get_rect())

    objectrect[0].left=112
    objectrect[0].top=128
    objectrect[1].left=880
    objectrect[1].top=128
    objectrect[2].left=112
    objectrect[2].top=416
    objectrect[3].left=880
    objectrect[3].top=416

    objectrect[4].left=0
    objectrect[4].top=192
    objectrect[5].left=446
    objectrect[5].top=0

    objectrect[6].left=0
    objectrect[6].top=0
    objectrect[7].left=768
    objectrect[7].top=0
    objectrect[8].left=0
    objectrect[8].top=288
    objectrect[9].left=768
    objectrect[9].top=288
    objectrect[10].left=498
    objectrect[10].bottom=512

    object_num = len(objectrect)
    return [object, objectrect, object_num]
def mapdraw(screen,hero,picture,picturerect,objectnum):

    for i in range(objectnum):
        screen.blit(picture[i],picturerect[i])

    screen.blit(hero.picture,hero.picturerect)