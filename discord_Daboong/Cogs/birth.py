# birth.py
import discord, asyncio
from discord.ext import commands

# 클래스 선언
class birth(commands.Cog):
    # 생성자
    def __init__(self, bot):
        self.bot = bot

    # 명령어
    @commands.command(name="가입일", aliases=["가입날짜"])
    async def birth(self, ctx):
        Y = ctx.author.created_at.year
        M = ctx.author.created_at.month
        D = ctx.author.created_at.day
        embed = discord.Embed(title="{}님의 계정 생성일이에여!" .format(ctx.author.name), description=f"{Y}년 {M}월 {D}일", color=0xF9FD86)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        await ctx.send(embed = embed)

# setup 함수 생성 후 Cog를 추가
def setup(bot):
    bot.add_cog(birth(bot))