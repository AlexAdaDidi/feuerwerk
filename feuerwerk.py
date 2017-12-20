# -*- coding: utf-8 -*-
"""
003_static_blit_pretty.py
static blitting and drawing (pretty version)
url: http://thepythongamebook.com/en:part2:pygame:step003
author: horst.jens@spielend-programmieren.at
licence: gpl, see http://www.gnu.org/licenses/gpl.html

works with pyhton3.4 and python2.7

Blitting a surface on a static position
Drawing a filled circle into ballsurface.
Blitting this surface once.
introducing pygame draw methods
The ball's rectangular surface is black because the background
color of the ball's surface was never defined nor filled."""

import random
import pygame 
import os
import sys

################## http://www.pygame.org/wiki/2DVectorClass ##################
import operator
import math
import vectorclass2d as v


                              
class VectorSprite(pygame.sprite.Sprite):
    pointlist = []
    
    def __init__(self, pos=v.Vec2d(100,100), move=v.Vec2d(50,0)):
        self._layer = 1
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.pos = v.Vec2d(pos.x, pos.y)
        self.move = v.Vec2d(move.x, move.y)
        self.create_image()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos.x, self.pos.y
        self.lifetime = None
        self.age = 0
    
    
    def update(self, seconds):
        self.age += seconds
        self.pos += self.move * seconds
        self.rect.center = (self.pos.x, self.pos.y)
        if self.lifetime is not None:
            self.lifetime -= seconds
            if self.lifetime < 0:
                self.kill()
        
    def create_image(self):
        minx = 0
        miny = 0
        maxx = 5
        maxy = 5
        for point in self.pointlist:
            if point.x < minx:
                minx = point.x
            if point.x > maxx:
                maxx = point.x
            if point.y < miny:
                miny = point.y
            if point.y > maxy:
                maxy = point.y
        self.image = pygame.Surface((maxx, maxy))
        pygame.draw.circle(self.image, (255,0,0), (2,2), 2)
        self.image.convert_alpha() 
        
