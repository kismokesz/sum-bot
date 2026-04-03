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
    # Ellenőrizzük, hogy reply üzenetre jött-e
    if ctx.message.reference:  # ha reply
        replied_message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        szamok = [int(n) for n in re.findall(r'\d+', replied_message.content)]
    else:
        # Ha nincs reply, akkor a parancs utáni szövegből keresünk számokat
        szamok = [int(n) for n in re.findall(r'\d+', ctx.message.content)]
        # Eltávolítjuk a parancs szövegét (pl. !fidesz_berenc)
        if szamok:
            szamok = szamok[1:]  # első szám a parancs száma lehet, eltávolítjuk

    if szamok:
        osszeg = sum(szamok)
        await ctx.send(f"A 'fidesz_berenc' alatti számok: {szamok}\nÖsszegük: {osszeg}")
    else:
        await ctx.send("❌ Nem találtam számokat a jegyben!")
