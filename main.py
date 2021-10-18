# Import a library of functions called 'pygame'
import pygame
from main_functions import *

# Initialize the game engine
pygame.init()

#call main routine
size = [1300, 600] # Define size of windows
ancho =  int(input("ancho de la ventana: "))
alto = int(input("alto de la venta: "))
size[0] = ancho
size[1] = alto
main2(size)