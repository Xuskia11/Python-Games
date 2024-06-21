import pygame
from pygame.locals import *
import random
import asyncio

pygame.init()

sets = set([0])
def display_score():
    current_time = pygame.time.get_ticks()//1000 - start_time
    sets.add(current_time)
    score_surf = test_font.render("Score: " +str(current_time),False,"white")
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    # return [current_time,score_surf]


size = width, height = (800,750)
road_w = int(width/1.6)
roadmark_w = int(width/80)
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
speed = 3
game_active = True
clock = pygame.time.Clock()
test_font = pygame.font.Font("images/Pixeltype.ttf", 50)
start_time = 0



running = True
screen = pygame.display.set_mode((size))
pygame.display.set_caption("atuka's super car game")
screen.fill((248,248,0))


pygame.draw.rect(screen, (50, 50, 50),(width/2-road_w/2,0,road_w, height)) # black road and around yellow field
pygame.draw.rect(screen,(248,248,0),(width/2 - roadmark_w/2, 0, roadmark_w, height)) # yellow line between road
pygame.draw.rect(screen,(248,248,248),(width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height))
pygame.draw.rect(screen,(248,248,248),(width/2 + road_w/2 - roadmark_w*2, 0, roadmark_w, height))
Dead_line1 = width/2 - road_w/2 + roadmark_w*2
Dead_line2 = width/2 + road_w/2 - roadmark_w*2



#my car code
car = pygame.image.load("images/car1.png").convert_alpha()
car_loc = car.get_rect()
car_loc.center = right_lane, height*0.8


#my enemy car code
car2 = pygame.image.load("images/car.png").convert_alpha()
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height*0.2
counter = 0

async def main():
    global car2
    global car2_loc
    global car
    global car_loc
    global counter
    global Dead_line1
    global Dead_line2
    global running
    global points
    global speed
    global road_w
    global roadmark_w
    global right_lane
    global left_lane
    global game_active
    global score_text
    global score_rect
    global clock
    global start_time
    
    
    
    
    

    while running:
        



        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key in [K_a, K_LEFT]:
                    if car_loc.center[0] <= 500 and car_loc.center[0] >= 170:
                        pass
                    else:   
                        car_loc = car_loc.move([-int(road_w/2),0])
                if event.key in [K_d, K_RIGHT]:
                    if car_loc.center[0] <= 630 and car_loc.center[0] >= 500:
                        pass
                    else:   
                        car_loc = car_loc.move([int(road_w/2),0])
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not game_active:
                    game_active = True
                    start_time  = pygame.time.get_ticks()//1000
        if game_active:
            counter += 1
            if counter == 1000:
                speed += 0.25
                counter = 0

                #animate enemy car
            car2_loc[1] += speed
            if car2_loc[1]> height:
                if random.randint(0,1) == 0:
                    car2_loc.center = right_lane, -200
                else:
                    car2_loc.center = left_lane, -200
                #end game
            if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] -230:
                game_active = False
            pygame.draw.rect(screen, (50, 50, 50),(width/2-road_w/2,0,road_w, height)) # black road and around yellow field
            pygame.draw.rect(screen,(248,248,0),(width/2 - roadmark_w/2, 0, roadmark_w, height)) # yellow line between road
            pygame.draw.rect(screen,(248,248,248),(width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height))
            pygame.draw.rect(screen,(248,248,248),(width/2 + road_w/2 - roadmark_w*2, 0, roadmark_w, height))

            
            

            
            screen.blit(car, car_loc)
            screen.blit(car2, car2_loc)
            display_score()
        else:
            test_text = test_font.render(("Press space to restart..."), False, 	"white")
            screen.blit(test_text,(220,200))
            car2_loc.center = 1000, -200
            speed = 3
        clock.tick(200)
        pygame.display.update()
        await asyncio.sleep(0)




    pygame.quit()

asyncio.run(main())