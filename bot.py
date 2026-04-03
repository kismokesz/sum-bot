import os
import re
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True  # Kell, hogy olvashassa az üzeneteket

bot = commands.Bot(command_prefix="!", intents=intents)

# Ping parancs teszteléshez
@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

# Fidesz Berenc parancs
@bot.command(name="fidesz_berenc")
async def fidesz_berenc(ctx):
    # Lekérjük a csatorna összes üzenetét (max 1000)
    szamok = []
    async for msg in ctx.channel.history(limit=1000):
        # Keresés: minden számot kiválasztunk az üzenetből
        szamok += [int(n) for n in re.findall(r'\d+', msg.content)]
    
    if szamok:
        osszeg = sum(szamok)
        await ctx.send(f"A csatorna összes számának összege: {osszeg}")
    else:
        await ctx.send("❌ Nem találtam számokat a csatorna üzeneteiben!")

@bot.event
async def on_ready():
    print(f'Bejelentkezve mint {bot.user}')

# Token Railway environment variable-ból
token = os.getenv("DISCORD_TOKEN")
bot.run(token)
