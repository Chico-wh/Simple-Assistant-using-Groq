import speech_recognition as sr
import pyttsx3 as t
import webbrowser
import os
from plyer import notification
import threading
import requests
class Assistant:
    def limpar_tela():
        if os.name == 'nt':
         os.system('cls')
        else:
            os.system('clear')
    
    
    resposta = t.init()
    
    # Reconhecimento de Fala
    def FalaRecon():
        recognizer = sr.Recognizer()
    
        with sr.Microphone() as source:
            print("Diga algo pra Miku fazer:")
            audio = recognizer.listen(source, phrase_time_limit=100)
    
        try:
            comandos = recognizer.recognize_google(audio, language='pt-BR').lower()
            print("Você disse: " + comandos)
            return comandos.lower()
        except sr.UnknownValueError:
            print("Não entendi o que você disse.")
            return None
        except sr.RequestError as e:
            print("Erro ao solicitar resultados; {0}".format(e))
            return None
    
    
    def comando(comandos):
        if comandos is None:
            return
    
        if 'pesquisar' in comandos or 'google' in comandos:
            url = f"https://www.google.com/search?q={comandos}"
            webbrowser.open(url)
        elif 'twitter' in comandos:
            url = "https://www.twitter.com/"
            webbrowser.open(url)
            resposta.say('Abrindo o Twitter...')
            resposta.runAndWait()
        elif 'noticias' in comandos or 'globo' in comandos:
            url = "https://www.globo.com/"
            webbrowser.open(url)
            resposta.say('Abrindo o Globo...')
            resposta.runAndWait()
        elif 'não'in comandos or 'errado' in comandos:
            resposta.say('Desculpe, não conheço essa opção.')
            resposta.runAndWait()
        elif 'agendar' in comandos or 'marcar' in comandos:
            resposta.say('Me diga o nome do evento por favor...')
            resposta.runAndWait()
            nome = FalaRecon()
            resposta.say('Me diga a data do evento por favor...')
            resposta.runAndWait()
            data = FalaRecon()
            resposta.say('Me diga a hora do evento por favor...')
            resposta.runAndWait()
            hora = FalaRecon()
            with open('agenda.csv', 'a') as agenda:
                agenda.write(f'{nome},{data},{hora}\n')
                resposta.say('Agendamento criado com sucesso!')
                resposta.runAndWait()
        elif 'sair' in comandos or 'encerrar' in comandos:
            resposta.say('Até mais!')
            resposta.runAndWait()
            quit()
        elif 'melhor' in comandos and 'música' in comandos:
            url = 'https://www.youtube.com/watch?v=TXnbX3GaGVs&ab_channel=Sat%C3%A9liteFunk'
            webbrowser.open(url)
            resposta.say('Sente a vibe..')
            resposta.runAndWait()
        elif 'compromissos' in comandos:
            threading.Thread(target=Leragenda).start()
        elif 'triste' in comandos or 'me anima' in comandos:
            resposta.say('Eu sei exatamente oque fazer, RE-CE-BA a felicidade ')
            resposta.runAndWait()
            felicidade = "C:/Users/felip/Downloads/Hatsune Miku - Ievan Polkka.mp4"
            os.startfile(felicidade)
        else:
            resposta.say('Não sei fazer isso, mas posso te ajudar.')
            resposta.runAndWait()
    
    def Leragenda():
        import time
        while True:
            with open('agenda.csv') as agenda:
                for evento in agenda:
                    nome, data, hora = evento.strip().split(',')
                    hora_atual = time.strftime("%H:%M:%S")
                    if data == hora_atual:
                        notification.notify(title=f'{nome}', message=f'Nome: {nome}, Data: {data}, Hora: {hora}')
            time.sleep(60)
    def PrintMiku():
      print(  """⠀⠀⠀⠀⠀⢀⠤⠒⠒⠒⠒⠒⠠⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢀⡞⡽⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢯⢳⡀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢀⣔⣻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⠢⡀⠀⠀⠀⠀
    ⠀⠀⢀⣾⣿⣶⡆⠀⠀⢐⡄⠀⠀⠀⠀⠐⠳⡀⠀⢸⣇⣧⡐⠀⠀⠀⠀⠀⠀
    ⠀⢠⠏⠀⢹⣿⡇⠀⠀⠇⢀⢂⠀⠀⠀⡃⢀⠀⠘⣦⢸⡿⡟⠋⠁⡀⠀⠀⠀
    ⠀⡋⠀⠀⠀⢹⣷⡀⡸⠀⠻⠀⠈⠒⠤⠃⠿⠀⢀⠻⣼⡇⠀⠀⠀⠀⢂⠀⠀
    ⢀⠀⠀⠀⠀⠈⣿⠱⣿⣅⠀⠀⠸⣉⡹⠀⠀⢀⠞⡼⠀⣿⡀⠀⠀⠀⠀⠐⠀
    ⠀⠀⠀⠀⠀⠀⣿⠀⢣⠀⠍⢶⣦⠤⢤⣖⠾⠠⣀⠇⠀⢹⡇⠀⠀⠀⠀⠀⠡
    ⡁⠀⠀⠀⢀⡴⣏⣴⡑⣀⣴⠂⢸⠤⠼⡀⠱⡤⡨⢳⣦⣸⣷⠀⠀⠀⠀⠀⢡
    ⠅⠀⠀⣴⡟⢷⣾⣿⡷⠳⠃⢠⠃⠀⠀⢣⣀⠡⡙⣿⣿⣿⠛⣦⡀⠀⠀⠀⢰
    ⠂⠀⣼⡯⠃⠢⠽⠋⡴⠧⣀⡣⡀⠀⠀⢈⢄⣭⣇⠘⠿⠕⠥⠜⠻⠦⣀⠀⡇
    ⠀⠉⠁⠀⠀⠀⡊⠉⢙⣿⡾⡶⠾⠶⣾⢕⢿⠟⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠉
    ⠀⠀⠀⠀⠀⠀⠐⢀⠼⠃⠀⠉⠉⠀⠂⠀⠈⠣⠄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀
          ♡⠀miku miku oo ee oo ♡⠀""")
if __name__ == '__main__':
    import time
    while True:
        #preciso falar mais?????MIKUUUUU
        PrintMiku()
        # Reconhece e executa os comandos
        comandos = [FalaRecon()]
        comando(comandos[0])
        # Faz a reconhecimento de fala a cada 1 segundo e executa o comando correspondente
        time.sleep(1)
        limpar_tela()
        comandos.clear() 
        
