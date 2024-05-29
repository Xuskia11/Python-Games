import pygame
from pygame.locals import *
import random


size = width, height = (1920,1080)
road_w = int(width/1.6)
roadmark_w = int(width/80)
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
speed = 3
points = pygame.time.get_ticks()
# test_font = pygame.font.Font("pixeltype.ttf", 50)



pygame.init()
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

pygame.display.update()



#my car code
car = pygame.image.load("images/car1.png")
car_loc = car.get_rect()
car_loc.center = right_lane, height*0.8


#my enemy car code
car2 = pygame.image.load("images/car.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height*0.2


counter = 0
while running:
    
    # test_text = test_font.render((f"Score: {str(points)} "), False,     "#00008B")
    score_surf = str(points)
    
    # score_rect = points.get_rect(center = (400,50))
    # screen.blit(test_text,score_rect)
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
          print("GAME OVER! YOU LOST!") 
          break



    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w/2),0])
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w/2),0])



    pygame.draw.rect(screen, (50, 50, 50),(width/2-road_w/2,0,road_w, height)) # black road and around yellow field
    pygame.draw.rect(screen,(248,248,0),(width/2 - roadmark_w/2, 0, roadmark_w, height)) # yellow line between road
    pygame.draw.rect(screen,(248,248,248),(width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height))
    pygame.draw.rect(screen,(248,248,248),(width/2 + road_w/2 - roadmark_w*2, 0, roadmark_w, height))
    


    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    pygame.display.update()




pygame.quit()