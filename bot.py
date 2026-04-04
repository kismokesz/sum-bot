import os
import re
import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

# ==== WEB SERVER ====
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot él!"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# ==== DISCORD BOT ====
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

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
        await ctx.send("❌ Nem találtam számokat!")

@bot.command(name="szoroz")
async def szoroz(ctx, *szamok: int):
    if not szamok:
        await ctx.send("❌ Adj meg számokat!")
        return

    eredmeny = 1
    for szam in szamok:
        eredmeny *= szam

    await ctx.send(f"{' * '.join(map(str, szamok))} = {eredmeny}")

@bot.event
async def on_ready():
    print(f'Bejelentkezve mint {bot.user}')

# ==== INDÍTÁS ====
token = os.getenv("DISCORD_TOKEN")

if not token:
    print("❌ NINCS TOKEN BEÁLLÍTVA!")
else:
    keep_alive()
    bot.run(token)
