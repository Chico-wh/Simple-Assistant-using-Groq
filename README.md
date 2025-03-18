Este projeto é um assistente virtual que realiza diversas tarefas como reconhecimento de fala, interação com o usuário através de conversas, e notificações de compromissos.

## Funcionalidades

- **Reconhecimento de Fala**: Utiliza a biblioteca `speech_recognition` para captar e interpretar comandos de voz.
- **Conversação**: Usa a classe `Brain` para gerar respostas de conversação usando um modelo de linguagem.
- **Notificações de Compromissos**: Lê um arquivo CSV de compromissos e notifica o usuário quando um evento está próximo.


## Requisitos

- Python 3.x
- Bibliotecas: `speech_recognition`, `pyttsx3`, `opencv-python`, `plyer`, `requests`

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/projeto-assistente.git
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Execução

Para iniciar o assistente, execute o arquivo `main.py`:
```bash
python main.py
```

## Estrutura do Projeto

- `functions.py`: Contém funções para reconhecimento de fala e processamento de comandos.
- `Brain.py`: Define a classe `Brain` para lidar com interações de conversação.
- `agenda.csv`: Arquivo CSV utilizado para gerenciar compromissos.

## Contribuição

Sinta-se à vontade para contribuir com o projeto, enviando pull requests ou relatando issues.

## Licença

Este projeto está licenciado sob a licença MIT.
