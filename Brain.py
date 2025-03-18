from groq import Groq

class Brain:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def chat(self, messages):
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            audio = recognizer.listen(source, phrase_time_limit=100)
            try:
               comandos = recognizer.recognize_google(audio, language='pt-BR').lower()
            except sr.UnknownValueError:
               comandos = ''
            except sr.RequestError as e:
               comandos = ''
        messages[1]['content'] = comandos
        chat_completion = self.client.chat.completions.create(
            messages=messages,
            model="llama-3.3-70b-versatile",
        )
        return chat_completion.choices[0].message.content

# Criar uma instância da classe Brain
api_key = 'API-KEY'
brain = Brain(api_key)

# Definir a lista de mensagens
messages = [{'role': 'system', 'content': 'Você é um assistente útil.'},
            {'role': 'user', 'content': ''}]

# Loop para chamar o método chat
if __name__ == '__main__':
    while True:
        response = brain.chat(messages)
        print(response)
