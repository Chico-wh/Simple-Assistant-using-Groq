from functions import *
import time
while True:
    # Reconhece e executa os comandos
    comandos = [FalaRecon()]
    comando(comandos[0])
    # Faz a reconhecimento de fala a cada 1 segundo e executa o comando correspondente
    time.sleep(1)
    limpar_tela()
    comandos.clear() 
