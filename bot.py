import os
import re
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

@bot.command(name="fidesz_berenc")
async def fidesz_berenc(ctx):
    szamok = []
    async for msg in ctx.channel.history(limit=1000):
        # Keresés minden számra (szóköz vagy vessző lehet)
        talalatok = re.findall(r'\d[\d ,]*\d|\d', msg.content)
        for t in talalatok:
            # Vessző és szóköz eltávolítása
            szamok.append(int(t.replace(",", "").replace(" ", "")))
    
    if szamok:
        osszeg = sum(szamok)
        await ctx.send(f"A csatorna összes számának összege: {osszeg}")
    else:
        await ctx.send("❌ Nem találtam számokat a csatorna üzeneteiben!")

@bot.event
async def on_ready():
    print(f'Bejelentkezve mint {bot.user}')

token = os.getenv("DISCORD_TOKEN")
bot.run(token)
