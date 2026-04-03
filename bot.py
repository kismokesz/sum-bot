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

@bot.command(name="fidesz")
async def fidesz(ctx):
    osszeg = 0
    # Feldolgozza az egész csatornát
    async for message in ctx.channel.history(limit=None):
        # Regex: minden 1-4 jegyű számot talál
        talalatok = re.findall(r'\b\d{1,4}\b', message.content)
        # Összegzés
        osszeg += sum(int(n) for n in talalatok)
    
    await ctx.send(f"Összegük: {osszeg}")

@bot.event
async def on_ready():
    print(f'Bejelentkezve mint {bot.user}')

token = os.getenv("DISCORD_TOKEN")
bot.run(token)
