import os
import re
import discord
from discord.ext import commands, tasks
import datetime

# ---------- Discord bot ----------
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Discord csatorna ID
PING_CHANNEL_ID = 1490006128875147506

# Bot indítási időpont
bot_start_time = datetime.datetime.now()

# ---------- Discord parancsok ----------
@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

@bot.command()
async def testping(ctx):
    await ctx.send("Ez egy teszt ping üzenet ✅")

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

# ---------- Ping küldése 5 percenként ----------
@tasks.loop(minutes=5)
async def send_ping():
    channel = bot.get_channel(PING_CHANNEL_ID)
    if channel is None:
        print("[ERROR] Nem találom a csatornát! Ellenőrizd a PING_CHANNEL_ID-t!")
        return
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    uptime = datetime.datetime.now() - bot_start_time
    hours, remainder = divmod(int(uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    await channel.send(
        f"✅ Ping at `{timestamp}` | Bot uptime: {hours}h {minutes}m {seconds}s"
    )

@bot.event
async def on_ready():
    print(f'Bejelentkezve mint {bot.user}')
    send_ping.start()  # indítjuk a folyamatos ping taskot

# ---------- Bot indítása ----------
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    print("[ERROR] DISCORD_TOKEN nincs beállítva!")
else:
    bot.run(TOKEN)
