import pygame
import json

pygame.init()


width, height = 1000, 720

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PixAlrT")

white = (255, 255, 255)
black = (0, 0, 0)

verdeOpaco = (224, 40, 40)
verdeClaro = (235, 80, 80)
amarilloClaro = (246, 115, 115)
cafeClaro = (221, 22, 19)
cafeFuerte = (100, 220, 81)
amarilloFuerte = (77, 189, 59)
naranjaClaro = (56, 161, 39)


# Pixel Art
columnas = 50
filas = 48

celdaAncho = 15
celdaAlto = 15


# Paleta de colores
columnasColores = 3
filasColores = 3

celdaColoresAncho = 50
celdaColoresAlto = 50

botonAncho = 200
botonAlto = 40

botonX = 780

botonY = 500

def guardar():
    with open('readme.txt', 'a') as f:
        for i in range(filas):
            for j in range(columnas):
                colorGuardado = cuadriculaEstado[i][j]
                informacion = {'fila': i, 'columna': j, 'color': colorGuardado}
                json.dump(informacion, f)
                f.write("\n")
    print("Guardado")


botones = [
    {"text": "Guardar", "function": guardar}
]


cuadricula = pygame.Surface(((3*width/4), height))
cuadricula.fill(white)
pygame.draw.rect(cuadricula, black, cuadricula.get_rect(),0)

cuadriculaEstado = [[white for _ in range(columnas)] for _ in range(filas)]


cuadriculaColores = pygame.Surface((width/4, height))
cuadriculaColores.fill(white)
pygame.draw.rect(cuadriculaColores, white, cuadriculaColores.get_rect(),0)

cuadriculaEstadoColores = [[white for _ in range(columnasColores)] for _ in range(filasColores)]



cuadriculaEstadoColores[0][0] = black
cuadriculaEstadoColores[0][1] = white
cuadriculaEstadoColores[0][2] = verdeOpaco
cuadriculaEstadoColores[1][0] = verdeClaro
cuadriculaEstadoColores[1][1] = amarilloClaro
cuadriculaEstadoColores[1][2] = amarilloFuerte
cuadriculaEstadoColores[2][0] = naranjaClaro
cuadriculaEstadoColores[2][1] = cafeClaro
cuadriculaEstadoColores[2][2] = cafeFuerte

colorReal=(255,255,255)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            
            mouseX = pos[0]
            mouseY = pos[1]

            if (mouseX >= 3*width/4) and (mouseY <= 300):
                colorP =  screen.get_at(pos)

                colorReal = colorP[0], colorP[1], colorP[2]
                
                print(colorReal)

            if (mouseX <= 3*width/4):
                cuadriculaEstado[mouseY//celdaAncho][mouseX//celdaAlto] = colorReal

            if (mouseX >= 3*width/4) and (mouseY >= 300):
                if mouseX//botonAncho >= 3 and mouseY//botonAlto >= 11:
                    botones[0]["function"]()   


    screen.fill(white)
    screen.blit(cuadricula, (0, 0))
    screen.blit(cuadriculaColores,(800,0))

    boton = pygame.Rect(botonX, botonY + botonAlto , botonAncho, botonAlto)
    pygame.draw.rect(screen, (55, 148, 65), boton)
    
    for fila in range(filas):
        for columna in range(columnas):
            cell_x = columna * celdaAncho
            cell_y = fila * celdaAlto
            pygame.draw.rect(cuadricula, cuadriculaEstado[fila][columna], (cell_x, cell_y, celdaAncho, celdaAlto), 0)
            pygame.draw.rect(cuadricula, black, (cell_x, cell_y, celdaAncho, celdaAlto), 1)

    for filaColores in range(filasColores):
        for columnaColores in range(columnasColores):
            celdaColoresX = columnaColores * celdaColoresAncho
            celdaColoresY = filaColores * celdaColoresAlto
            pygame.draw.rect(cuadriculaColores, cuadriculaEstadoColores[filaColores][columnaColores], (celdaColoresX, celdaColoresY, celdaColoresAncho, celdaColoresAlto), 0)
            pygame.draw.rect(cuadriculaColores, black, (celdaColoresX, celdaColoresY, celdaColoresAncho, celdaColoresAlto), 1)


    pygame.display.flip()


pygame.quit()


