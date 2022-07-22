from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

#janela
janela=Window(800, 600)
fundo=GameImage("fundo.jpg")
janela.set_title("Pong")

#bola
bola =  Sprite ("bola.png", 1)
bola.x = janela.width/2 - bola.width/2
bola.y = janela.height/2 - bola.height/2
bola_velox = 500
bola_veloy = 500
bola.set_position((janela.width/2) - (bola.width/2), (janela.height/2) - (bola.height/2))

#padE
padE = Sprite("pad.png",1)
padE.set_position(5, janela.height/2 - padE.height/2)
pad_velo = 500
teclado = Window.get_keyboard()

#padD
padD = Sprite("pad.png",1)
padD.set_position(janela.width - padD.width - 5, janela.height/2 - padD.height/2)
padD_velo = 6000
teclado2 = Window.get_keyboard()

#pontos
pontosD = 0
pontosE = 0

#fps
ultimo_framerate = janela.time_elapsed()
contador_frame = 0
framerate = 0

startgame = True
teclado3 = Window.get_keyboard()

while(True):

    bola.x += bola_velox * janela.delta_time()
    bola.y += bola_veloy * janela.delta_time()

    if(teclado.key_pressed("W")):
        if(padE.y >= 0):
            padE.y -= pad_velo*janela.delta_time()
    if (teclado.key_pressed("S")):
        if (padE.y <= janela.height - padE.height):
            padE.y += pad_velo * janela.delta_time()

    #IA
    if bola.y > padD.y:
        if(padD.y <= janela.height - padD.height):
            padD.y +=2
    if bola.y < padD.y:
        if(padD.y >= 0):
            padD.y -=2
    else:
        pass

    if bola.collided(padE):
        bola_velox *= -1
        bola.x = bola.x + bola.width / 2
    if bola.collided(padD):
        bola_velox *= -1
        bola.x = bola.x - bola.width / 2

    if bola.x > janela.width - bola.width:
        bola_velox = bola_veloy = 0
        bola.x = janela.width / 2 - bola.width/2
        bola.y = janela.height / 2 - bola.height/2
        startgame = False
        pontosE +=1

        padE.set_position(5, janela.height / 2 - padE.height / 2)
        padD.set_position(janela.width - 5 - padD.width, janela.height / 2 - padD.height / 2)
        bola.set_position(0, janela.height / 2 - bola.height / 2)

    if bola.x < 0:
        bola_velox = bola_veloy = 0
        bola.x = janela.width / 2 - bola.width/2
        bola.y = janela.height / 2 - bola.height/2
        startgame = False
        pontosD +=1

        padE.set_position(5, janela.height / 2 - padE.height / 2)
        bola.set_position(padD.x - bola.height, 260)
        padD.set_position(janela.width - 5 - padD.width, janela.height / 2 - padD.height / 2)

    if bola.y <= 0 or bola.y + bola.height >= janela.height:
        if bola.y <= 0:
            bola.y = 0
        else:
            bola.y = janela.height - bola.height
        bola_veloy *= -1

    tempo = janela.time_elapsed()
    if (tempo - ultimo_framerate > 1000):
        framerate = contador_frame
        contador_frame = 0
        ultimo_framerate = tempo

    fundo.draw()
    padE.draw()
    padD.draw()
    bola.draw()
    janela.draw_text(str(pontosE), 150, 0, size=50, color=(0, 0, 0), font_name="Arial", bold=True, italic=False)
    janela.draw_text(str(pontosD), janela.width - 180, 0, size=50, color=(0, 0, 0), font_name="Arial", bold=True, italic=False)
    janela.draw_text(str(framerate) + " FPS", 10, janela.height - 22, size=15, color=(255, 255, 255), bold=True)

    if teclado3.key_pressed('SPACE') and not startgame:
        startgame = True

        bola_velox = 500
        bola_veloy = 500

    janela.update()
    contador_frame +=1