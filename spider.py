import pygame
import random
import time

pygame.init()
disp_width=700
disp_height=600
screen=pygame.display.set_mode((disp_width,disp_height))
clock=pygame.time.Clock()
pygame.display.set_caption("SPIDER HUNT")
img=pygame.image.load("C:/Users/Administrator.DESKTOP-C9E863I/Desktop/spider1.png")
icon=pygame.image.load("C:/Users/Administrator.DESKTOP-C9E863I/Desktop/spider.png")
pygame.display.set_icon(icon)
wasted=pygame.mixer.Sound("C:/Users/Administrator.DESKTOP-C9E863I/Downloads/crash.wav")

def button(x,y,w,h,d_col,l_col,msg,p,eas=0):
    mouse_pos=pygame.mouse.get_pos()
    mouse_press=pygame.mouse.get_pressed()

    if x<mouse_pos[0]<x+w and y<mouse_pos[1]<y+h:
        pygame.draw.rect(screen,d_col,(x,y,w,h))
        if mouse_press[0]==1:
            if msg=="RESUME":
                return 1
            elif msg in ["Retry","Easy","Medium","Hard","Home","Restart"]:
                eas()
            elif msg=="Quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(screen,l_col,(x,y,w,h))
        
    txt=pygame.font.Font("C:/Windows/Fonts/BowlbyOneSC-Regular.ttf",20)
    text=txt.render(msg,True,(0,0,0))
    screen.blit(text,p)

def home():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill((95,95,95))
        button(disp_width/4.8,disp_height/2,80,60,(0,150,0),(0,200,0),"Easy",((disp_width/4.8)+14,(disp_height/2)+15),easy)
        button(disp_width/2.35,disp_height/2,100,60,(180,130,5),(250,152,5),"Medium",((disp_width/2.35)+8,(disp_height/2)+15),medium)
        button(disp_width/1.5,disp_height/2,80,60,(150,0,0),(200,0,0),"Hard",((disp_width/1.5)+12,(disp_height/2)+15),hard)
        txt=pygame.font.Font("C:/Windows/Fonts/dead.ttf",70)
        text=txt.render("SPIDER HUNT",True,(0,0,0))
        screen.blit(text,(disp_width/4.8,disp_height/3.5))
        t=pygame.font.Font("C:/Windows/Fonts/ebrima.ttf",20)
        T=t.render("© ASHMIT RAJ",True,(0,0,0))
        screen.blit(T,(disp_width/2.5,disp_height/1.2))
        pygame.display.update()
def pause(eas):
    pygame.mixer.music.pause()
    f=0
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p or event.key==pygame.K_SPACE:
                    return
        f=button(disp_width/5,disp_height/2,100,60,(0,150,0),(0,200,0),"RESUME",((disp_width/5)+3,(disp_height/2)+15))
        if f:
            return
        button(disp_width/2.35,disp_height/2,100,60,(180,130,5),(250,152,5),"Restart",((disp_width/2.35)+6,(disp_height/2)+15),eas)
        button(disp_width/1.5,disp_height/2,80,60,(150,0,0),(200,0,0),"Quit",((disp_width/1.5)+15,(disp_height/2)+15))
        text=pygame.font.Font("C:/Windows/Fonts/StencilStd.otf",60)
        txt=text.render("Paused",True,(0,0,0))
        screen.blit(txt,(disp_width/3.1  ,disp_height/4))
        pygame.display.update()
