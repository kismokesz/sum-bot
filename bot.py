import os
import re
import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

# ---------- Discord bot beállítás ----------
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
        await ctx.send(f"{' + '.join(map(str, szamok))}\nÖsszegük: {osszeg}")
    else:
        await ctx.send("❌ Nem találtam 1-2 jegyű számokat az utolsó 1000 üzenetben!")

# Szorzás parancs - tetszőleges számú szám
@bot.command(name="szoroz")
async def szoroz(ctx, *szamok: int):
    if not szamok:
        await ctx.send("❌ Adj meg legalább egy számot a szorzáshoz!")
        return

    eredmeny = 1
    for szam in szamok:
        eredmeny *= szam

    await ctx.send(f"{' * '.join(map(str, szamok))} = {eredmeny}")

# Ready event
@bot.event
async def on_ready():
    print(f'Bejelentkezve mint {bot.user}')

# ---------- Flask web server az UptimeRobot pinghez ----------
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

# Web szerver külön szálon, hogy a bot fusson tovább
Thread(target=run).start()

# ---------- Bot indítása ----------
token = os.getenv("DISCORD_TOKEN")
bot.run(token)
