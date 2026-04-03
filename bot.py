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

# Fidesz parancs
@bot.command(name="fidesz")
async def fidesz(ctx):
    szamok = []

    # Utolsó 1000 üzenet lekérése a csatornából
    async for message in ctx.channel.history(limit=1000):
        # Minden szám kinyerése az üzenetből
        talalatok = re.findall(r'\d+', message.content)
        # Csak 1-2 jegyű számokat vegye figyelembe
        szamok += [int(n) for n in talalatok if 1 <= len(n) <= 2]

    if szamok:
        osszeg = sum(szamok)
        # Az összes számot + végső összeget egy üzenetben küldjük
        await ctx.send(f"{' + '.join(map(str, szamok))}\nÖsszegük: {osszeg}")
    else:
        await ctx.send("❌ Nem találtam 1-2 jegyű számokat az utolsó 1000 üzenetben!")

# Ready event
@bot.event
async def on_ready():
    print(f'Bejelentkezve mint {bot.user}')

# Token Railway environment variable-ból
token = os.getenv("DISCORD_TOKEN")
bot.run(token)
