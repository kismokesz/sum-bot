import os
import re
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Ping parancs teszteléshez
@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

# Fidesz Berenc parancs: a szövegből olvassa ki a számokat
@bot.command(name="fidesz_berenc")
async def fidesz_berenc(ctx):
    # Az üzenetben lévő számokat keressük regex-szel
    # Feltételezzük, hogy a számok a "jegy alatt" szövegben vannak
    jegy_szoveg = ""
    # Ha az üzenetnek van "reply"-je, akkor a reply tartalmát használjuk
    if ctx.message.reference:
        replied_message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        jegy_szoveg = replied_message.content
    else:
        jegy_szoveg = ctx.message.content

    # Számok kinyerése a szövegből
    szamok = [int(n) for n in re.findall(r'\d+', jegy_szoveg)]
    
    if szamok:
        osszeg = sum(szamok)
        await ctx.send(f"A 'fidesz_berenc' alatti számok: {szamok}\nÖsszegük: {osszeg}")
    else:
        await ctx.send("❌ Nem találtam számokat a jegyben!")

@bot.event
async def on_ready():
    print(f'Bejelentkezve mint {bot.user}')

# Token Railway environment variable-ból
token = os.getenv("DISCORD_TOKEN")
bot.run(token)
