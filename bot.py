import os
import re
import discord
from discord.ext import commands
from flask import Flask
from threading import Thread
import datetime
import asyncio

# ---------- Discord bot ----------
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Ide a Discord csatorna ID-je, ahová a ping logot küldeni akarod
PING_CHANNEL_ID = 123456789012345678  # <--- cseréld a saját csatorna ID-re

# ---------- Discord parancsok ----------
@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

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

@bot.command(name="szoroz")
async def szoroz(ctx, *szamok: int):
    if not szamok:
        await ctx.send("❌ Adj meg legalább egy számot a szorzáshoz!")
        return
    eredmeny = 1
    for szam in szamok:
        eredmeny *= szam
    await ctx.send(f"{' * '.join(map(str, szamok))} = {eredmeny}")

@bot.event
async def on_ready():
    print(f'Bejelentkezve mint {bot.user}')

# ---------- Flask szerver az Uptimerobot pinghez ----------
app = Flask('')

@app.route('/')
def home():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Aszinkron küldés a Discord csatornára
    asyncio.run_coroutine_threadsafe(send_ping_to_discord(now), bot.loop)
    return f"Bot is alive! Last ping: {now}"

async def send_ping_to_discord(timestamp):
    channel = bot.get_channel(PING_CHANNEL_ID)
    if channel:
        await channel.send(f"Ping received at {timestamp} 🟢")

def run_flask():
    port = int(os.environ.get("PORT", 8080))  # Replit PORT változó
    print(f"Flask keep-alive server running on port {port}")
    app.run(host='0.0.0.0', port=port)

# Flask külön szálon
Thread(target=run_flask).start()

# ---------- Bot indítása ----------
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    print("[ERROR] DISCORD_TOKEN nincs beállítva!")
else:
    bot.run(TOKEN)
