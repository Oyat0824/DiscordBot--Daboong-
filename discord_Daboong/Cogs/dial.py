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

# 욕설 관련
    # 두려움 관련  
    @commands.command(pass_context = True , aliases=['주거', '주거버려', '죽어', '죽을래', '죽을래?', '죽어버려', '디져', '뒤져', '디질래?', '뒤질래?', '덤벼'])
    async def swear(self, ctx):
        randomNum = random.randrange(1, 101)
        if 1 <= randomNum <= 20:
            await ctx.send("무섭게.. 왜 그래여.. ㅠㅠ")
        elif 21 <= randomNum <= 40:
            await ctx.send("마! 니 어디 사나?!")
        elif 41 <= randomNum <= 60:
            await ctx.send("깝치지마")
        elif 61 <= randomNum <= 80:
            await ctx.send("ㅗ")
        elif 81 <= randomNum <= 100:
            file = discord.File("Kizaru.jpg")
            msg1 = await ctx.send(file=file)
            msg2 = await ctx.send("코와이네~")
    # 바보
    @commands.command(pass_context = True , name="바보")
    async def babo(self, ctx):
        babo = ['로봇인 제가 바보면 당신은..?', '저 바보 아니에여! :sob:']
        reply = random.choice(babo)
        await ctx.send(reply)
    # 멍청이
    @commands.command(pass_context = True , name="멍청이")
    async def dumm(self, ctx):
        dumm = ['저한테 한 말인가여?', '응 아니야~']
        reply = random.choice(dumm)
        await ctx.send(reply)
    # 어쩌라고
    @commands.command(pass_context = True , aliases=['어쩌라고', '어쩔', '어쩔티비', '저쩌라고', '저쩔', '저쩔티비'])
    async def wtd(self, ctx):
        wtd = ['응~ 어쩔티비~ 저쩔티비~ 안물티비~ 안궁티비~ 뇌절티비~', '우짤래미~ 저짤래미~ 쿠쿠루삥뽕', '지금 화났죠? 개킹받죠? 죽이고 싶죠? 어차피 내가 사는곳 모르죠? 응~ 못 죽이죠?', '어~또 빡치죠? 아무것도 모르죠? 아무것도 못하죠? 그냥 화났죠?', '냬~알걨섑니댸', '물어본 사람? 궁금한 사람?']
        reply = random.choice(wtd)
        await ctx.send(reply)
    # 섹드립
    @commands.command(pass_context = True , aliases=['빨아', '빨아줘'])
    async def suck(self, ctx):
        suck = ['씹어줄까여?', '6.9cm :pinching_hand:', '보여야 빨던가하지!', '너무 작은데?', '너무 작은걸?']
        reply = random.choice(suck)
        await ctx.send(reply)
    # 짖어
    @commands.command(pass_context = True , aliases=['짖어', '짖어봐'])
    async def wang(self, ctx):
        wang = ['멍! 멍!', '조시나 까잡숴~']
        reply = random.choice(wang)
        await ctx.send(reply)
    # 때찌
    @commands.command(pass_context = True , name="때찌")
    async def punch(self, ctx):
        punch = ['아얏!', '아파요!', '함 뜰까 똘게이야?']
        reply = random.choice(punch)
        await ctx.send(reply)
    # 나가
    @commands.command(pass_context = True , name="나가")
    async def naga(self, ctx):
        naga = ['네..', '수고하셨습니다..']
        reply = random.choice(naga)
        await ctx.send(reply)
    # ㅗㅗ
    @commands.command(pass_context = True , aliases=['ㅗ', 'ㅗㅗ'])
    async def hhh(self, ctx):
        hhh = ['ㅋ.. 이젠 하다 하다 이런 거까지 받아줘야 하나', '유치하다 그만해라..']
        reply = random.choice(hhh)
        await ctx.send(reply)
    # 하앍, 핥핥
    @commands.command(pass_context = True , aliases=['하앍', '핥핥', '하악', '하읏', '하앙', '그거하자'])
    async def hak(self, ctx):
        randomNum = random.randrange(1, 100)
        if 1 <= randomNum <= 33:
            await ctx.send("히익..!")
        elif 34 <= randomNum <= 66:
            await ctx.send("변태새끼!")
        elif 67 <= randomNum <= 84:
            file = discord.File("sr_otaku.jpg")
            msg = await ctx.send(file=file)
        elif 85 <= randomNum <= 99:
            file = discord.File("ok_go.png")
            msg = await ctx.send(file=file)
    # 응기잇
    @commands.command(pass_context = True , aliases=['응기잇', '섹스', '낑낑'])
    async def uwu(self, ctx):
        uwu = ['..하', '얼른 이 짓도 때려치우고 다른 데로 떠야 하는데..']
        reply = random.choice(uwu)
        await ctx.send(reply)
    # 느금마
    @commands.command(pass_context = True , aliases=["느금마", "느검마", "니애미", "니엄"])
    async def ngm(self, ctx):
        ngm = ['저희 어머니는 왜..?', '어머니까지 건드는 건 좀..']
        reply = random.choice(ngm)
        await ctx.send(reply)
    # 느금빠
    @commands.command(pass_context = True , aliases=["느금빠", "니애비", "느검빠"])
    async def ngf(self, ctx):
        ngf = ['열심히 일하시는 우리 아버지는 왜 건들어요..?', ':cry: 우리 아부진 미국 가 있어! 곧 돌아오실 거라구!']
        reply = random.choice(ngf)
        await ctx.send(reply)
