import os
import re
import discord
from discord.ext import commands

# Intents beállítása
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Ping parancs teszteléshez
@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

# Fidesz Berenc parancs
@bot.command(name="fidesz_berenc")
async def fidesz_berenc(ctx):
    szamok = []

    # Utolsó 200 üzenet lekérése a csatornából
    async for message in ctx.channel.history(limit=200):
        # Csak a rövid számokat (1-2 jegyű) gyűjtjük
        talalatok = re.findall(r'\b\d{1,2}\b', message.content)
        szamok.extend(int(n) for n in talalatok)

    if szamok:
        osszeg = sum(szamok)
        # Egy sorba írjuk ki a számokat, majd a végén az összeget
        szamok_str = " + ".join(str(n) for n in szamok)
        await ctx.send(f"{szamok_str} = {osszeg}")
    else:
        await ctx.send("❌ Nem találtam rövid számokat az utolsó 200 üzenetben!")

# Ready event
@bot.event
async def on_ready():
    print(f'Bejelentkezve mint {bot.user}')

# Token Railway environment variable-ból
token = os.getenv("DISCORD_TOKEN")
bot.run(token)
