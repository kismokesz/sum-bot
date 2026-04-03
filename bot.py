import os
import discord
from discord.ext import commands
import re

# Intents: üzenetek olvasásához kötelező
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Ping parancs teszteléshez
@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

# Sum parancs: az adott csatorna összes üzenetéből számokat keres és összeadja
@bot.command(name="sum")
async def sum_numbers(ctx):
    total_sum = 0
    # Limit: hány üzenetet nézzen vissza, pl. 100
    async for message in ctx.channel.history(limit=100):
        # Számok kinyerése minden üzenetből
        numbers = re.findall(r'\d+', message.content)
        numbers = [int(n) for n in numbers]
        if numbers:
            msg_sum = sum(numbers)
            total_sum += msg_sum
    await ctx.send(f"A csatorna összes számának összege: {total_sum}")

@bot.event
async def on_ready():
    print(f'Bejelentkezve mint {bot.user}')

# Token Railway environment variable-ból
token = os.getenv("DISCORD_TOKEN")
bot.run(token)
