#clear.py
import discord, asyncio
from discord.ext import commands

# 클래스 선언
class clear(commands.Cog):
    # 생성자
    def __init__(self, bot):
        self.bot = bot

    # 명령어
    @commands.command(name="청소")
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount:int):
        await ctx.message.delete()
        await ctx.channel.purge(limit = amount)
        await ctx.send('{}　>>　{}개의 메시지 청소 완료!'.format(ctx.author.mention, amount), delete_after = 15)

    # 명령어 오류일 경우
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("{}님! 이 명령어는 관리자만 가능해여!".format(ctx.author.mention), delete_after = 10)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("청소할 값을 입력해야 해여!", delete_after = 10)

# setup 함수 생성 후 Cog를 추가
def setup(bot):
    bot.add_cog(clear(bot))