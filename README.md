# Discord Reverse-Shell

This tool make a reverse shell using discord servers, the way it works is that theres 2 scripts, one is the client, one is the server, the server is the victim and whenever the client sends a message, this message gets send using your bot token, then the server reads the message and runs it as a command, really one of the easiest way to make a reverse shell

# Previews
<img width="1917" height="975" alt="image" src="https://github.com/user-attachments/assets/748a69d1-751b-419d-baf2-c59a3485788f" />
<img width="1917" height="975" alt="image" src="https://github.com/user-attachments/assets/c52a3f7d-cd89-48dd-a08d-864f608a7acc" />
<img width="1916" height="981" alt="image" src="https://github.com/user-attachments/assets/53c5a611-4b27-4e8c-ba89-ed29968dbda4" />

# Info
External commands are

`refresh` : refreshes the script.

`exit` : exits the code.

In case the script freezes. Dont close it
i have set a refresh every 20 seconds, so if
it freezes just wait 20 seconds and it will be back.

# Requirements
A discord account
A discord server
A Discord bot
A linux based OS


# Setting up the files
In the files by default in the start of the script it says

SERVER_ID = 
CHANNEL_ID = 
TOKEN = ""

Inside the server.py and client.py put
SERVER_ID = (Your server ID)
CHANNEL_ID = (Your Channel ID)
TOKEN = "(Paste your discord bot token.)"

And make sure you have invited your bot to your server.

# Run
`cd Reverse-Shell`

`pip install colorama`

`pip install discord`

`python client.py`
Then send the server.py to another device you would like to reverse shell.

# Done

Your now officaly done.

The server.py is who receives the commands, and the client.py is who sends the commands.

Thats it! thank you for using my tool.

# How dose it work?
the way it works is like this. when you run the client.py it types ping evrey 2 seconds using your discord bot. this is to check if theres a connection. when someone connects
using the server.py using your discord bot it sends pong. and if client.py sees that it sends pong its gonna connect, when you type a command it encodes it with base64 (for less risk of getting limited) and sends it, then the server.py reads what you have typed and runs it. and after it runs it sends the output with base64 encoded to the discord, and client.py decodes that message and prints it.

into your discord server

