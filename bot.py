import discord
from discord.ext import commands

import json

bot = commands.Bot(command_prefix="$",intents=discord.Intents.all())

@bot.slash_command(name="help",description="查看機器人指令表")
async def help(ctx):
    await ctx.respond("嘿嘿") #使用respond回應斜線指令

with open("config.json","r") as file:
    data = json.load(file)
TOKEN = data["token"]
bot.run(TOKEN)