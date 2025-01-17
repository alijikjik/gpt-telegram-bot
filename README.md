# gpt-telegram-bot
A small model of gpt that can be connected to your personal bot in Telegram and used as a free but small assistant.
## 1. Installation
Ollama supports running on Windows, macOS, and Linux. You can install Ollama through this link (https://ollama.com/download). After successful installation, you can directly use Ollama script to call Phi-3 through a terminal window. You can see all the available libaries in Ollama. If you open this repository in a Codespace, it will already have Ollama installed.
## 2. run phi3 model
```bash

ollama run phi3:mini

```
> [!NOTE]
> The model will be downloaded first when you run it for the first time. Of course, you can also directly specify the downloaded Phi-3 model. We take WSL as an example to run the command. After the model is successfully downloaded, you can interact directly on the terminal.
## 3. Call the phi-3 API from Ollama (optional)

If you want to call the Phi-3 API generated by ollama, you can use this command in the terminal to start the Ollama server.

```bash

ollama serve

```

> [!NOTE]
> If running MacOS or Linux, please note that you may encounter the following error **"Error: listen tcp 127.0.0.1:11434: bind: address already in use"** You may get this error when calling running the command. You can either ignore that error, since it typically indicates the server is already running, or you can stop the and restart Ollama:

**macOS**

```bash

brew services restart ollama

```

**Linux**

```bash

sudo systemctl stop ollama

```
## 4. make a bot on telegram
use the link to make a bot on telegram : https://core.telegram.org/bots/tutorial
## 5. run the program
Do not forget to place your robot token in the "**.env file"** before running the program
> Install libraries
```bash

pip install -r requirements.txt

```
run the program 
```bash

python main.py

```
