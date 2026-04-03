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

# Fidesz Berenc parancs
@bot.command(name="fidesz_berenc")
async def fidesz_berenc(ctx):
    # Ellenőrizzük, hogy van-e reply
    if ctx.message.reference:  # Ha reply
        replied_message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        szamok = [int(n) for n in re.findall(r'\d+', replied_message.content)]
        if szamok:
            osszeg = sum(szamok)
            await ctx.send(f"A 'fidesz_berenc' alatti számok: {szamok}\nÖsszegük: {osszeg}")
        else:
            await ctx.send("❌ Nem találtam számokat a reply-elt üzenetben!")
    else:
        await ctx.send("❌ Kérlek reply-elj az üzenetre, ami a számokat tartalmazza!")

@bot.event
async def on_ready():
    print(f'Bejelentkezve mint {bot.user}')

# Token Railway environment variable-ból
token = os.getenv("DISCORD_TOKEN")
bot.run(token)