class Ufo(VectorSprite):
  
    def update(self, seconds):
        # --- animate ---
        i = (self.age * 10) % 4 # modulo = rest of division by 3
        self.image = self.images[int(i)]
        # --- chance to change move vector ---
        if random.random() < 0.001:
            self.move=v.Vec2d(random.randint(-80,80),
                              random.randint(-80,80))
        # --- bounce on screen edge ---
        if self.pos.x < 0:
            self.pos.x = 0
            self.move.x *= -1
        elif self.pos.x > PygView.width:
            self.pos.x = PygView.width
            self.move.x *= -1
        if self.pos.y < 0:
            self.pos.y = 0
            self.move.y *= -1
        elif self.pos.y > PygView.height:
            self.pos.y = PygView.height
            self.move.y *= -1
        VectorSprite.update(self, seconds)
  
    def create_image(self):
        # ------ image0 ------
        self.image0 = pygame.Surface((100, 100))
        pygame.draw.line(self.image0, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (15, 50), (25, 25), 3)
        pygame.draw.line(self.image0, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (15, 50), (25, 75), 3)
        pygame.draw.line(self.image0, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (85, 50), (75, 25), 3)
        pygame.draw.line(self.image0, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (85, 50), (75, 75), 3)
        pygame.draw.line(self.image0, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (25, 25), (75, 25), 3)
        pygame.draw.line(self.image0, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (25, 75), (75, 75), 3)
        pygame.draw.circle(self.image0, (255,255,0), (50, 50), 7)
        pygame.draw.circle(self.image0, (255,0,0), (30, 50), 7)
        pygame.draw.circle(self.image0, (0,0,255), (70, 50), 7)
        pygame.draw.line(self.image0, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (25, 75), (15, 100), 3)
        pygame.draw.line(self.image0, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (40, 75), (35, 100), 3)
        pygame.draw.line(self.image0, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (55, 75), (60, 100), 3)
        pygame.draw.line(self.image0, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (70, 75), (80, 100), 3)
        self.image0.set_colorkey((0,0,0))
        self.image0.convert_alpha()
        # ------ image1 ------
        self.image1 = pygame.Surface((100, 100))
        pygame.draw.line(self.image1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (15, 50), (25, 25), 3)
        pygame.draw.line(self.image1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (15, 50), (25, 75), 3)
        pygame.draw.line(self.image1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (85, 50), (75, 25), 3)
        pygame.draw.line(self.image1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (85, 50), (75, 75), 3)
        pygame.draw.line(self.image1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (25, 25), (75, 25), 3)
        pygame.draw.line(self.image1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (25, 75), (75, 75), 3)
        pygame.draw.circle(self.image1, (0,0,255), (50, 50), 7)
        pygame.draw.circle(self.image1, (255,255,0), (30, 50), 7)
        pygame.draw.circle(self.image1, (255,0,0), (70, 50), 7)
        pygame.draw.line(self.image1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (25, 75), (15, 100), 3)
        pygame.draw.line(self.image1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (40, 75), (35, 100), 3)
        pygame.draw.line(self.image1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (55, 75), (60, 100), 3)
        pygame.draw.line(self.image1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (70, 75), (80, 100), 3)
        pygame.draw.line(self.image1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (25, 25), (15, 15), 3)
        pygame.draw.line(self.image1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (40, 25), (35, 15), 3)
        pygame.draw.line(self.image1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (55, 25), (60, 15), 3)
        pygame.draw.line(self.image1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (70, 25), (80, 15), 3)
        self.image1.set_colorkey((0,0,0))
        self.image1.convert_alpha()
        # ------ image2 ------
        self.image2 = pygame.Surface((100, 100))
        pygame.draw.line(self.image2, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (15, 50), (25, 25), 3)
        pygame.draw.line(self.image2, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (15, 50), (25, 75), 3)
        pygame.draw.line(self.image2, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (85, 50), (75, 25), 3)
        pygame.draw.line(self.image2, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (85, 50), (75, 75), 3)
        pygame.draw.line(self.image2, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (25, 25), (75, 25), 3)
        pygame.draw.line(self.image2, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (25, 75), (75, 75), 3)
        pygame.draw.circle(self.image2, (255,0,0), (50, 50), 7)
        pygame.draw.circle(self.image2, (0,0,255), (30, 50), 7)
        pygame.draw.circle(self.image2, (255,255,0), (70, 50), 7)
        pygame.draw.line(self.image2, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (25, 75), (15, 100), 3)
        pygame.draw.line(self.image2, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (40, 75), (35, 100), 3)
        pygame.draw.line(self.image2, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (55, 75), (60, 100), 3)
        pygame.draw.line(self.image2, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (70, 75), (80, 100), 3)
        self.image2.set_colorkey((0,0,0))
        self.image2.convert_alpha()
        # --- image3 ---
        self.image3 = pygame.Surface((100, 100))
        pygame.draw.line(self.image3, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (15, 50), (25, 25), 3)
        pygame.draw.line(self.image3, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (15, 50), (25, 75), 3)
        pygame.draw.line(self.image3, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (85, 50), (75, 25), 3)
        pygame.draw.line(self.image3, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (85, 50), (75, 75), 3)
        pygame.draw.line(self.image3, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (25, 25), (75, 25), 3)
        pygame.draw.line(self.image3, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (25, 75), (75, 75), 3)
        pygame.draw.circle(self.image3, (0,0,255), (50, 50), 7)
        pygame.draw.circle(self.image3, (255,255,0), (30, 50), 7)
        pygame.draw.circle(self.image3, (255,0,0), (70, 50), 7)
        pygame.draw.line(self.image3, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (25, 75), (15, 100), 3)
        pygame.draw.line(self.image3, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (40, 75), (35, 100), 3)
        pygame.draw.line(self.image3, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (55, 75), (60, 100), 3)
        pygame.draw.line(self.image3, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (70, 75), (80, 100), 3)
        pygame.draw.line(self.image3, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (25, 25), (15, 15), 3)
        pygame.draw.line(self.image3, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (40, 25), (35, 15), 3)
        pygame.draw.line(self.image3, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (55, 25), (60, 15), 3)
        pygame.draw.line(self.image3, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (70, 25), (80, 15), 3)
        self.image3.set_colorkey((0,0,0))
        self.image3.convert_alpha()
        # --------------
        self.images = [self.image0, self.image1, self.image2, self.image3]
        self.image = self.images[0]        
        
