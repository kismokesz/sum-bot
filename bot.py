import os
import discord
from discord.ext import commands
import re

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def fidesz_berenc(ctx, limit: int = 50):
    """
    Összeszámolja az utolsó `limit` üzenetben található számokat
    és a végén egyetlen összegként adja vissza.
    """
    total_sum = 0
    
    async for message in ctx.channel.history(limit=limit):
        # Minden számot külön kezelünk, nem fűzünk össze
        numbers = [int(n) for n in re.findall(r'\d+', message.content)]
        total_sum += sum(numbers)
    
    await ctx.send(f"A csatorna utolsó {limit} üzenetében lévő számok összege: {total_sum}")

@bot.event
async def on_ready():
    print(f'Bejelentkezve mint {bot.user}')

token = os.getenv("DISCORD_TOKEN")
bot.run(token)
