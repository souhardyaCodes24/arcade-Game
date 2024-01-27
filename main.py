import pygame
pygame.init()
import random
pygame.font.init()
import sys
pygame.mixer.init()

import asyncio

credit_font= pygame.font.SysFont("comicsans",19)
credit_colour="magenta"

# GAME SOUND
sound=pygame.mixer.Sound("music.mp3")


#CHARACTER IMAGE
char=pygame.image.load("pic1.png")
char1=pygame.transform.scale(char,(64,120))

bg=pygame.image.load("bg.jpg")
bg_rect=bg.get_rect(topleft=(0,0))


apple=pygame.image.load("a1.png")
apple1=pygame.transform.scale(apple,(31,39))


# MAKING THE FONT
SOCRE_FONT= pygame.font.SysFont("comicsans",20,"bold")
GAME_FONT=pygame.font.SysFont("comicsans",35,"bold")



# COLOUR SCHEME OF THE GAME

screen_colour="black"
player_colour="red"
block_color="white"
game_over_colour="black"
score_colour="black"
high_score_colour="black"

# MAKING WINDOW

HEIGHT , WIDTH = 600,900
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SAVE ISSAC NEWTON")




# MAKING THE PLAYER  
player_spawn_x=450
player_spawn_y=480
        
player_height=20
player_width=50

player=pygame.Surface((player_width,player_height))
player.fill(player_colour)
player_1=player.get_rect(topleft=[player_spawn_x,player_spawn_y])


# CLOCK

c=pygame.time.Clock()

# HANDLING THE PLAYER MOVEMENTS
velocity=6

def handle_movement(player,key):
    if key[pygame.K_LEFT] and player.x> 10: # GOING LEFT COMMAND
            player.x=player.x-velocity
    if key[pygame.K_RIGHT] and player.x < WIDTH-player_width: # GOING RIGHT COMMAND
            player.x=player.x+velocity
    if key[pygame.K_UP] and player.y >10 : # GOING UP COMMAND
            player.y=player.y-velocity
    if key[pygame.K_DOWN] and player.y < HEIGHT-20 : # GOING DOWN COMMAND
            player.y=player.y+velocity




    
# MAKING THE BLOCKS
blocks_list=[]

block_width=20
block_height=40

block_speed=7




def move_block():
    for block in blocks_list:
        block.y=block.y + block_speed
    
def draw_blocks(blocks_list):
    for block in blocks_list:
        screen.blit(apple1,(block.x,block.y))


def make_blocks():
    pass
    
# CHECK CONDITION FOR COLLISIONS

def collision_check(blocks_list,player_1):
    for block in blocks_list:
        if player_1.colliderect(block):
            blocks_list.clear()
            return True
        else:
            pass
        

# LAST MESSAGE AFTER GAME ENDS
def game_over(text1,text2,HIGHEST_SCORE):
    #  TEXT AFTER GAME IS OVER
    text_1=GAME_FONT.render(text1,1,game_over_colour)
    screen.blit(text_1,(200,250))
    text_2=GAME_FONT.render(text2,1,game_over_colour)
    screen.blit(text_2,(200,400))

    
    pygame.display.update()
    
    pygame.time.delay(800)
    



# FUNCTION TO MAINTAIN HIGH SCORE
def high_score(HIGHEST_SCORE):
    pass

scores_list=[0]


# FUNCTIONS TO SPAWN BLOCK PERIODICALLY

def get_random_no_for_timer():
    t=random.randrange(0,1000,5)
    return t




# ------------MAIN GAME LOOP-----------------
async def main():
    PAUSE=False

    

    game_run=True
    
    # MAKING THE SCORING SYSTEM
    score=0

    FPS=25

    HIGHEST_SCORE=0

    var=0
    sound.play()
    

    

    while game_run:
        var+=10
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                 pygame.quit()
                 game_run=False
                 sys.exit()
               
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    PAUSE=True
                if event.key==pygame.K_p:
                    PAUSE=True
        while PAUSE:
             pygame.display.update()
             pygame.time.delay(5)

             text_1=GAME_FONT.render(f" GAME PAUSED !",1,game_over_colour)
             screen.blit(text_1,(200,250))
                
             for event in pygame.event.get():
                  if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_SPACE:
                            PAUSE=False
    
                
        
                
             
             

        screen.blit(bg,(bg_rect))
        
        
        screen.blit(char1,(player_1.x,player_1.y))
        #print(player_1.center)   # PLAYER COORDINATES



        key=pygame.key.get_pressed()
        handle_movement(player_1,key)

       

        
            
        # MAKING THE BLOCKS AT RANDOM POSITIONS

        t=get_random_no_for_timer()
        block_spawn_x=random.randrange(0,900,15)



        if t%7==0:
                    block=pygame.Rect(block_spawn_x,0,block_height,block_width)
                    blocks_list.append(block)



        draw_blocks(blocks_list)
        move_block()

        # SCORE UPDATE AND SHOWING ON SCREEN
        score_actual=SOCRE_FONT.render(f"SCORE : {int(score)}",1,score_colour)
        screen.blit(score_actual,(30,30))
        score=score+0.2

        
        

        
                  
            
            
            
        text1 = ""    # THE WAY ONE PLAYER WINS AND OTHER LOOSES

        

        if collision_check(blocks_list,player_1):
            text1 = f" GAME OVER !"
            text2=f"YOUR SCORE : {int(score)}"
            scores_list.append(int(score))


        if text1 != "":
            

            game_over(text1,text2,HIGHEST_SCORE)
            break
        HIGHEST_SCORE=max(scores_list)

        h=SOCRE_FONT.render(f"HIGH SCORE : {HIGHEST_SCORE}",1,high_score_colour)
        screen.blit(h,(30,50))

        credits=credit_font.render(f"Created by Souhardya Saha",1,credit_colour)
        screen.blit(credits,(170,10))

        if var<10000:
             score_actual=SOCRE_FONT.render(f"PRESS ARROW KEYS TO MOVE | SPACE BAR TO PAUSE",1,score_colour)
             screen.blit(score_actual,(250,50))
        


        
        

        pygame.display.update()
        await asyncio.sleep(0)
        
        c.tick(FPS)
        FPS=FPS+0.5
        if FPS>50:
            FPS=50
    main()


    


asyncio.run(main())

            