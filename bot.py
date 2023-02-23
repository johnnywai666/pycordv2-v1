import discord
from discord.ext import commands

#定義機器人(前綴與intent)
bot = commands.Bot(command_prefix="$",intents=discord.Intents.all())

@bot.command()
async def here(ctx):
    await ctx.send(F"{ctx.author}你好,你現在在{ctx.guild.name}的{ctx.channel.mention}")

bot.run("")