def game_over(eas):
    pygame.mixer.Sound.play(wasted)
    pygame.mixer.music.stop()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        button(disp_width/4.8,disp_height/1.6,100,50,(0,150,0),(0,200,0),"Retry",((disp_width/4.8)+20,(disp_height/1.6)+8),eas)
        button(disp_width/2.3,disp_height/1.6,100,50,(180,130,5),(250,152,5),"Home",((disp_width/2.3)+20,(disp_height/1.6)+8),home)
        button(disp_width/1.5,disp_height/1.6,100,50,(150,0,0),(200,0,0),"Quit",((disp_width/1.5)+23,(disp_height/1.6)+8))
        text=pygame.font.Font("C:/Windows/Fonts/BlackoakStd.otf",50)
        txt=text.render("WASTED",True,(0,0,0))
        screen.blit(txt,(disp_width/9,disp_height/2.5))
        pygame.display.update()
        
def bubbles(x,y,f1,f2,f3,f4):
    if f1:
        pygame.draw.circle(screen,(255,255,0),(x,y),5)
    if f2:
        pygame.draw.circle(screen,(255,255,0),(x-70,y),5)
    if f3:
        pygame.draw.circle(screen,(255,255,0),(x+140,y),5)
    if f4:
        pygame.draw.circle(screen,(255,255,0),(x-90,y),5)
    
def score(point):
    text=pygame.font.Font("C:/Windows/Fonts/BlackoakStd.otf",20)
    txt=text.render("Score : "+str(point),True,(0,0,0))
    screen.blit(txt,(0,10))
def easy():
    pygame.mixer.music.load("C:/Users/Administrator.DESKTOP-C9E863I/Downloads/dont_shoot.wav")
    pygame.mixer.music.play(-1)
    x=disp_width/2.8
    y=disp_height-190
    move_x=move_y=c=i=0
    point=m=0
    

    X=random.randrange(0,disp_width-61)
    t=random.randrange(70,250)
    Y=bub_y=-disp_height
    h=60
    w=60

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT or event.key==pygame.K_a:
                    move_x=-5
                if event.key==pygame.K_RIGHT or event.key==pygame.K_d:
                    move_x=5
                if event.key==pygame.K_UP or event.key==pygame.K_w:
                    move_y=-5
                if event.key==pygame.K_DOWN or event.key==pygame.K_s:
                    move_y=5
                if event.key==pygame.K_p or event.key==pygame.K_SPACE:
                    pause(easy)
                    pygame.mixer.music.unpause()
            if event.type==pygame.KEYUP:
                if event.key in [pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN,pygame.K_a,pygame.K_d,pygame.K_w,pygame.K_s]:
                    move_x=move_y=0
        x+=move_x
        y+=move_y
        screen.fill((95,95,95))

        Y+=5+i
        if Y>disp_height:
            Y=-61
            X=random.randrange(0,disp_width-61)
            t=random.randrange(70,250)
            m=0
        screen.blit(img,(x,y))

        score(point)
    
        pygame.draw.rect(screen,(102,51,0),[X+t,Y,w,h])
        pygame.draw.rect(screen,(102,51,0),[X,Y,w,h])
        if x+61>disp_width or x<0:
            game_over(easy)
        if y+59>disp_height or y<0:
            game_over(easy)
        if Y+h>y and Y<y:
            if (X<x<X+w or X<x+61<X+w)  or (X+t<x<X+t+w or X+t<x+61<X+t+w):
                game_over(easy)
            elif m==0:
                point+=1
                m+=1
        pygame.display.update()
        clock.tick(60)
        c+=1
        if c>500 and c<580:
            if c%10==0:
                i+=1

