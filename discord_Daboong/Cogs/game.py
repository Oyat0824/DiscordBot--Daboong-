# dial.py
import discord, asyncio, random, os
from discord.ext import commands
from pytz import timezone
from datetime import datetime, timedelta

# 클래스 생성
class dial(commands.Cog):
    # 생성자
    def __init__(self, bot):
        self.bot = bot

    # 동전 관련
    @commands.command(pass_context = True , aliases=['동전', '동전던져줘', '코인'])
    async def coin(self, ctx):
        randomNum = random.randrange(1, 102)
        await ctx.send("{}".format(ctx.author.mention))
        if randomNum == 101:
            await ctx.send(embed = discord.Embed(description=':coin:　' + '동전이 섰다?!', color=0xFF8C00))
        elif 1 <= randomNum <= 50:
            await ctx.send(embed = discord.Embed(description=':coin:　' + '뒷면이에여!', color=0x6B8E23))
        elif 51 <= randomNum <= 100:
            await ctx.send(embed = discord.Embed(description=':coin:　' + '앞면이네여!', color=0xF9FD86))
    
    # 주사위 관련
    @commands.command(name = "주사위")
    async def dice(self, ctx):
        await ctx.send("에잇!")
        randomNum = random.randrange(1, 7)
        print(randomNum)
        await ctx.send("{}".format(ctx.author.mention))
        if randomNum == 1:
            await ctx.send(embed=discord.Embed(description=':game_die:　' + ':one:'))
        if randomNum == 2:
            await ctx.send(embed=discord.Embed(description=':game_die:　' + ':two:'))
        if randomNum == 3:
            await ctx.send(embed=discord.Embed(description=':game_die:　' + ':three:'))
        if randomNum == 4:
            await ctx.send(embed=discord.Embed(description=':game_die:　' + ':four:'))
        if randomNum == 5:
            await ctx.send(embed=discord.Embed(description=':game_die:　' + ':five:'))
        if randomNum == 6:
            await ctx.send(embed=discord.Embed(description=':game_die:　' + ':six:'))

# setup 함수 생성 후 Cog를 추가
def setup(bot):
    bot.add_cog(dial(bot))