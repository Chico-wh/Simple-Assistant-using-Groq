# MIKU CHATbot
# Speech Recognition Assistant

Este projeto é um assistente virtual controlado por voz chamado Miku. O Miku pode executar várias tarefas baseadas em comandos de voz, como pesquisar na web, abrir sites, agendar compromissos e tocar música.

Funcionalidades
Reconhecimento de Fala: Utiliza a biblioteca speech_recognition para interpretar comandos de voz.

Síntese de Fala: Utiliza a biblioteca pyttsx3 para fornecer respostas audíveis.

Navegação na Web: Abre sites específicos com base nos comandos fornecidos.

Agendamento de Compromissos: Permite que o usuário agende eventos e recebe notificações quando o evento está próximo.

Notificações: Utiliza a biblioteca plyer para enviar notificações do sistema.

Animação Miku: Exibe uma arte ASCII da Miku no console.

Instalação
Para instalar as dependências necessárias, utilize o seguinte comando:

bash
pip install speechrecognition pyttsx3 webbrowser plyer threading requests
Como Usar
Execute o script principal:

bash
python miku_assistant.py
Siga as instruções de voz fornecidas no console para interagir com o assistente Miku.

Exemplos de Comandos
Pesquisar [termo]: Pesquisa o termo fornecido no Google.

Twitter: Abre o site do Twitter.

Notícias ou Globo: Abre o site de notícias Globo.

Agendar [evento]: Agenda um novo evento.

Melhor música: Toca uma música específica.

Triste ou Me anima: Toca uma música animada para levantar o seu humor.

Estrutura do Código
limpar_tela(): Limpa o console.

FalaRecon(): Função que reconhece a fala do usuário.

comando(comandos): Função que processa os comandos reconhecidos e executa as ações correspondentes.

Leragenda(): Função que verifica e notifica os eventos agendados.

PrintMiku(): Função que imprime a arte ASCII da Miku.

Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para fazer um fork do projeto e enviar pull requests.

Licença
Este projeto é licenciado sob os termos da licença MIT.
