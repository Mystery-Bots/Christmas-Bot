from discord.ext import commands
import random
from config import *

bot = commands.Bot(command_prefix="+", description="The bot for the Christmas event in the Craft of Clans Discord")

@bot.event
async def on_ready():
    print("Loaded")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        m , s = divmod(error.retry_after, 60)
        h, m = divmod(m, 60)
        if m == 0 and h == 0:
            await ctx.send(f"You have already collected gifts in the last 24 hours. Try again in `{round(s)} seconds`")
        elif h == 0:
            await ctx.send(f"You have already collected gifts in the last 24 hours. Try again in `{round(m)} minutes {round(s)} seconds`")
        else:
            await ctx.send(f"You have already collected gifts in the last 24 hours. Try again in `{round(h)} hours {round(m)} minutes`")


@bot.command()
#@commands.cooldown(1,86400.0,type=commands.BucketType.member)
@commands.cooldown(1, 12, type=commands.BucketType.member)
async def check(ctx):
    user = ctx.author
    gifts = random.randint(5,10)
    await ctx.send(f"{user.mention}, You collected {gifts} :gift: from under the tree!")


@bot.command()
async def userinfo(ctx):
    await ctx.send("not started")

bot.run(token)
