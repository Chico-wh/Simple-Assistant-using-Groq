from ChicO.functions import *

def main():
    while True:
        audio = speech_recognition.listen()
        requisicao = speech_recognition.comando(audio)
        limpar_tela()

main()