import pygame
import sys
import json


class Vetana():
    

    def __init__(self, nombre):
        pygame.init()

        white = (255, 255, 255)
        black = (0, 0, 0)
        

        width, height = 3*1000/4, 720

        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Hola")

        # Pixel Art
        columnas = 50
        filas = 60

        celdaAncho = 15
        celdaAlto = 15


        cuadricula = pygame.Surface((width, height))
        cuadricula.fill(white)
        pygame.draw.rect(cuadricula, black, cuadricula.get_rect(),0)

        self.cuadriculaEstado = [[(white) for _ in range(columnas)] for _ in range(filas)]


        def cargar():
            global cuadriculaEstado
            with open(nombre, 'r') as f:
                for line in f:
                    informacion = json.loads(line)
                    fila = informacion['fila']
                    columna = informacion['columna']
                    colorGuardado = informacion['color']
                    self.cuadriculaEstado[fila][columna] = colorGuardado
            print("Cargado")

        cargar()

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    

            screen.fill(white)
            screen.blit(cuadricula, (0, 0))

            
            for fila in range(filas):
                for columna in range(columnas):
                    cell_x = columna * celdaAncho
                    cell_y = fila * celdaAlto
                    pygame.draw.rect(cuadricula, self.cuadriculaEstado[fila][columna], (cell_x, cell_y, celdaAncho, celdaAlto), 0)
                    pygame.draw.rect(cuadricula, black, (cell_x, cell_y, celdaAncho, celdaAlto), 1)

            pygame.display.flip()


        pygame.quit()
        sys.exit()