class Fragment(VectorSprite):
    def __init__(self, pos=v.Vec2d(100,100), move=None, color=None, gravity=None, lifetime=None, clone=False, radius=2):
        self.radius = radius
        if gravity is not None:
            self.gravity = v.Vec2d(gravity.x, gravity.y)
        else:
            self.gravity = gravity
        if color is not None:
            self.color = color
        else:
            self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        if move is not None:
            self.move = v.Vec2d(move.x, move.y)
        else:
            self.move = v.Vec2d(0,random.randint(5,250))
            self.move.rotate(random.randint(0,360))
        self.clone = clone
        VectorSprite.__init__(self, pos, self.move)
        if lifetime is not None:
            self.lifetime = lifetime
        else:
            self.lifetime = 0.1 + random.random() * 3
            
    def update(self, seconds):
        VectorSprite.update(self, seconds)
        if self.gravity is not None:
            self.move += self.gravity * seconds
        if self.clone and random.random() < 0.5:
            Smoke(pos=self.pos, move=v.Vec2d(0,0), color=self.color, lifetime=0.8)
        
    def create_image(self):
        self.image = pygame.Surface((self.radius*2,self.radius*2))
        pygame.draw.circle(self.image, self.color, (self.radius,self.radius), self.radius)
        self.image.set_colorkey((0,0,0))
        self.image.convert_alpha()
        
class Spark(Fragment):
    
    def create_image(self):
        self.image = pygame.Surface((50,50))
        self.color = (random.randint(200, 255), random.randint(128, 220), 50)
        pygame.draw.circle(self.image, self.color, (25,25), 2)
        self.image.set_colorkey((0,0,0))
        self.image.convert_alpha()
        
    def update(self, seconds):
        VectorSprite.update(self, seconds)
        if self.gravity is not None:
            self.move += self.gravity * seconds
        
        if self.age / 10 > 2:
            self.radius = self.age // 10
            self.create_image(self)
            
class Smoke(Fragment):
    def create_image(self):
        self.image = pygame.Surface((50,50))
        pygame.draw.circle(self.image, self.color, (25,25), 2)
        self.image.set_colorkey((0,0,0))
        self.image.convert_alpha()
        
    def update(self, seconds):
        VectorSprite.update(self, seconds)
        if self.gravity is not None:
            self.move += self.gravity * seconds
        if self.age / 10 > 2:
            self.radius = self.age // 10
            self.create_image(self)
        
