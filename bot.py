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
        # Minden szám kinyerése az üzenetből
        talalatok = re.findall(r'\d+', message.content)
        szamok.extend(int(n) for n in talalatok)  # Minden szám külön kerül a listába

    if szamok:
        szamok_str = " + ".join(str(n) for n in szamok)
        vegosszeg = sum(szamok)
        await ctx.send(f"{szamok_str} = {vegosszeg}")
    else:
        await ctx.send("❌ Nem találtam számokat az utolsó 200 üzenetben!")

@bot.event
async def on_ready():
    print(f'Bejelentkezve mint {bot.user}')

# Token Railway environment variable-ból
token = os.getenv("DISCORD_TOKEN")
bot.run(token)
