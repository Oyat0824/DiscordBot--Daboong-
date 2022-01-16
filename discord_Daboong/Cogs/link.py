#-*- encoding: utf-8 -*-
import discord, asyncio
from discord.ext import commands
from urllib.request import urlopen, Request
from pytz import timezone
from datetime import datetime, timedelta
import urllib
import urllib.request
import bs4
from selenium import webdriver
import os
import sys
import json

class link(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def 날씨(self, ctx, location: str):
        enc_location = urllib.parse.quote(location+' 날씨')
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        todayBase = bsObj.find('div', {'class': 'main_info'})
        if (todayBase is None):
            await ctx.send("정보를 불러올 수 없습니다.:dizzy_face:")
        elif (todayBase is not None):
            todayTemp1 = todayBase.find('span', {'class': 'todaytemp'})
            todayTemp = todayTemp1.text.strip()  # 온도
            print("todayTemp", todayTemp)

            todayValueBase = todayBase.find('ul', {'class': 'info_list'})
            todayValue2 = todayValueBase.find('p', {'class': 'cast_txt'})
            todayValue = todayValue2.text.strip()  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌
            print("todayValue", todayValue)

            todayFeelingTemp1 = todayValueBase.find('span', {'class': 'sensible'})
            todayFeelingTemp = todayFeelingTemp1.text.strip()  # 체감온도
            print("todayFeelingTemp", todayFeelingTemp)
        
            tomorrowBase = bsObj.find('div', {'class': 'table_info weekly _weeklyWeather'})
            tomorrowTemp1 = tomorrowBase.find('li', {'class': 'date_info'})
            tomorrowTemp2 = tomorrowTemp1.find('dl')
            tomorrowTemp3 = tomorrowTemp2.find('dd')
            tomorrowTemp = tomorrowTemp3.text.strip()  # 오늘 오전,오후온도
            print("tomorrowTemp", tomorrowTemp)

            todayMiseaMongi1 = bsObj.find('div', {'class': 'sub_info'})
            print("todayMiseaMongi1",todayMiseaMongi1)
            
            if (todayMiseaMongi1 is None):
                embed = discord.Embed(title='Weather', description=location+ '의 기상 정보입니다.', colour=0xFFBB00)
                embed.add_field(name='현재 온도', value=todayTemp+'˚', inline=False)  # 현재온도, 체감온도
                embed.add_field(name='현재 날씨', value=todayValue, inline=False)  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌
                embed.add_field(name='오전/오후 온도', value=tomorrowTemp, inline=False)  # 오늘날씨
                embed.set_footer(text="by weatheri.co.kr")
                await ctx.send(embed=embed)
            else:
                todayMiseaMongi2 = todayMiseaMongi1.find('div', {'class': 'detail_box'})
                todayMiseaMongi3 = todayMiseaMongi2.find('dd')
                todayMiseaMongi = todayMiseaMongi3.text  # 미세먼지
                print("todayMiseaMongi", todayMiseaMongi)

                tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
                tomorrowMoring1 = tomorrowAreaBase.find('div', {'class': 'main_info morning_box'})
                tomorrowMoring2 = tomorrowMoring1.find('span', {'class': 'todaytemp'})
                tomorrowMoring = tomorrowMoring2.text.strip()  # 내일 오전 온도
                print("tomorrowMoring", tomorrowMoring)

                tomorrowValue1 = tomorrowMoring1.find('div', {'class': 'info_data'})
                tomorrowValue = tomorrowValue1.text.strip()  # 내일 오전 날씨상태, 미세먼지 상태
                print("tomorrowValue", tomorrowValue)

                tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
                tomorrowAllFind = tomorrowAreaBase.find_all('div', {'class': 'main_info morning_box'})
                tomorrowAfter1 = tomorrowAllFind[1]
                tomorrowAfter2 = tomorrowAfter1.find('p', {'class': 'info_temperature'})
                tomorrowAfter3 = tomorrowAfter2.find('span', {'class': 'todaytemp'})
                tomorrowAfterTemp = tomorrowAfter3.text.strip()  # 내일 오후 온도
                print("tomorrowAfterTemp", tomorrowAfterTemp)

                tomorrowAfterValue1 = tomorrowAfter1.find('div', {'class': 'info_data'})
                tomorrowAfterValue = tomorrowAfterValue1.text.strip()

                print("tomorrowAfterValue", tomorrowAfterValue)  # 내일 오후 날씨상태,미세먼지

                embed = discord.Embed(title='Weather',description=location+ '의 기상 정보입니다.',colour=0xFFBB00)
                embed.add_field(name='현재 온도', value=todayTemp+'˚, '+todayFeelingTemp, inline=False)  # 현재온도, 체감온도
                embed.add_field(name='현재 날씨', value=todayValue, inline=False)  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌
                embed.add_field(name='미세먼지', value=todayMiseaMongi, inline=False)  # 오늘 미세먼지
                embed.add_field(name='오전/오후 온도', value=tomorrowTemp+'**\n------------내일 날씨------------**', inline=False)  # 오늘날씨
                embed.add_field(name='오전', value=tomorrowMoring+'˚, '+tomorrowValue, inline=False)  # 내일오전날씨
                embed.add_field(name='오후', value=tomorrowAfterTemp + '˚, '+tomorrowAfterValue, inline=False)  # 내일오후 날씨상태
                embed.set_footer(text="by weatheri.co.kr")

                await ctx.send(embed=embed)
    
    @commands.command()
    async def 한강수온(self, ctx):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get('https://hangang.life/')
        html = driver.page_source
        #hdr = {'User-Agent': 'Mozilla/5.0'}
        #url = 'https://hangang.life/'
        #print(url)
        #req = Request(url, headers=hdr)
        #html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, 'html.parser')
        tempBase = bsObj.find('span',{'id':'hangang_temp'})
        print(tempBase)
        HangangTemp = tempBase.text.strip()
        print(HangangTemp)
		
        embed = discord.Embed(colour=0xFFBB00)
        embed.add_field(name='오늘의 한강 수온입니다.', value=HangangTemp, inline=False)  # 현재온도
        embed.set_footer(text="by hangang.life")
	
        await ctx.send(embed=embed)

    @commands.command()
    async def 롤(self, ctx, *usrl: str):
        usrl = list(filter(None, usrl))
        usr = " ".join(usrl)
        print(usrl, "usrl")
        if not len(usrl):
            await ctx.send("계정을 입력해 주세요")
            return
        else:
            message = await ctx.send("불러오는 중이에요!")
            enc_usr = urllib.parse.quote(usr)
            hdr = {'User-Agent': 'Mozilla/5.0'}
            url = 'https://op.gg/summoner/userName=' + enc_usr
            print(url)
            req = Request(url, headers=hdr)
            html = urllib.request.urlopen(req)
            bsObj = bs4.BeautifulSoup(html, "html.parser")
            ProfileIcon = bsObj.find('div', {'class':'ProfileIcon'})
            print("profile", ProfileIcon)
            if(ProfileIcon is None):
                await message.edit(content="정보를 불러올 수 없습니다.:dizzy_face:")
            thumb_img = ProfileIcon.find('img').get('src')
            thumb_url = "https:"+thumb_img
            print("thumb_url", thumb_url)
            Rankc = bsObj.find('div', {'class':'TierRank'})
            Rank = Rankc.text.strip()
            print("rank", Rank)
    
            if Rank=='Unranked':
                embed = discord.Embed(title='LOL',colour=0xFFBB00)
                embed.set_thumbnail(url=thumb_url)
                embed.add_field(name=Rank, value="먼저 등급전을 플레이해주세요.", inline=False)
                await message.edit(content=f'{usr}님의 전적입니다.')
                embed.set_footer(text="by op.gg")
                await ctx.send(embed=embed)
            if Rank != 'Unranked':
                LPc = bsObj.find('span', {'class':'LeaguePoints'})
                LP = LPc.text.strip()
                print(LP)
                WL = bsObj.find('span', {'class':'WinLose'})
                winc = WL.find('span', {'class':'wins'})
                losec = WL.find('span', {'class':'losses'})
                raitoc = WL.find('span', {'class':'winratio'})
                win = winc.text.strip()
                winK = win.replace("W", "승")
                lose = losec.text.strip()
                loseK = lose.replace("L", "패")
                raito = raitoc.text.strip()
                raitoK = raito.replace("Win Ratio", "승률")
        
                print(win, lose, raito)
                embed = discord.Embed(title='LOL전적',colour=0xFFBB00)
                embed.set_thumbnail(url=thumb_url)
                embed.add_field(name=Rank, value=LP+" | "+winK+" "+loseK+" | "+raitoK, inline=False)
                embed.set_footer(text="by op.gg")
        
                await message.edit(content=f'{usr}님의 전적입니다.')
                await ctx.send(embed=embed)
                
    @commands.command(pass_context = True , aliases=['코로나현황', '코로나', '코로나19'])
    async def covid19(self, ctx):
        KST = datetime.now(timezone('Asia/Seoul'))
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'http://ncov.mohw.go.kr/'
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        totalBase = bsObj.find('ul', {'class':'cityinfo'})
        total1 = totalBase.findAll('span', {'class':'num'})
        total = total1[0].text
        print("total", total)
        comp1 = totalBase.find('span', {'class':'sub_num red'})
        comp = comp1.text.strip()
        print("comp", comp)
        isol = total1[1].text
        print("isol", isol)
        deisol = total1[2].text
        print("deisol", deisol)
        death = total1[3].text
        print("death", death)
        tenM = total1[4].text
        print("tenM", tenM)
        embed = discord.Embed(title = 'COVID19', description= f"{KST.month}월 {KST.day}일의 코로나19 현황입니다.",colour=0xFFBB00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/762328035814146139/801707222890709042/pepecovid19.gif")
        embed.add_field(name='누적 확진자', value=total+" | 전일대비 "+comp, inline=False)
        embed.add_field(name='격리중', value=isol, inline=False)
        embed.add_field(name='격리해제', value=deisol, inline=False)
        embed.add_field(name='사망자', value=death, inline=False)
        embed.add_field(name='10만명당 발생률', value=f"{tenM}%", inline=False)
        embed.set_footer(text="by ncov.mohw.go.kr")
        await ctx.send(embed=embed)
    
    @commands.command()
    async def 주식(self, ctx, *col: str):
        col = list(filter(None, col))
        co = " ".join(col)
        if not len(col):
            await ctx.send("종목을 입력해 주세요")
            return
        else:
            enc_co = urllib.parse.quote(co+'주식')
            hdr = {'User-Agent': 'Mozilla/5.0'}
            url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_co
            print(url)
            req = Request(url, headers=hdr)
            html = urllib.request.urlopen(req)
            bsObj = bs4.BeautifulSoup(html, "html.parser")
        
            stockBase = bsObj.find('div', {'class': 'api_cs_wrap'})#외부 레이아웃 wrapper
            print('stb',stockBase)
        
            if stockBase is None:
                await ctx.send("정보를 불러올 수 없습니다.:dizzy_face:", delete_after=10)
            elif stockBase is not None:
                Bconame = stockBase.find('span',{'class':'stk_nm'})#종목 이름
                print("coname", Bconame)
                coname = Bconame.text.strip()

                Bchartimglink = stockBase.find('img',{'class':'_stock_chart'})#차트 이미지(링크)
                print(Bchartimglink)
                chartimglink = Bchartimglink['src']
                print(chartimglink)
            
                Pbase = stockBase.find('div', {'class': 'spt_tlt'})#종목 하위 레이아웃
                Plist = Pbase.find('span',{'class':'spt_con up'})
                if Plist is None:
                    Plist = Pbase.find('span',{'class':'spt_con dw'})
                #Bprice = Plist.find('span',{'class':'blind'})
                print(Plist)
                Bprice = Plist.text.strip()
                p = Bprice.split(" ")
                print("p: ",p)
            
                pr=[]
                #pr2=[]
                for item in p:
                    #문자열 치환
                    item_mod = item.replace("지수", "").replace("상승", "▲").replace("하락", "▼")
                    # 새로운 리스트에 추가
                    pr.append(item_mod)

        
                pr = " ".join(pr)
                print(pr)
        
                embed = discord.Embed(colour=0xFFBB00)
                #embed.set_thumbnail(url=chartimglink)
                embed.add_field(name=coname, value=f'{pr}', inline=False)
                #embed.add_field(name='updown', value=updown, inline=False)
                embed.set_footer(text="by finance.naver.com")
    
                await ctx.send(chartimglink)
                await ctx.send(embed=embed)



    
    @날씨.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("지역을 입력해 주세요.", delete_after=10)
    
    @주식.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("종목을 입력해 주세요.", delete_after=10)

def setup(bot):
    bot.add_cog(link(bot))