import os
import discord
from discord.ext import commands
import re

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def fidesz_berenc(ctx, limit: int = 50):
    total_sum = 0
    numbers_found = []

    async for message in ctx.channel.history(limit=limit):
        numbers = [int(n) for n in re.findall(r'\d+', message.content)]
        if numbers:
            numbers_found.extend(numbers)
            total_sum += sum(numbers)

    if numbers_found:
        expression = " + ".join(str(n) for n in numbers_found)
        await ctx.send(f"{expression}\nÖsszegük: {total_sum}")
    else:
        await ctx.send("❌ Nem találtam számokat az utolsó üzenetekben!")

@bot.event
async def on_ready():
    print(f'Bejelentkezve mint {bot.user}')

token = os.getenv("DISCORD_TOKEN")
bot.run(token)