def medium():
    pygame.mixer.music.load("C:/Users/Administrator.DESKTOP-C9E863I/Downloads/dont_shoot.wav")
    pygame.mixer.music.play(-1)
    x=disp_width/2.8
    y=disp_height-190
    move_x=move_y=0
    fire=i=c=point=m=n=o=f1=f2=f3=f4=0
    p=q=r=d1=d2=d3=d4=1

    X=random.randrange(0,disp_width-61)
    t=random.randrange(70,250)
    Y=bub_y=-disp_height
    h=60
    w=60
    bub_x=random.randrange(0,disp_width-70)

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT or event.key==pygame.K_a:
                    move_x=-5
                if event.key==pygame.K_RIGHT or event.key==pygame.K_d:
                    move_x=5
                if event.key==pygame.K_UP or event.key==pygame.K_w:
                    move_y=-5
                if event.key==pygame.K_DOWN or event.key==pygame.K_s:
                    move_y=5
                if event.key==pygame.K_p or event.key==pygame.K_SPACE:
                    pause(medium)
                    pygame.mixer.music.unpause()
            if event.type==pygame.KEYUP:
                if event.key in [pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN,pygame.K_a,pygame.K_d,pygame.K_w,pygame.K_s]:
                    move_x=move_y=0
        x+=move_x
        y+=move_y
        if abs(fire)>y:
            fire =0
        fire-=(7+i)
        screen.fill((95,95,95))

        Y+=5+i
        if Y>disp_height:
            Y=-61
            X=random.randrange(0,disp_width-61)
            t=random.randrange(70,250)
            p=q=r=1
            m=n=o=0

        pygame.draw.line(screen,(0,0,0),(x+28,y+fire),(x+28,y-20+fire))
        pygame.draw.line(screen,(0,0,0),(x+32,y+fire),(x+32,y-20+fire))
        screen.blit(img,(x,y))

        score(point)
        bub_y+=6
        bubbles(bub_x,bub_y,d1,d2,d3,d4)
        if bub_y>disp_height:
            bub_y=-10
            bub_x=random.randrange(0,disp_width-70)
            d1=d2=d3=d4=1
            f1=f2=f3=f4=0
        if (Y>0 and y-20+fire<Y+h and y-20+fire>Y) :
            if (X<x+28<X+w or X<x+32<X+w) and m==0:
                point+=1
                m+=1
                r=0
            elif (X-t<x+28<X-t+w or X-t<x+32<X-t+w) and n==0:
                point+=1
                n+=1
                p=0
            elif  (X+t<x+28<X+t+w or X+t<x+32<X+t+w) and o==0:
                point+=1
                o+=1
                q=0
        if p:
            pygame.draw.rect(screen,(102,51,0),[X-t,Y,w,h])
        if q:
            pygame.draw.rect(screen,(102,51,0),[X+t,Y,w,h])
        if r:
            pygame.draw.rect(screen,(102,51,0),[X,Y,w,h])
        if x+61>disp_width or x<0:
            game_over(medium)
        if y+59>disp_height or y<0:
            game_over(medium)
        if Y+h>y and Y<y:
            if ((X<x<X+w or X<x+61<X+w) and r) or ((X-t<x<X-t+w or X-t<x+61<X-t+w) and p) or ((X+t<x<X+t+w or X+t<x+61<X+t+w) and q):
                game_over(medium)
        if y<bub_y:
            #print("jghjgdf")
            if x<bub_x<x+w and f1==0:
                point+=2
                f1+=1
                d1=0
            if x<bub_x-70<x+w and f2==0:
                point+=2
                f2+=1
                d2=0
            if x<bub_x+140<x+w and f3==0:
                point+=2
                f3+=1
                d3=0
            if x<bub_x-90<x+w and f4==0:
                point+=2
                f4+=1
                d4=0
        pygame.display.update()
        clock.tick(60)
        c+=1
        if c>500 and c<560:
            if c%10==0:
                i+=1
