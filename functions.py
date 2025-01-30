import speech_recognition as sr
import pyttsx3 as t
import webbrowser
import os

class SpeechRecognition:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = t.init()


    def listen(self):
        with sr.Microphone() as source:
            print("Diga algo:")
            audio = self.recognizer.listen(timeout= 100, source=source)
            if audio:
                try:
                    requisicao = self.recognizer.recognize_google(audio, language='pt-BR').lower()
                    print("Você disse: " + requisicao)
                    return requisicao.lower()
                except sr.UnknownValueError:
                    return None
                except sr.RequestError as e:
                    print("Erro ao solicitar resultados; {0}".format(e))
                    return None
            else:
                pass
    def comando(self, requisicao):
        if requisicao:
            if "abraçar" in requisicao:
                self.engine.say("Eu vou e abraçar pra sempre meu lindo sinta-se abraçado!")
                self.engine.runAndWait()
            elif 'desligar' in requisicao:
                self.engine.say("Indo dar um cochilinho, boa noite meu amor")
                self.engine.runAndWait()
                os.system('shutdown /s /t 0')
            elif 'pesquisar' in requisicao:
                termo_pesquisa = requisicao.split('pesquisar')[1].strip()
                url = f"https://www.youtube.com/results?search_query={termo_pesquisa}"
                webbrowser.open(url)
            elif 'horas' in requisicao:
                import datetime
                horario = datetime.datetime.now()
                self.engine.say(f"Agora são {horario.hour} horas e {horario.minute} minutos")
                self.engine.runAndWait()
            elif 'obrigado' or 'agradeço' in requisicao:
                self.engine.say("De nada meu amor!,estou aqui pra ajudar")
                self.engine.runAndWait()
            elif 'google' in requisicao:
                termo_pesquisa = requisicao.split('pesquisar')[1].strip()
                url = f"https://www.google.com/search?q={termo_pesquisa}"
                webbrowser.open(url)
            elif 'twitter' in requisicao:
                url = f"https://www.twitter.com/"
                webbrowser.open(url)
            elif 'noticias' in requisicao:
                import selenium 

                
            else:
                pass
# Exemplo de uso
speech_recognition = SpeechRecognition()
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
if __name__=='__main__':
    while True:
        audio = speech_recognition.listen()
        requisicao = speech_recognition.comando(audio)
        limpar_tela()
