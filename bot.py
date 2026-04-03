import os
import discord
from discord.ext import commands
import re
from collections import defaultdict

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

@bot.command(name="fidesz_berenc")
async def fidesz_berenc(ctx, limit: int = 50):
    """
    Összeszámolja az utolsó `limit` üzenetben található számokat felhasználónként.
    """
    user_sums = defaultdict(int)
    
    async for message in ctx.channel.history(limit=limit):
        numbers = [int(n) for n in re.findall(r'\d+', message.content)]
        if numbers:
            user_sums[message.author.display_name] += sum(numbers)
    
    if user_sums:
        msg_lines = [f"{user}: {total}" for user, total in user_sums.items()]
        final_msg = "**Számok összege felhasználónként az utolsó üzenetekből:**\n" + "\n".join(msg_lines)
        await ctx.send(final_msg)
    else:
        await ctx.send("❌ Nem találtam számokat az utolsó üzenetekben!")

@bot.event
async def on_ready():
    print(f'Bejelentkezve mint {bot.user}')

token = os.getenv("DISCORD_TOKEN")
bot.run(token)
