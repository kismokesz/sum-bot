import os
import discord
from discord.ext import commands
import re

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

@bot.command(name="fidesz_berenc")
async def fidesz_berenc(ctx, limit: int = 50):
    """Összeszámolja az utolsó `limit` üzenetben található számokat a csatornában."""
    total_sum = 0
    async for message in ctx.channel.history(limit=limit):
        # Az üzenetben lévő összes számot külön int-ként kezeljük
        numbers = re.findall(r'\d+', message.content)
        numbers = [int(n) for n in numbers]  # minden számot int-re alakít
        if numbers:
            message_sum = sum(numbers)  # az üzenetben lévő számok összege
            total_sum += message_sum    # hozzáadjuk a csatorna összegéhez
    await ctx.send(f"A csatorna utolsó {limit} üzenetében lévő számok összege: {total_sum}")

@bot.event
async def on_ready():
    print(f'Bejelentkezve mint {bot.user}')

token = os.getenv("DISCORD_TOKEN")
bot.run(token)
