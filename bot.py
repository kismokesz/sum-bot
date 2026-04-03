import os
import re
import discord
from discord.ext import commands

# Intents beállítása
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

@bot.command(name="fidesz")
async def fidesz(ctx):
    osszeg = 0
    async for message in ctx.channel.history(limit=None):
        talalatok = re.findall(r'\d+', message.content)
        osszeg += sum(int(n) for n in talalatok)

    await ctx.send(f"Összegük: {osszeg}")

@bot.event
async def on_ready():
    print(f'Bejelentkezve mint {bot.user}')

# Token Railway environment variable-ból
token = os.getenv("DISCORD_TOKEN")
if not token:
    print("❌ Hiba: A DISCORD_TOKEN nincs beállítva!")
else:
    bot.run(token)