# 인사 관련
    # Hi 관련
    @commands.command(pass_context = True , aliases=['안녕', '헬로', '반가워', '방가루', '방가방가', '하이', '안뇽'])
    async def hello(self, ctx):
        KST = datetime.now(timezone('Asia/Seoul'))
        print(KST)
        if 0 <= KST.hour <= 6:#0시~6시
            await ctx.send("아름다운 밤이에여! :wave:")
        elif 7 <= KST.hour <= 8:#7시~8시
            await ctx.send("아침 일찍부터 반가워여! :wave:")
        elif 9 <= KST.hour <= 11:#9시~11시
            await ctx.send("좋은 아침이에여! :wave:")
        elif 12 <= KST.hour <= 18:#12~18시
            await ctx.send("좋은 하루 되세여! :wave:")
        elif 19 <= KST.hour <= 23:#19시~23시
            await ctx.send("오늘도 수고하셨어여! :wave:")
        else:
            hi = ['안녕하세여!', '방가방가', '안냥!', '앗뇽!']
            reply = random.choice(hi)
            await ctx.send(reply)
    # Bye 관련
    @commands.command(pass_context = True , aliases=['잘가', '잘있어', '빠이', '바이'])
    async def bye(self, ctx):
        bye = ['들어가세여~', '다바~', '바이바이', '잘가여~', '고생많으셨어여~']
        reply = random.choice(bye)
        await ctx.send(reply)    
    # Sleep 관련
    @commands.command(pass_context = True , aliases=['잘자', '굿나잇', '내꿈꿔', '잘장'])
    async def Good_night(self, ctx):
        KST = datetime.now(timezone('Asia/Seoul'))
        print(KST)
        if 0 <= KST.hour <= 1:#0시~1시
            await ctx.send("안녕히 ..zzZ :sleeping:")
        elif 2 <= KST.hour <= 5:#2~5시
            await ctx.send(f"벌써 {KST.hour}시에여, 얼른 주무세여! :disappointed_relieved:")
        elif 6 <= KST.hour <= 8:#6시~8시
            await ctx.send("벌써 해가 떳다구여!? :scream:")
        elif 9 <= KST.hour <= 18:#9시~18시
            await ctx.send("저도 낮잠 좀 자야겠어여~ :kissing_closed_eyes:")
        elif 19 <= KST.hour <= 21:#19시~21시
            await ctx.send("오늘은 일찍 주무시네영?")
        elif 22 <= KST.hour <= 23:#22시~23시
            await ctx.send("안녕히 주무세여 ..zzZ :sleeping:")
        else:
            await ctx.send("안녕히 주무세요 ..zzZ :sleeping:")
    # Thx 관련
    @commands.command(pass_context = True , aliases=['고마워', '땡큐', '아리가또', '쎼쎼', '감사'])
    async def thx(self, ctx):
        thx = ['저도 고마워여!', '감사합니다!', '고마워여!', '감사링! 감사띠!']
        reply = random.choice(thx)
        await ctx.send(reply)
    # Love 관련
    @commands.command(pass_context = True , aliases=['사랑해', '사귀자', '좋아해', '결혼해줘', '결혼하자', '결혼할래?'])
    async def love(self, ctx):
        randomNum = random.randrange(1, 106)
        if 1 <= randomNum <= 10:
            await ctx.send("감사해여!")
        elif 11 <= randomNum <= 20:
            await ctx.send("마음만으로도 감사해여!")
        elif 21 <= randomNum <= 30:
            await ctx.send("고백으로 혼내주기 뭐 그런 건가여~? ㅎㅎ!")
        elif 31 <= randomNum <= 40:
            await ctx.message.add_reaction("❤️")
        elif 41 <= randomNum <= 50:
            await ctx.send("네.. ㅎㅎ..")
        elif 51 <= randomNum <= 60:
            await ctx.send("저 말고 다른 사람에게 나눠주는 게 좋을 거 같아여!")
        elif 61 <= randomNum <= 70:
            await ctx.send("혹시 거울은 보시고 사시나요?")
        elif 71 <= randomNum <= 80:
            await ctx.send("ㅔ")
        elif 81 <= randomNum <= 90:
            await ctx.send("네, 선생님 감사합니다.")
        elif 91 <= randomNum <= 95:
            msg = await ctx.send("더러운 새끼가 뭐라고 하는 거야")
            await asyncio.sleep(1)
            await msg.delete()
            await ctx.send("ㅎㅎ 저도여")
        elif 96 <= randomNum <= 100:
            msg = await ctx.send("아, 존나 자존심 상하네 씨발..")
            await asyncio.sleep(1)
            await msg.delete()
        elif 101 <= randomNum <= 105:
            file = discord.File("otaku.png")
            msg = await ctx.send(file=file)
            await asyncio.sleep(2)
            await msg.delete()
            await ctx.send("앗...")
        elif 106 <= randomNum <= 110:
            file = discord.File("otaku2.png")
            msg = await ctx.send(file=file)
            await asyncio.sleep(2)
            await msg.delete()
            await ctx.send("ㅋ")
