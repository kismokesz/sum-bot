import os
import re
import discord
from discord.ext import commands

# Intents beállítása
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Ping parancs
@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

# Fidesz parancs: számolja az utolsó 1000 üzenet számait
@bot.command(name="fidesz")
async def fidesz(ctx):
    szamok = []

    # Utolsó 1000 üzenet lekérése a csatornából
    async for message in ctx.channel.history(limit=1000):
        # Kinyeri az 1-2 jegyű számokat az üzenetekből
        szamok += [int(n) for n in re.findall(r'\d{1,2}', message.content)]

    if szamok:
        osszeg = sum(szamok)
        # Összes szám + végső összeget egy üzenetben küldjük
        await ctx.send(f"{' + '.join(map(str, szamok))}\nÖsszegük: {osszeg}")
    else:
        await ctx.send("❌ Nem találtam rövid számokat az utolsó 1000 üzenetben!")

# Multiply parancs: két szám összeszorzása
@bot.command(name="multiply")
async def multiply(ctx, num1: int, num2: int):
    await ctx.send(f"{num1} x {num2} = {num1 * num2}")

# Ready event
@bot.event
async def on_ready():
    print(f'Bejelentkezve mint {bot.user}')

# Token Railway/Render environment variable-ból
token = os.getenv("DISCORD_TOKEN")
bot.run(token)
