import os
import re
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

@bot.command(name="fidesz_berenc")
async def fidesz_berenc(ctx):
    osszeg = 0

    # Egész csatorna üzeneteinek feldolgozása
    async for message in ctx.channel.history(limit=None):
        # Csak 1-2 jegyű számokat veszünk figyelembe
        talalatok = re.findall(r'\b\d{1,2}\b', message.content)
        osszeg += sum(int(n) for n in talalatok)

    await ctx.send(f"Összegük: {osszeg}")

@bot.event
async def on_ready():
    print(f'Bejelentkezve mint {bot.user}')

token = os.getenv("DISCORD_TOKEN")
bot.run(token)
