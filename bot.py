import os
import discord
from discord.ext import commands, tasks
import datetime

# pip install automatikusan (Temalix miatt)
os.system("pip install py-cord==2.3.2")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

CHANNEL_ID = 1490006128875147506

@bot.event
async def on_ready():
    print(f"Bejelentkezve mint {bot.user}")
    send_ping.start()

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

@bot.command()
async def testping(ctx):
    await ctx.send("Teszt ping működik ✅")

@tasks.loop(minutes=5)
async def send_ping():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        await channel.send(f"Ping: {now}")
    else:
        print("Nem találom a csatornát!")

# 🔐 IDE AZ ÚJ TOKEN
bot.run("ide ird")