class Rocket(Fragment):
    def __init__(self, startpos, target, speed=None, color=(150,99,0), ex=None):
            #leftcorner = v.Vec2d(0,self.height)
            #rightcorner = v.Vec2d(self.width,self.height)
            if speed is not None:
                self.speed = speed
            else:
                self.speed = random.randint(130,180)
            rocketcolor = color
            #speed = random.randint(150,180)
            rocketmove = target - startpos
            rockettime = rocketmove.length / self.speed
            rocketmove = rocketmove.normalized() * self.speed
            #leftmove = pos-leftcorner
            #lefttime = leftmove.length / speed
            #leftmove = leftmove.normalized() * speed
            Fragment.__init__(self, pos=startpos, move=rocketmove, color=rocketcolor, gravity=None, lifetime=rockettime)
            if ex is None:
                self.ex = random.randint(1,7)
            else:
                self.ex = ex
     
    def update(self, seconds):
          self.pos += self.move * seconds
          self.rect.center = (self.pos.x, self.pos.y)
          self.lifetime -= seconds
          if self.lifetime > 0:
              # black smoke
              if random.random() < 1:
                  Smoke(self.pos, move=self.move* -0.1, color=(19,0,0))  
              m = self.move * -1
              m.rotate(random.randint(-5, 5))
              Spark(self.pos, move = m)
          else:
          #if self.lifetime < 0:
                # explosion
                c1 = random.randint(0,255)
                c2 = random.randint(0,255)
                c3 = random.randint(0,255)
                c4 = random.randint(0,255)
                g = v.Vec2d(0,random.randint(100,250))
                
                explosion = self.ex 
                if explosion == 0:
                    for x in range(50):
                        Fragment(self.pos, gravity=None, color=(c1,c2,c3))
                
                elif explosion == 1:
                    for x in range(50):
                        Fragment(self.pos, gravity=g, color=(c1,c2,c3))
                
                elif explosion == 2:
                    m = v.Vec2d(random.randint(100,200), 0)
                    for x in range(72):
                        Fragment(self.pos, move=m, gravity=g, color=(c1,c2,c3))
                        m.rotate(5)
                
                elif explosion == 3:
                    m = v.Vec2d(random.randint(100,200), 0)
                    for x in range(72):
                        Fragment(self.pos, move=m, gravity=g, color=(c1,c2,c3), clone=True)
                        m.rotate(5)
                    
                elif explosion == 4:
                    m = v.Vec2d(100,0)
                    wieoft = random.randint(1,4)
                    winkel = random.randint(1,360)
                    for x in range(wieoft):
                        Rocket(self.pos, target=self.pos+m)
                        m.rotate(winkel)
                        
                elif explosion == 5:
                    m = v.Vec2d(100,0)
                    wieoft = random.randint(1,10)
                    winkel = random.randint(1,360)
                    for x in range(wieoft):
                        Rocket(self.pos, target=self.pos+m)
                        m.rotate(winkel)
                        
                elif explosion == 6:
                    m = v.Vec2d(random.randint(150,200), 0)
                    for x in range(36):
                        Fragment(self.pos, move=m)
                        m.rotate(10)
                        m *= 0.92 
                        
                elif explosion == 7:
                    m = v.Vec2d(random.randint(100,200), 0)
                    wieoft = random.randint(1,10)
                    winkel = random.randint(1,360)
                    wieoft2 = random.randint(1,2)
                    for x in range(wieoft):
                        Fragment(self.pos, move=m)
                        m.rotate(winkel)
                        m *= wieoft2
                
                self.kill()
                
      

            
    
