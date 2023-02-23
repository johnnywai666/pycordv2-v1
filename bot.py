import discord
import os
from discord.ext import commands
from discord.commands import Option

import json

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all()) # 定義什麼是bot

for file in os.listdir('./cogs'):  # 抓取所有cog資料夾裡的檔案
    if file.endswith('.py'):  # 判斷檔案是否是python檔
        try:
            # 載入cog,[:-3]是字串切片,為了把.py消除
            bot.load_extension(f'cogs.{file[:-3]}')
            print(f'✅   已加載 {file}')
        except Exception as error:  # 如果cog未正確載入
            print(f'❎   {file} 發生錯誤  {error}')

with open("config.json", "r") as file: # 使用閱讀模式開啟資料檔案
    data = json.load(file) # 讀取資料檔的內容
bot.run(data["token"]) # 這是啟動機器人的部分哪