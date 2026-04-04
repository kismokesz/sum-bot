import os
import re
import discord
from discord.ext import commands
from flask import Flask
from threading import Thread
import datetime

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

    async for message in ctx.channel.history(limit=1000):
        talalatok = re.findall(r'\d+', message.content)
        szamok += [int(n) for n in talalatok if 1 <= len(n) <= 2]

    if szamok:
        osszeg = sum(szamok)
        await ctx.send(f"{' + '.join(map(str, szamok))}\nÖsszegük: {osszeg}")
    else:
        await ctx.send("❌ Nem találtam 1-2 jegyű számokat az utolsó 1000 üzenetben!")

# Szorzás parancs
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

# Ping log lista
ping_log = []

@app.route('/')
def home():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Ping hozzáadása a listához
    ping_log.append(now)
    
    # Csak az utolsó 10 pinget tartjuk
    if len(ping_log) > 10:
        ping_log.pop(0)
    
    # Szép táblázat a konzolba
    print("\n┌─────────────── UptimeRobot Ping Log ────────────────┐")
    for i, t in enumerate(ping_log, 1):
        print(f"│ {i:2}. {t} │")
    print("└─────────────────────────────────────────────────────┘\n")
    
    return f"Bot is alive! Last ping: {now}"

def run():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run).start()

# ---------- Bot indítása ----------
token = os.getenv("DISCORD_TOKEN")
bot.run(token)