class PygView(object):
  
    width = 0
    height = 0
  
    def __init__(self, width=1440, height=800, fps=30):
        """Initialize pygame, window, background, font,...
           default arguments 
        """
        pygame.init()
        pygame.display.set_caption("Press ESC to quit.")
        PygView.width = width    # also self.width 
        PygView.height = height  # also self.height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()  
        self.background.fill((255, 255, 255)) # yannik hier hintergrund färben
        # fill background white
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        self.font = pygame.font.SysFont('mono', 24, bold=True)
        self.allgroup = pygame.sprite.LayeredUpdates()
        VectorSprite.groups = self.allgroup
        Fragment.groups = self.allgroup
        
        # ------ background images ------
        self.backgroundfilenames = [] # every .jpg file in folder 'data'
        for root, dirs, files in os.walk("data"):
            for file in files:
                if file[-4:] == ".jpg" or file[-5:] == ".jpeg":
                    self.backgroundfilenames.append(file)
        random.shuffle(self.backgroundfilenames) # remix sort order
        if len(self.backgroundfilenames) == 0:
            print("Error: no .jpg files found")
            pygame.quit
            sys.exit()
        self.level = 1
        self.loadbackground()
        
    def loadbackground(self):
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((255,255,255)) # fill background white
        self.background = pygame.image.load(os.path.join("data", self.backgroundfilenames[self.level % len(self.backgroundfilenames)]))
        self.background = pygame.transform.scale(self.background, (PygView.width,PygView.height))
        self.background.convert()
        
        
        
    def run(self):
        """The mainloop
        """ 
        running = True
        leftcorner = v.Vec2d(0,self.height)
        rightcorner = v.Vec2d(self.width,self.height)
        middle = v.Vec2d(self.width//2,self.height)
        quarter = v.Vec2d(self.width//4,self.height)
        quarter3 = v.Vec2d(self.width//4*3,self.height)
        third = v.Vec2d(self.width//3, self.height)
        third2 = v.Vec2d(self.width//3*2, self.height)
        ground = (leftcorner,quarter,third,middle,third2, quarter3,rightcorner)
            
        while running:
            # --------- update time -------------            
            
            milliseconds = self.clock.tick(self.fps)
            seconds = milliseconds / 1000.0
            self.playtime += seconds
            
            text_time = "FPS: {:4.3} TIME: {:6.3} sec".format(self.clock.get_fps(), self.playtime)
            self.draw_text(text_time, x = self.width//2-200, y=30, color=(100,0,100))
            
            # ------ 
            
            pos = v.Vec2d(pygame.mouse.get_pos())
            
            # ------------ event handler: keys pressed and released -----
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_b:
                        self.level +=1
                        self.loadbackground()
                    if event.key == pygame.K_SPACE:
                        pos = v.Vec2d(self.width//2, self.height//2)
                        m = v.Vec2d(50,0)
                        for _ in range(36):
                            VectorSprite(pos,m)
                            m.rotate(10)
                    if event.key == pygame.K_0:
                        Rocket(random.choice(ground), pos, ex=0)
                    if event.key == pygame.K_1:
                        Rocket(random.choice(ground), pos, ex=1)
                        #Rocket(rightcorner, pos, ex=1)
                    if event.key == pygame.K_2:
                        Rocket(random.choice(ground), pos, ex=2)
                        #Rocket(rightcorner, pos, ex=2)
                    if event.key == pygame.K_3:
                        Rocket(random.choice(ground), pos, ex=3)
                        #Rocket(rightcorner, pos, ex=3)
                    if event.key == pygame.K_4:
                        Rocket(random.choice(ground), pos, ex=4)
                        #Rocket(rightcorner, pos, ex=4)
                    if event.key == pygame.K_5:
                        Rocket(random.choice(ground), pos, ex=5)
                        #Rocket(rightcorner, pos, ex=5)
                    if event.key == pygame.K_6:
                        Rocket(random.choice(ground), pos, ex=6)
                        #Rocket(rightcorner, pos, ex=6)
                    if event.key == pygame.K_7:
                        Rocket(random.choice(ground), pos, ex=7)
                        #Rocket(rightcorner, pos, ex=7)
                    if event.key == pygame.K_c:
                        self.background.fill((255,255,255))
                                        
            # --------- pressed key handler --------------            
            pressed = pygame.key.get_pressed()
            
            if pressed[pygame.K_f]:
                pos = v.Vec2d(self.width//2, self.height//2)
                Fragment(pos, gravity=v.Vec2d(0, 200))            
            # ------ mouse handler ------
            
            
            left,middle,right = pygame.mouse.get_pressed()
            if left:
                #Fragment(leftcorner,leftmove,lifetime=lefttime,color=(255,0,0))
                Rocket(leftcorner, pos)
            if right:
                Rocket(rightcorner, pos)
                #Fragment(pos, gravity=v.Vec2d(0,70), color=(random.randint(0,255,0)))
                #Fragment(rightcorner,rightmove,lifetime=righttime,color=(0,0,255))
                
            # ---------- update screen ----------- 
            self.screen.blit(self.background, (0, 0))
            # ------ sprite ------
            self.allgroup.update(seconds)
            self.allgroup.draw(self.screen)
            # ------ flip screen ------
            pygame.display.flip()
            
            
        pygame.quit()


    def draw_text(self, text, x=50, y=150, color=(0,0,0)):
        """Center text in window
        """
        fw, fh = self.font.size(text)
        surface = self.font.render(text, True, color)
        self.screen.blit(surface, (x,y))


    
####

if __name__ == '__main__':

    # call with width of window and fps
    PygView().run()
