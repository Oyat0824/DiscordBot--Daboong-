# info.py
import discord, asyncio
from discord.ext import commands

# 클래스 선언
class info(commands.Cog):
    # 생성자
    def __init__(self, bot):
        self.bot = bot

    # 초대 코드
    @commands.command(name = "초대", aliases=['초대링크', '초대링크줘', '초대줘', '초대해줘'])
    async def invite(self, ctx):
        await ctx.send("초대링크 입니다! :smiling_face_with_3_hearts:")
        await ctx.send(embed=discord.Embed(title="초대링크", url="https://discord.com/api/oauth2/authorize?client_id=932212201090068510&permissions=8&scope=bot"))

# setup 함수 생성 후 Cog를 추가 
def setup(bot):
    bot.add_cog(info(bot))