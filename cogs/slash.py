import discord
from discord.ext import commands
from discord.commands import Option
from discord.commands import slash_command


class slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    info = discord.SlashCommandGroup(
        "info",
        "查詢資訊"
    )

    @slash_command(description="查詢用戶資訊")
    async def user(self,ctx,user:Option(discord.User,"要查詢的用戶")):
        await ctx.respond(F"{user.id}")
    

def setup(bot):
    bot.add_cog(slash(bot))
