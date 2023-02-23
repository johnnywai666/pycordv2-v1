import discord
from discord.ext import commands

import json

bot = commands.Bot(command_prefix="$",intents=discord.Intents.all())

@bot.command()
async def here(ctx):
    await ctx.send(F"{ctx.author}你好,你現在在{ctx.guild.name}的{ctx.channel.mention}")

@bot.command()
async def set_welcome(ctx,channel:discord.TextChannel):
    with open("data/welcome.json","r") as file:
        data = json.load(file)
    data[str(ctx.guild.id)] = channel.id
    with open("data/welcome.json","w") as file:
        json.dump(data,file,indent=4)
    await ctx.send("資料更新成功")

@bot.command()
async def set_leave(ctx,channel:discord.TextChannel):
    with open("data/leave.json","r") as file:
        data = json.load(file)
    data[str(ctx.guild.id)] = channel.id
    with open("data/leave.json","w") as file:
        json.dump(data,file,indent=4)
    await ctx.send("資料更新成功")

@bot.event
async def on_member_join(member):
    with open("data/welcome.json","r") as file:
        data = json.load(file)
    if str(member.guild.id) in data:
        channel = bot.get_channel(data[str(member.guild.id)])
        await channel.send(f"{member.mention} 歡迎加入")

@bot.event
async def on_member_remove(member):
    with open("data/leave.json","r") as file:
        data = json.load(file)
    if str(member.guild.id) in data:
        channel = bot.get_channel(data[str(member.guild.id)])
        await channel.send(f"{member.mention} 離開了")

with open("data/config.json","r") as file:
    data = json.load(file)
TOKEN = data["token"]
bot.run(TOKEN)