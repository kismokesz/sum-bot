import os
import re
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command(name="fidesz_berenc")
async def fidesz_berenc(ctx):
    # Ellenőrizzük, hogy van-e reply-elt üzenet
    if ctx.message.reference is None:
        await ctx.send("❌ Kérlek reply-elj az üzenetre, ami a számokat tartalmazza!")
        return
    
    # Lekérjük a reply-elt üzenetet
    try:
        replied_msg = await ctx.channel.fetch_message(ctx.message.reference.message_id)
    except:
        await ctx.send("❌ Nem sikerült lekérni az üzenetet!")
        return
    
    # Számok kiszedése
    talalatok = re.findall(r'\d+', replied_msg.content)
    szamok = [int(t) for t in talalatok]
    
    if szamok:
        osszeg = sum(szamok)
        await ctx.send(f"A reply-elt üzenetben lévő számok összege: {osszeg}")
    else:
        await ctx.send("❌ Nem találtam számokat a reply-elt üzenetben!")
