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
        # Keresés minden számra (szóköz vagy vessző lehet)
        talalatok = re.findall(r'\d[\d ,]*\d|\d', msg.content)
        szamok = []
        for t in talalatok:
            szamok.append(int(t.replace(",", "").replace(" ", "")))
        
        if szamok:
            osszeg = sum(szamok)
            await ctx.send(f"Üzenet ID {msg.id} számainak összege: {osszeg}")
