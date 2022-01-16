#main.py
import os, asyncio, discord, random
from discord.ext import commands, tasks
from itertools import cycle

# 봇 접두사 설정
bot = commands.Bot(command_prefix="다붕아 ")

# 봇 기본 도움말 삭제
bot.remove_command('help')

# 디스코드 봇 토큰
token_path = os.path.dirname(os.path.abspath( __file__ ))+"/token.txt"
t = open(token_path, "r" ,encoding = "utf-8")
token = t.read().split()[0]

# 관리자 확인
def is_owner(ctx):
    return ctx.message.author.id == 314362974829543424

# 봇 순환 상태 메시지 설정
# status에 n 자리 표시자를 놔두고 루프 내부에서 서식 지정
status = cycle(["설거지", "밥", "{n}개의 서버에서 운영"])

# 봇 상태메시지 순환
@tasks.loop(seconds = 6000)
async def change_status():
    # next(status).format(n=len(bot.guilds))
    name = next(status)
    name = name.format(n=len(bot.guilds))
    
    # online , idle , dnd , offline # 온라인 , 자리비움, 다른용무, 오프라인
    await bot.change_presence(status = discord.Status.online, activity=discord.Game(name))

# 봇이 실행되면 콘솔창에 표시
@bot.event
async def on_ready():
    change_status.start()
    print("#### 봇 연결 성공 ####")
    print(f"> 봇 이름 : {bot.user.name}")
    print(f"> ID : {bot.user.id}")
    print(f"> 토큰 키 : ", token)
    print(f"> 가입된 채널 수 : {len(bot.guilds)}")

# 일반 명령어 로드
for filename in os.listdir("Cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"Cogs.{filename[:-3]}")


################### 관리자 명령어 ###################
# 로드 관련
@bot.command(name="로드")
@commands.check(is_owner)
async def load_commands(ctx, extension):
    bot.load_extension(f"Cogs.{extension}")
    await ctx.send(f":white_check_mark:　**{extension}**　::　로드!")

@bot.command(name="언로드")
@commands.check(is_owner)
async def unload_commands(ctx, extension):
    bot.unload_extension(f"Cogs.{extension}")
    await ctx.send(f":white_check_mark:　**{extension}**　::　언로드!")

@bot.command(name="리로드")
@commands.check(is_owner)
async def reload_commands(ctx, extension=None):
    if extension is None:   # 그냥 리로드 명령어만 적었을 경우
        for filename in os.listdir("Cogs"):
            if filename.endswith(".py"):
                bot.unload_extension(f"Cogs.{filename[:-3]}")
                bot.load_extension(f"Cogs.{filename[:-3]}")
                await ctx.send(f":white_check_mark:　**{filename[:-3]}**　::　리로드!")
    else:                   # 특정 파일 리로드
        bot.unload_extension(f"Cogs.{extension}")
        bot.load_extension(f"Cogs.{extension}")
        await ctx.send(f":white_check_mark:　**{extension}**　::　리로드!")

@load_commands.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("{}님은 개발자가 아니에요:(".format(ctx.author.mention), delete_after=10)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("모듈 이름을 입력해주세요.", delete_after=10)

@unload_commands.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("{}님은 개발자가 아니에요:(".format(ctx.author.mention), delete_after=10)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("모듈 이름을 입력해주세요.", delete_after=10)
        
@reload_commands.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("{}님은 개발자가 아니에요:(".format(ctx.author.mention), delete_after=10)

# 참가서버
@bot.command(name="참가서버")
@commands.check(is_owner)
async def inServer(self, ctx):
    for guild in self.client.guilds:
        await ctx.send(guild.name)

# 명령어가 존재 하지 않을 경우
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
    	await ctx.send("명령어가 존재하지 않습니다.")

# 봇 실행
print("접속 중. . .")
bot.run(token)