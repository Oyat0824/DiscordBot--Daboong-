# help.py
import discord, asyncio, os
from discord.ext import commands

# 버전 파일 경로 및 세팅
ver_path = os.path.dirname( os.path.abspath( __file__ ) )+"/ver.txt"
v = open(ver_path,"r",encoding="utf-8")
ver = v.read().split()[0]

# 클래스 생성
class help(commands.Cog):
    # 생성자
    def __init__(self, bot):
        self.bot = bot

    # 명령어
    @commands.command(pass_context = True, name="도움", aliases=["도와줘", "헬프", "help", "Help", "헤업"])
    async def _help(self, ctx):
    # 임베드 1
        # Embed : Body, Author
        page1 = discord.Embed(title = "사용법", description = " ", color = 0xF9FD86)
        page1.set_author(name = "다붕이", url="https://discord.com/api/oauth2/authorize?client_id=932212201090068510&permissions=8&scope=bot", icon_url="https://i.imgur.com/qKQ7cNI.png")
        
        # Embed : Images
        page1.set_thumbnail(url = "https://i.imgur.com/8RkPr1Z.jpg")
        
        # Embed : Fields
        page1.add_field(name = "명령어 접두사", value="`다붕아 (명령어)`", inline=False)
        page1.add_field(name = "초대", value="`다붕아 초대`", inline=False)
        page1.add_field(name = "카테고리", value="`대화` | `관리` | `게임` | `정보` | `부가기능`", inline=False)

        # Embed : Footer
        page1.set_footer(text = f"다붕이 버전_{ver}　by Oyat　　||　　page 1/6")

    # 임베드 2
        # Embed : Body, Author
        page2=discord.Embed(title='대화 사용법', description=' ', color=0xF9FD86)
        page2.set_author(name="다붕이", url="https://discord.com/api/oauth2/authorize?client_id=932212201090068510&permissions=8&scope=bot", icon_url="https://i.imgur.com/qKQ7cNI.png")
        
        # Embed : Fields
        page2.add_field(name = "안녕", value="`인사해줍니다.`", inline=False)
        page2.add_field(name = "잘가", value="`작별 인사해줍니다.`", inline=False)
        page2.add_field(name = "잘자", value="`자라고 해줍니다.`", inline=False)
        page2.add_field(name = "감사", value="`감사 해줍니다.`", inline=False)
        page2.add_field(name = "사랑해", value="`사랑해 해줍니다.`", inline=False)
        page2.add_field(name = "뭐해", value="`뭐하는지 물어봅니다.`", inline=False)
        page2.add_field(name = "그 외", value="`여러가지 있습니다, 알아서 찾으세요.`", inline=False)

        # Embed : Footer
        page2.set_footer(text = f"다붕이 버전_{ver}　by Oyat　　||　　page 2/6")
    # 임베드 3
        # Embed : Body, Author    
        page3=discord.Embed(title='관리 사용법', description=' ', color=0xF9FD86)
        page3.set_author(name="다붕이", url="https://discord.com/api/oauth2/authorize?client_id=932212201090068510&permissions=8&scope=bot", icon_url="https://i.imgur.com/qKQ7cNI.png")
        
        # Embed : Fields
        page3.add_field(name = "청소 (숫자)", value="`채팅창을 청소 합니다.`", inline=False)

        # Embed : Footer
        page3.set_footer(text = f"다붕이 버전_{ver}　by Oyat　　||　　page 3/6")
    
    # 임베드 4
        # Embed : Body, Author     
        page4=discord.Embed(title='게임 사용법', description=' ', color=0xF9FD86)
        page4.set_author(name="다붕이", url="https://discord.com/api/oauth2/authorize?client_id=932212201090068510&permissions=8&scope=bot", icon_url="https://i.imgur.com/qKQ7cNI.png")

        # Embed : Fields
        page4.add_field(name = "주사위", value="`주사위를 던집니다.`", inline=False)
        page4.add_field(name = "동전", value="`동전을 던집니다.`", inline=False)

        # Embed : Footer
        page4.set_footer(text = f"다붕이 버전_{ver}　by Oyat　　||　　page 4/6")
    
    # 임베드 5
        # Embed : Body, Author     
        page5=discord.Embed(title='정보 사용법', description=' ', color=0xF9FD86)
        page5.set_author(name="다붕이", url="https://discord.com/api/oauth2/authorize?client_id=932212201090068510&permissions=8&scope=bot", icon_url="https://i.imgur.com/qKQ7cNI.png")
        
        # Embed : Fields
        #page5.add_field(name = "한강수온", value="`한강수온을 알려줍니다.`", inline=False)
        page5.add_field(name = "가입일", value="`가입일을 보여줍니다.`", inline=False)
        #page5.add_field(name = "날씨 (지역)", value="`해당 지역 날씨를 알려줍니다.`", inline=False)
        page5.add_field(name = "롤 (아이디)", value="`계정 전적을 알려줍니다.`", inline=False)

        # Embed : Footer
        page5.set_footer(text = f"다붕이 버전_{ver}　by Oyat　　||　　page 5/5")

    # 변수 및 출력 설정 
        pg = [page1, page2, page3, page4, page5]
        pages = 5
        cur_page = 1
        txt = await ctx.send("{}　{} 서버의 귀염둥이 다붕이 등장!".format(ctx.author.mention, ctx.guild.name))
        message = await ctx.send(embed = pg[cur_page - 1])
        
    # 편집 및 반응을 위한 메시지 개체 가져오기
        await message.add_reaction("◀️")
        await message.add_reaction("▶️")
        await message.add_reaction("📌")

    # 명령을 보낸 사람 제외는 작동 불가
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️", "📌"]
    
        while True:
            # 반응이 추가될 때까지 대기 - x초 후 시간 초과
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout = 180, check = check)
                
                if str(reaction.emoji) == "📌":
                    await message.clear_reaction("◀️")
                    await message.clear_reaction("▶️")
                    await message.clear_reaction("📌")
                    await txt.edit(content = "📌 고정되었습니다.", delete_after=5)
                    break

                if str(reaction.emoji) == "▶️" and cur_page != pages:
                    cur_page += 1
                    await message.edit(embed=pg[cur_page-1])
                    await message.remove_reaction(reaction, user)

                elif str(reaction.emoji) == "◀️" and cur_page > 1:
                    cur_page -= 1
                    await message.edit(embed=pg[cur_page-1])
                    await message.remove_reaction(reaction, user)
                
                # 사용자가 마지막 페이지로 넘어가려고 하면 반응을 제거하거나
                # 첫 페이지에서 뒤로
                else:
                    await message.remove_reaction(reaction, user)

            except asyncio.TimeoutError:
                await message.delete()
                break

# setup 함수 생성 후 Cog를 추가            
def setup(bot):
    bot.add_cog(help(bot))