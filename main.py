
import pygame

sc=pygame.display.set_mode((900,700))
pygame.display.set_caption("fake mario")




c=pygame.time.Clock()

#char=pygame.image.load("NEW GAME (UNDER CONSTRUCTION)\c2.png").convert_alpha()


# FLOOR SETUP
floor=580
wall_left=10
wall_Right=810


# gravity
gravity=3
jump_height=30
player_move=19


# MAKING THE BLOCKS
BLOCKS=[]
block_spawn_x=200

block_width=40
block_height=100
block_spawn_y=450

block_color="green"

def draw_blocks(block_list):
    
    pygame.draw.rect(sc,block_color,block_list)



def main():
    player_y=floor
    player_x=50
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
                break

            # jump
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    player_y-=jump_height
                if event.key==pygame.K_RIGHT:
                    player_x+=player_move
                if event.key==pygame.K_LEFT:
                    player_x-=player_move
                
        sc.fill("black")

        # CONTROLING GRAVITY
        if player_y<=floor:
            player_y+=gravity
        if player_y>floor:
            player_y=floor
        # keys=pygame.key.get_pressed()
        # if keys[pygame.K_LEFT] and player_x>=wall_left: # GOING LEFT COMMAND
        #     player_x-=player_move
        # if keys[pygame.K_RIGHT] and player_x<=wall_Right: # GOING RIGHT COMMAND
        #     player_x+=player_move
        
        # MAKING BLOCKS
        block=pygame.Rect(block_spawn_x,block_spawn_y,block_height,block_width)

        draw_blocks(block)

        

        

        #sc.blit(char,(player_x,player_y))

        pygame.display.update()
        c.tick(60)



main()

