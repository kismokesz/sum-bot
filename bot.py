import os
import re
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

@bot.command(name="fidesz_berenc")
async def fidesz_berenc(ctx):
    async for msg in ctx.channel.history(limit=100):  # az utolsó 100 üzenet
        # Külön számok keresése, szóköz vagy vessző figyelmen kívül hagyva
        talalatok = re.findall(r'\d+', msg.content)
        szamok = [int(t) for t in talalatok]
        
        if szamok:
            osszeg = sum(szamok)
            await ctx.send(f"Üzenet ID {msg.id} számainak összege: {osszeg}")
