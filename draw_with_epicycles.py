import pygame
from rotating_vec import rotvec, epicycles
from vector_class import vector
from convert_image_to_points import get_points
import numpy as np
import time
import sys

def run_draw():
    pygame.init()
    screen_value = 1000
    screen = pygame.display.set_mode([screen_value,screen_value])
    run = True
    my_centre = vector(500,100)
    if len(sys.argv) >1:
        shape = get_points(sys.argv[1])
    else:
        shape = get_points("a.png")
    dft_coeffs = [np.fft.fft(item) for item in shape ]
    circles = epicycles(my_centre,screen,dft_coeffs)
    circles.assign_params()
    while (run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill((255,255,255))
        circles.draw_them_all()
        pygame.display.flip()
    pygame.quit()


run_draw()
