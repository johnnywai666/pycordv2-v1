import json

import discord
from discord.ext import commands


class welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def set_welcome(self, ctx, channel: discord.TextChannel):
        with open("data/welcome.json", "r") as file:  # 用read模式開啟檔案
            data = json.load(file)  # 抓取檔案資料
        # 更新字典的資料(請見https://youtu.be/y7Wa7NaSKgs)
        data[str(ctx.guild.id)] = channel.id
        with open("data/welcome.json", "w") as file:  # 用write模式開啟檔案
            json.dump(data, file, indent=4)  # 上載更新後的資料
        await ctx.send("資料更新成功")

    @commands.command()
    async def set_leave(self, ctx, channel: discord.TextChannel):
        with open("data/leave.json", "r") as file:  # 用read模式開啟檔案
            data = json.load(file)  # 抓取檔案資料
        # 更新字典的資料(請見https://youtu.be/y7Wa7NaSKgs)
        data[str(ctx.guild.id)] = channel.id
        with open("data/leave.json", "w") as file:  # 用write模式開啟檔案
            json.dump(data, file, indent=4)  # 上載更新後的資料
        await ctx.send("資料更新成功")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open("data/welcome.json", "r") as file:  # 用read模式開啟檔案
            data = json.load(file)  # 抓取檔案資料
        if str(member.guild.id) in data:  # 判斷該群組是否有資料
            channel = self.bot.get_channel(data[str(member.guild.id)]) # 由資料裡的ID找到頻道
            await channel.send(f"{member.mention} 歡迎加入")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        with open("data/leave.json", "r") as file:  # 用read模式開啟檔案
            data = json.load(file)  # 抓取檔案資料
        if str(member.guild.id) in data:  # 判斷該群組是否有資料
            channel = self.bot.get_channel(data[str(member.guild.id)]) # 由資料裡的ID找到頻道
            await channel.send(f"{member.mention} 離開了")


def setup(bot):
    bot.add_cog(welcome(bot))
