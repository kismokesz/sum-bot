import os
import discord
from discord.ext import commands, tasks
import datetime

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

PING_CHANNEL_ID = 1490006128875147506
bot_start_time = datetime.datetime.now()

@bot.event
async def on_ready():
    print(f'Bejelentkezve mint {bot.user}')
    send_ping.start()  # indítjuk a folyamatos ping taskot

@tasks.loop(minutes=5)
async def send_ping():
    channel = bot.get_channel(PING_CHANNEL_ID)
    if channel is None:
        print("[ERROR] Nem találom a csatornát!")
        return
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    uptime = datetime.datetime.now() - bot_start_time
    hours, remainder = divmod(int(uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    await channel.send(f"✅ Ping at `{timestamp}` | Uptime: {hours}h {minutes}m {seconds}s")

# Teszt parancs
@bot.command()
async def testping(ctx):
    await ctx.send("Ez egy teszt ping üzenet ✅")

# Token betöltés
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
