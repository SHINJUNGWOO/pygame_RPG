import pygame
class move:

    def __init__(self):
        self.pressedcode=0
        self.x=462
        self.y=420
        self.runcode=0
        self.picture=pygame.image.load("graphic/hero/hero0type0.png")
        self.picturerect=self.picture.get_rect()
        self.map=1
        self.speed=1
        self.crashcheck=0
    def linecheck(self):

        if (self.x>960) or (self.x<0) or (self.y<0) or (self.y)>448:
            return 1
        else: return 0
    def up(self):

        self.y -= self.speed
        self.runcode+=1
        self.pressedcode=0
    def down(self):

        self.y += self.speed
        self.runcode +=1
        self.pressedcode = 1
    def left(self):

        self.x-=self.speed
        self.runcode+=1
        self.pressedcode=2

    def right(self):
        self.x+=self.speed
        self.runcode +=1
        self.pressedcode = 3

    def upleft(self):
        self.x-=self.speed
        self.y-=self.speed
        self.runcode +=1
        self.pressedcode = 4
    def upright(self):
        self.x+=self.speed
        self.y-=self.speed
        self.runcode +=1
        self.pressedcode = 5
    def downleft(self):
        self.x-=self.speed
        self.y+=self.speed
        self.runcode +=1
        self.pressedcode = 6
    def downright(self):
        self.x+=self.speed
        self.y+=self.speed
        self.runcode +=1
        self.pressedcode = 7
    def moveback(self):
        if self.pressedcode==0:
            self.y+=self.speed
        if self.pressedcode==1:
            self.y-=self.speed
        if self.pressedcode==2:
            self.x+=self.speed
        if self.pressedcode==3:
            self.x-=self.speed
        if self.pressedcode==4:
            self.x+=self.speed
            self.y+=self.speed
        if self.pressedcode==5:
            self.x-=self.speed
            self.y+=self.speed
        if self.pressedcode==6:
            self.x+=self.speed
            self.y-=self.speed
        if self.pressedcode==7:
            self.x-=self.speed
            self.y-=self.speed
    def playmove(self,crashcheck):
        pressed = pygame.key.get_pressed()
        if crashcheck == 1:
            move.moveback(self)

        else:
            if pressed[pygame.K_UP] and pressed[pygame.K_LEFT]:
                self.upleft()
            elif pressed[pygame.K_UP] and pressed[pygame.K_RIGHT]:
                move.upright(self)
            elif pressed[pygame.K_DOWN] and pressed[pygame.K_LEFT]:
                move.downleft(self)
            elif pressed[pygame.K_DOWN] and pressed[pygame.K_RIGHT]:
                move.downright(self)
            elif pressed[pygame.K_UP]:
                move.up(self)

            elif pressed[pygame.K_DOWN]:
                move.down(self)
            elif pressed[pygame.K_LEFT]:
                move.left(self)

            elif pressed[pygame.K_RIGHT]:
                move.right(self)

        self.picturerect.left=self.x
        self.picturerect.top=self.y
    def follow(self,hero):
        if (hero.x>self.x):
            if hero.y==self.y:
                move.right(self)
            if hero.y<self.y:
                move.upright(self)
            if hero.y>self.y:
                move.downright(self)

        if (hero.x < self.x):
            if hero.y == self.y:
                move.left(self)
            if hero.y < self.y:
                move.upleft(self)
            if hero.y > self.y:
                move.downleft(self)

        if (hero.x == self.x):
            if hero.y < self.y:
                move.up(self)
            if hero.y > self.y:
                move.down(self)
        self.picturerect.left = self.x
        self.picturerect.top = self.y


