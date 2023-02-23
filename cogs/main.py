import discord
from discord.ext import commands
from discord.commands import slash_command


class main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def here(self, ctx):
        await ctx.send(F"{ctx.author}你好,你現在在{ctx.guild.name}的{ctx.channel.mention}")

    @slash_command(name="help", description="查看機器人指令表")
    async def help(self, ctx):
        await ctx.respond("嘿嘿")  # 使用respond回應斜線指令


def setup(bot):
    bot.add_cog(main(bot))
