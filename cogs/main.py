import discord
from discord.ext import commands
from discord.commands import slash_command


class main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # 訊息指令範例
    @commands.command()
    async def here(self, ctx):
        await ctx.send(F"{ctx.author}你好,你現在在{ctx.guild.name}的{ctx.channel.mention}")

    #斜線指令範例    
    @slash_command(name="help", description="查看機器人指令表")
    async def help(self, ctx):
        await ctx.respond("嘿嘿")  # 使用respond回應斜線指令

    #特定權限可使用
    @slash_command(description="管理限定")
    async def admin(self,ctx):
        if ctx.author.guild_permissions.administrator: #檢查使用者的所有權限種是否有admin權限
            await ctx.respond("你是管理員")
        else:
            await ctx.respond("不是管理員不要來鬧欸")

    # 特定身份組能使用
    @slash_command(description="owner身份組限定")
    async def owner(self,ctx):
        role = ctx.guild.get_role(1032288469915013124) #抓取該身份組資訊
        if role in ctx.author.roles: # 檢查使用者是否有該身分
            await ctx.respond("你是owner!")
        else:
            await ctx.respond("你不是owner")

def setup(bot):
    bot.add_cog(main(bot))