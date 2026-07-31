# Discord Reverse-Shell

This tool make a reverse shell using discord servers, the way it works is that theres 2 scripts, one is the client, one is the server, the server is the victim and whenever the client sends a message, this message gets send using your bot token, then the server reads the message and runs it as a command, really one of the easiest way to make a reverse shell

# Requirements

A working Working browser
A discord account
A discord server
A Discord bot
A linux based os


Running

`pip install discord`

`pip install colorama`

# Setup Guide
This guide will show you how to create a bot, how to make your server, and how to set evreything up, so no errors will haunt you.

If you dont have a discord bot, here's how to make one.
# Creating discord bot and copying token

Go to https://discord.com/developers/applications.

And click on Create new application.

<img width="1900" height="869" alt="useless2" src="https://github.com/user-attachments/assets/7516380b-a848-4357-9f2b-3ed788e4502d" />

After that, Go to the Bot tab, scroll down and copy thoes settings

<img width="1900" height="869" alt="uesless3" src="https://github.com/user-attachments/assets/9aeb596a-2b12-4d80-a1ed-7bae70f448ea" />

After you have done that, Scroll up on the bot tab and click Reset token

<img width="1922" height="900" alt="useless4" src="https://github.com/user-attachments/assets/074e313f-e8e5-47bb-9af3-306335d570e3" />

Then click copy

<img width="1897" height="891" alt="useless1" src="https://github.com/user-attachments/assets/3eefe390-345b-4bdd-a4f0-f2f80928eec8" />

After you have copied. inside the folder that you have downloaded server.py and cliet.py and the top should look like this

SERVER_ID = 

CHANNEL_ID = 

TOKEN = ""

Paste your token inside the double quotation marks

# Making the server.
here is how to correctly set up your server
(optional read) after you have made your server, you can customize it how ever you want, But we are only going to use 1 channel from the server so you can rename it however you want or customize it nicely

Ones your server is done. make sure you have develepor mode enabled. if you dont know how follow thoes images.
# Enabling develepor mode
Open settings
<img width="1922" height="954" alt="useless5" src="https://github.com/user-attachments/assets/1816428b-899c-4f0c-aff8-1292a8fbd0da" />

Scroll all the way down to developer and click on it
<img width="1922" height="954" alt="image (69)" src="https://github.com/user-attachments/assets/68bc1115-32d5-42c1-8204-7b6cb4965083" />

Then enable developer mode.

<img width="1922" height="954" alt="image (68)" src="https://github.com/user-attachments/assets/15fd2929-276e-4c9d-9e2f-b1d5e4a23cc8" />

# Copying Server ID, And Channel ID

Now lets copy the server id, and your channel id.

Right click on your server, then go down to copy server info, then go right and press copy server ID

<img width="1922" height="954" alt="image (70)" src="https://github.com/user-attachments/assets/80b8d89a-5d17-4d6f-868e-631c3ac3b86c" />

Then inside the server.py and client.py paste it inside the SERVER_ID = (your server ID)

After that inside your server, right click your channel and press copy channel ID on the bottom of the menu.

<img width="1922" height="954" alt="image (71)" src="https://github.com/user-attachments/assets/1eb75b0b-312b-41b2-ac17-91bfd1f8dffb" />

Then inside the server.py and the client.py paste in your channel id inside CHANNEL_ID = (Your channel ID)

# Done

Your now officaly done.

The server.py is who receives the commands, and the client.py is who sends the commands.

Thats it! thank you for using my tool.