# 질문 관련
    # 뭐해?
    @commands.command(pass_context = True , aliases=['뭐해', '뭐해?', '모해', '모해?'])
    async def WRUdoing(self, ctx):
        randomNum = random.randrange(1, 15)
        message = await ctx.send("저는 지금")
        await asyncio.sleep(0.7)
        do = [
            '저는 지금 청소하는 중이에여!',
            '저는 지금 빨래하는 중이에여!',
            '저는 지금 설거지하는 중이에여!',
            '저는 지금 강아지와 산책 중이에여!',
            '저는 지금 잠깐 쉬고 있어여!',
            '저는 지금 고양이 밥주고 있어여!',
            '저는 지금 강아지랑 산책 중이에여!',
            '저는 지금 밥 먹고 있어여!',
            '저는 지금 롤 하고 있어여!',
            '저는 지금 넷플릭스 보고 있어여!',
            '저는 지금 애니메이션 보고 있어여!',
            '저는 지금.. 므흣 :blush:',
            '저는 지금 업무 보는 중이에여!',
            '저는 지금 술 마시는 중이에여!'
            ]
        reply = random.choice(do)
        await message.edit(content = reply)
    # 골라줘
    @commands.command(pass_context = True , aliases=['결정해줘', '결정', '정해줘', '골라줘'])
    async def select(self, ctx):
        randomNum = random.randrange(1, 101)
        if randomNum == 100:
            msg = await ctx.send("가끔은 스스로 생각합니다. 쫌!!")
            await msg.edit(content="앗... 아닙니당 ㅎㅎ..")
        else:
            todo = ['하세여!', '하지마세여!', '안돼여!', '좋아여!', '그럴까요?', '잘 모르겠어요...', '별로에요.']
            reply = random.choice(todo)
            await ctx.send(reply)
    # 배고파
    @commands.command(pass_context = True , aliases=["배고파", "나배고파", "뭐먹을까", "뭐먹을까?"])
    async def hungry(self, ctx):
        hungry = ['밥을 드세요!', '오또케... :pleading_face:']
        reply = random.choice(hungry)
        await ctx.send(reply)
    # 심심해
    @commands.command(pass_context = True , aliases=["심심해", "나심심해", "뭐하고놀까", "뭐하고놀까?"])
    async def boring(self, ctx):
        boring = ['혼자 노는 법을 알면 좋겠네요! ㅎ', '어쩌라구욘~!']
        reply = random.choice(boring)
        await ctx.send(reply)
    # 놀아줘
    @commands.command(pass_context = True , aliases=["놀아줘", "놀자"])
    async def playme(self, ctx):
        playme = ['뭐 하구 놀까요?', '저랑 시체놀이 해요!']
        reply = random.choice(playme)
        await ctx.send(reply)

    # 핑
    @commands.command(pass_context = True , name="핑")
    async def ping(self, ctx):
        latency = self.bot.latency
        await ctx.send(f'퐁!　{round(latency * 1000)}ms')

# setup 함수 생성 후 Cog를 추가
def setup(bot):
    bot.add_cog(dial(bot))