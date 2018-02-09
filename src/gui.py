#modified from https://stackoverflow.com/questions/597369/how-to-create-ms-paint-clone-with-python-and-pygame
import pygame, random
import read_digit

screen = pygame.display.set_mode((220, 220))
pygame.display.set_caption('Handwriting Recognition')

LEFT = 1
RIGHT = 3
RADIUS = 6

draw_on = False
last_pos = (0, 0)


def roundline(srf, color, start, end, RADIUS=1):
    dx = end[0]-start[0]
    dy = end[1]-start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start[0]+float(i)/distance*dx)
        y = int(start[1]+float(i)/distance*dy)
        pygame.display.update(pygame.draw.circle(srf, color, (x, y), RADIUS))

try:
    while True:
        e = pygame.event.wait()
        if e.type == pygame.QUIT:
            raise StopIteration
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == LEFT:
            #draw on the window
            color = (255, 255, 255)
            pygame.draw.circle(screen, color, e.pos, RADIUS)
            draw_on = True
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == RIGHT:
            #clear the window
            draw_on = False
            pygame.display.update(screen.fill((0, 0, 0)))
        if e.type == pygame.MOUSEBUTTONUP and e.button == LEFT:
            #save the drawing as a number
            draw_on = False
            pygame.image.save(screen, "./data/number.jpg")
            read_digit.read()
        if e.type == pygame.MOUSEMOTION:
            if draw_on:
                pygame.display.update(pygame.draw.circle(screen, color, e.pos, RADIUS))
                roundline(screen, color, e.pos, last_pos, RADIUS)
            last_pos = e.pos

except StopIteration:
    pass

pygame.quit()