def hard():
    pygame.mixer.music.load("C:/Users/Administrator.DESKTOP-C9E863I/Downloads/dont_shoot.wav")
    pygame.mixer.music.play(-1)
    x=disp_width/2.8
    y=disp_height-190
    move_x=move_y=k=0
    fire=i=c=point=m=n=o=f1=f2=f3=f4=b=0
    p=q=r=d1=d2=d3=d4=s=1

    X=random.randrange(0,disp_width-61)
    t=random.randrange(70,250)
    Y=bub_y=-disp_height
    h=60
    w=60
    bub_x=random.randrange(0,disp_width-70)

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT or event.key==pygame.K_a:
                    move_x=-5
                if event.key==pygame.K_RIGHT or event.key==pygame.K_d:
                    move_x=5
                if event.key==pygame.K_UP or event.key==pygame.K_w:
                    move_y=-5
                if event.key==pygame.K_DOWN or event.key==pygame.K_s:
                    move_y=5
                if event.key==pygame.K_p or event.key==pygame.K_SPACE:
                    pause(hard)
                    pygame.mixer.music.unpause()
            if event.type==pygame.KEYUP:
                if event.key in [pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN,pygame.K_a,pygame.K_d,pygame.K_w,pygame.K_s]:
                    move_x=move_y=0
        x+=move_x
        y+=move_y
        if abs(fire)>y:
            fire =0
        fire-=(7+i)
        screen.fill((95,95,95))

        Y+=5+i
        if Y>disp_height:
            Y=-61
            X=random.randrange(0,disp_width-61)
            t=random.randrange(70,250)
            p=q=r=s=1
            m=n=o=b=0

        pygame.draw.line(screen,(0,0,0),(x+28,y+fire),(x+28,y-20+fire))
        pygame.draw.line(screen,(0,0,0),(x+32,y+fire),(x+32,y-20+fire))
        screen.blit(img,(x,y))

        score(point)
        bub_y+=6
        bubbles(bub_x,bub_y,d1,d2,d3,d4)
        if bub_y>disp_height:
            bub_y=-10
            bub_x=random.randrange(0,disp_width-70)
            d1=d2=d3=d4=1
            f1=f2=f3=f4=0
        if (Y>0 and y-20+fire<Y+h and y-20+fire>Y) or (Y>0 and y+fire<Y+h and y+fire>Y ):
            if (X<x+28<X+w or X<x+32<X+w) and m==0:
                point+=1
                m+=1
                r=0
            elif (X-t<x+28<X-t+w or X-t<x+32<X-t+w) and n==0:
                point+=1
                n+=1
                p=0
            elif  (X+t<x+28<X+t+w or X+t<x+32<X+t+w) and o==0:
                point+=1
                o+=1
                q=0
            elif  (X+2*t<x+28<X+2*t+w or X+2*t<x+32<X+2*t+w) and b==0:
                point+=1
                b+=1
                s=0
        if p:
            pygame.draw.rect(screen,(102,51,0),[X-t,Y,w,h])
        if q:
            pygame.draw.rect(screen,(102,51,0),[X+t,Y,w,h])
        if r:
            pygame.draw.rect(screen,(102,51,0),[X,Y,w,h])
        if s:
            pygame.draw.rect(screen,(102,51,0),[X+2*t,Y,w,h])
        if x+61>disp_width or x<0:
            game_over(hard)
        if y+59>disp_height or y<0:
            game_over(hard)
        if Y+h>y and Y<y:
            if ((X<x<X+w or X<x+61<X+w) and r) or ((X-t<x<X-t+w or X-t<x+61<X-t+w) and p) or ((X+t<x<X+t+w or X+t<x+61<X+t+w) and q) or ((X+2*t<x<X+2*t+w or X+2*t<x+61<X+2*t+w) and s):
                game_over(hard)
        if y<bub_y:
            #print("jghjgdf")
            if x<bub_x<x+w and f1==0:
                point+=2
                f1+=1
                d1=0
            if x<bub_x-70<x+w and f2==0:
                point+=2
                f2+=1
                d2=0
            if x<bub_x+140<x+w and f3==0:
                point+=2
                f3+=1
                d3=0
            if x<bub_x-90<x+w and f4==0:
                point+=2
                f4+=1
                d4=0
        pygame.display.update()
        clock.tick(60)
        c+=1
        if c>500 and c<570:
            if c%10==0:
                i+=1
            if h<=90 and w<=90:
                h+=1
                w+=1
home()