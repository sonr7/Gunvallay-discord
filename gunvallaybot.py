import discord
import asyncio
import youtube_dl
import re
import os
import ffmpeg
from discord.ext import commands
from discord.ext import tasks
import math
from functools import reduce
from operator import mul
from fractions import Fraction
from datetime import datetime
import time
import random
import sys
import wikipedia
import json
import urllib
from discord_slash import SlashCommand, SlashContext

kouyatitai = '790254976198115380'

main = '774933645001621545'

zikkenmain = '795957183988629546'

citycodes = {
    "北海道":"016010",
    "青森":"020010",
    "岩手":"030010",
    "宮城":"040010",
    "秋田":"050010",
    "山形":"060010",
    "福島":"070010",
    "茨城":"080010",
    "栃木":"090010",
    "群馬":"100010",
    "埼玉":"110010",
    "千葉":"120010",
    "東京":"130010",
    "神奈川":"140010",
    "新潟":"150010",
    "富山":"160010",
    "石川":"170010",
    "福井":"180010",
    "山形":"190010",
    "長野":"200010",
    "岐阜":"210010",
    "静岡":"220010",
    "愛知":"230010",
    "三重":"240010",
    "滋賀":"250010",
    "京都":"260010",
    "大阪":"270000",
    "兵庫":"280010",
    "奈良":"290010",
    "和歌山":"300010",
    "鳥取":"310010",
    "島根":"320010",
    "岡山":"330010",
    "広島":"340010",
    "山口":"350010",
    "徳島":"360010",
    "香川":"370000",
    "愛媛":"380010",
    "高知":"390010",
    "福岡":"400010",
    "佐賀":"410010",
    "長崎":"420010",
    "熊本":"430010",
    "大分":"440010",
    "宮崎":"450010",
    "鹿児島":"460010",
    "沖縄":"471010",    
}

def inverse(f):
    return Fraction(f.denominator,f.numerator)

from decimal import Decimal

import logging

logging.basicConfig(level=logging.INFO)

token = os.environ.get('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents = intents)

bot = discord.Client(intents=discord.Intents.all())

slash_client = SlashCommand(bot, sync_commands=True)

X = datetime.now().strftime('%H')
Xint = int(X) + 9
NK = f'今は%Y年%m月%d日{Xint}:%Mだぜ！'
now = datetime.now().strftime(NK)

async def create_channel(message, channel_name):
    guild = message.guild
    overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False), guild.me: discord.PermissionOverwrite(read_messages=True)}
    category_id = message.channel.category_id
    category = message.guild.get_channel(category_id)
    new_channel = await category.create_text_channel(name = channel_name, overwrites = overwrites)
    return new_channel

async def reply(message):
    reply = f'{message.author.mention}呼んだ？'
    await message.channel.send(reply)
    
async def zikan(message):
    timer0, timer1 = message.content.split()
    timers = int(timer1)
    timer2 = f'{timer1}杪待つのだ！'
    await message.channel.send(timer2)
    await asyncio.sleep(timers)
    timer = f'{message.author.mention}時間だよ！'
    await message.channel.send(timer)
    
async def NG(message):
    NG0, NG1 = message.content.split()
    with open('NG', 'a') as l:
        kaki = f'{NG1}\n'
        l.write(kaki)
    g = f'「{NG1}」を追加しました'
    await message.channel.send(g)
    
class Room():
    def __init__(self, hard = False):
        self.ans = ""
        if hard :
            for i in range(4):
                self.ans = self.ans + str(random.randrange(0, 10))
        else:
            l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            random.shuffle(l)
            for i in range(4):
                self.ans = self.ans + l[i]
        self.history = []  
    def step(selp, req):
        brow = 0 
        hit = 0
        for index, value in enumerate(req):
            if self.ans[index] == value:
                brow += 1
            elif self.ans.find(value) != -1:
                hit += 1
        return hit, brow

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}
    
ffmpeg_options = {
    'options': '-vn'
}
    
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')
    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

        
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
    
rooms = {0:"example"}

async def on_member_join(member):
    guild = member.guild
    channel = guild.get_channel(774679471809626124)
    await client.send_message(channel, 'よろしく！')

@slash_client.slash(name = 'ebr')
async def _slash_hello(ctx: SlashContext):
    embed = discord.Embed(title = 'みんはや鯖メンバー')
    guild = message.guild
    ebr_all = guild.member_count
    ebr_user = sum(1 for member in guild.members if not member.bot)
    ebr_bot = sum(1 for member in guild.members if member.bot)
    embed.add_field(name = '`メンバー数`', value = ebr_all)
    embed.add_field(name = '`人数`', value = ebr_user)
    embed.add_field(name = '`bot数`', value = ebr_bot)
    await ctx.send(embed = embed)
        
async def timer():
        guild = client.get_guild(774679471243788339)
        channel = guild.get_channel(774933645001621545)
        await client.send_message(channel, 'じほ')
        
nowY = datetime.now().strftime('%Y')
nowm = datetime.now().strftime('%m')
nowd = datetime.now().strftime('%d')
nowH_1 = datetime.now().strftime('%H')
nowM = datetime.now().strftime('%M')
nows = datetime.now().strftime('%S')
nowH_int = int(nowH_1)
nowH = nowH_int + 9
nowa = f'今は{nowY}年{nowm}月{nowd}日{nowH}時{nowM}分{nows}秒だぜ！'
nowtime = datetime.now().strftime('%H:%M')
     
@client.event
async def on_ready():
    print('起動しました')

@client.event
async def on_message(message):
    print(message.author.name + "<" + message.content)
    reg_res = re.compile(u"#wea (.+)").search(message.content)
    if message.author.bot:
        return
    if '。' in message.content:
        return
    if 'いってき' in message.content:
        await message.channel.send('いってら！今日もがんばれ👍')
    if '勉強' in message.content:
        await message.channel.send('勉強がんばれ👍')
    if 'おは' in message.content:
        await message.channel.send('おは！今日も一日がんばれ👍')
    if 'おやす' in message.content:
        await message.channel.send('おう！おやすみ！睡眠がんばれ👍')
    if  'こんにちは' in message.content or message.content == 'こんちゃ' or message.content == 'こんちゃす' or message.content == 'こんちゃすー' or message.content == 'Hi' or message.content == 'Hello':
        await message.channel.send('こんちゃ！頑張ってるかい？応援するぜ！がんばれ👍')
    if message.content == 'こんばんは' or message.content == 'こんばんはー':
        await message.channel.send('こんばんは！まだ今日は終わってないぞ！がんばれ👍')
    if 'ただいま' in message.content[0:4]: 
        await message.channel.send('おかえりぃ！頑張れたかい？')
    if 'がんば' in message.content or '頑張' in message.content:
        await message.channel.send('おう！俺も応援するぜ！がんばれ👍！')
    if message.content == '@がんばれ君':
        await message.channel.send('ん？どした？')
    if message.content == 'がんばった' or message.content == 'がんばったよ':
        await message.channel.send('よく頑張った！今後もがんばれ👍')
    if 'ハハッ' in message.content or 'ﾊﾊｯ' in message.content or 'ははっ' in message.content or 'はハッ' in message.content or 'はハっ' in message.content or 'ははッ' in message.content or 'ハはっ' in message.content or 'ハはッ' in message.content or 'ハハっ' in message.content:
        await message.channel.send('(ミッキーだよ)')
    if '#pls' in message.content:
        plus_list_str = message.content.split()
        plus_list_str.remove('#pls')
        plus_list = map(float, plus_list_str)
        plus = sum(plus_list)
        await message.channel.send(plus)
    if '#mns' in message.content:
        minus_list2_str = message.content.split()
        minus_list2_str.remove('#mns')
        minus11 = float(minus_list2_str[0])
        minus1 = Decimal(minus11)
        minus_list2_str.remove(minus_list2_str[0])
        minus_list2 = map(float, minus_list2_str)
        minus_list = [i * -1 for i in minus_list2]
        minus22 = sum(minus_list)
        minus2 = Decimal(minus22)
        minus = minus1 + minus2
        await message.channel.send(minus)
    if '#tim' in message.content:
        time_list_str = message.content.split()
        time_list_str.remove('#tim')
        time_list = map(float, time_list_str)
        time = reduce(mul, time_list)
        await message.channel.send(time)
    if '#div' in message.content:
        divide_list_str = message.content.split()
        divide_list_str.remove('#div')
        divide11_str = divide_list_str[0]
        divide11 = float(divide11_str)
        divide1 = Decimal(divide11)
        divide_list = map(float, divide_list_str)
        divide22 = reduce(mul, divide_list)
        divide2 = Decimal(divide22)
        divide = (divide1 / divide2) * divide1
        await message.channel.send(divide)
    if '#oio' in message.content:
        oio0, oio1_str, oio2_str = message.content.split( )
        oio1 = float(oio1_str)
        oio2 = float(oio2_str)
        oio = oio1 % oio2
        ii = oio1 // oio2
        iioio = f'{ii}あまり{oio}'
        await message.channel.send(iioio)
    if '#sqr' in message.content:
        square0, square1_str, square2_str = message.content.split()
        square1 = float(square1_str)
        square2 = float(square2_str)
        square = square1 ** square2
        await message.channel.send(square)
    if '#rot' in message.content:
        root0, root1_str = message.content.split()
        root1 = float(root1_str)
        root2 = math.sqrt(root1)
        root = f'√{root1}, {root2}'
        await message.channel.send(root)
    if '#now' in message.content:
        await message.channel.send(nowa)
    if '#help' in message.content:
        embed = discord.Embed(title = "がんばれ君が助けに来た！")
        embed.add_field(name = "``応答``", value = "たまに言葉で反応するときがあるよ！（「。」を使えば黙らせられるよー）", inline = False)
        embed.add_field(name = "``#pls x y``", value = "足し算できるよ！3個以上の数値もできるよ！（この場合はx+yになるよー）", inline = False)
        embed.add_field(name = "`#mns x y`", value = "引き算できるよ！3個以上の数値もできるよ！（この場合はx-yになるよー）", inline = False)
        embed.add_field(name = "`#tim x y`", value = "掛け算できるよ！3個以上の数値もできるよ！（この場合はx×yになるよー）", inline = False)
        embed.add_field(name = "`#div x y`", value = "割り算できるよ！3個以上の数値もできるよ！（この場合はx÷yになるよー）", inline = False)
        embed.add_field(name = "`#oio x y`", value = "割り算あまりできるよ！", inline = False)
        embed.add_field(name = "`#sqr x y`", value = "累乗できるよ！（この場合はxのy乗になるよー）", inline = False)
        embed.add_field(name = "`#rot x`", value = "ルートの値求めてくれるよ！", inline = False)
        embed.add_field(name = "`#llt x y z`", value = "ルーレットできるよ！（この場合はx,y,z,のどれかが出るよ！", inline = False)
        embed.add_field(name = "`#ebr`", value = "鯖内のデータがわかるよ！", inline = False)
        embed.add_field(name = "`#fjk`", value = "くぁwせdrftgyふじこlp", inline = False)
        embed.add_field(name = "`#wiki`", value = "wikiで検索してくれるよ！", inline = False)
        embed.add_field(name = "`#wach `", value = "wikiでxの検索候補を10個表示してくれるよ！", inline = False)
        embed.add_field(name = '`#ranks`', value = 'それぞれのみんはやのランクの人数を教えてくれるよ！', inline = False)
        embed.add_field(name = '`#zikan`', value = 'タイマーを使えるよ！', inline = False)
        embed.add_field(name = '`#wea`', value = '天気予報が見れるよ！(都道府県でやってね！)', inline = False)
        await message.channel.send(embed = embed)
    if '#llt' in message.content:
        rlt_list = message.content.split()
        rlt_list.remove('#llt')
        rlt_result = random.choice(rlt_list)
        await message.channel.send(rlt_result)
    if '#ebr' in message.content:
        embed = discord.Embed(title = 'みんはや鯖データ')
        guild = message.guild
        ebr_all = guild.member_count
        ebr_user = sum(1 for member in guild.members if not member.bot)
        ebr_bot = sum(1 for member in guild.members if member.bot)
        embed.add_field(name = '`メンバー数`', value = ebr_all)
        embed.add_field(name = '`人数`', value = ebr_user)
        embed.add_field(name = '`bot数`', value = ebr_bot)
        embed.add_field(name = 'テキストチャンネル数', value = len(message.guild.text_channels), inline = False)
        embed.add_field(name = 'ボイスチャンネル数', value = len(message.guild.voice_channels), inline = False)
        embed.add_field(name = 'カテゴリー数', value = len(message.guild.categories), inline = False)
        await message.channel.send(embed = embed)
    if '!d bump' in message.content:
        if message.content.startswith("!d bump"):
            if client.user!=message.author:
                def checks(m):
                    return m.channel == message.channel and m.author.id==302050872383242240
                bp=await client.wait_for('message', check=checks, timeout=15)
                msgid=bp.id
                embmsg=await message.channel.fetch_message(msgid)
                bumpdata="EmbedProxy(url='https://disboard.org/images/bot-command-image-bump.png', proxy_url='https://images-ext-1.discordapp.net/external/tAuRcs-FCy2M8OaTS9Ims62J1vrFiviahjBDtpZrrBs/https/disboard.org/images/bot-command-image-bump.png', width=800, height=200)"
                getdata=embmsg.embeds[0].image
                if str(bumpdata)==str(getdata):
                    await asyncio.sleep(7200)
                    embed = discord.Embed(title="BUMPできるよ！",description="BUMPがんばれ👍！",color=0x24B8B8)
                    await message.channel.send(embed=embed)
                    print("send:bump!!!")
    if '#ranks' in message.content:
        embed = discord.Embed(title = '**ランクごとの人数！**')
        guild = message.guild
        role_S2 = guild.get_role(774989846501654528)
        embed.add_field(name = '`S2ランク`', value = len(role_S2.members), inline = False)
        role_S1 = guild.get_role(774987289045630997)
        embed.add_field(name = '`S1ランク`', value = len(role_S1.members), inline = False)
        role_S = guild.get_role(774989364199424010)
        embed.add_field(name = '`Sランク`', value = len(role_S.members), inline = False)
        role_Ap = guild.get_role(774988208895033425)
        embed.add_field(name = '`A+ランク`', value = len(role_Ap.members), inline = False)
        role_A = guild.get_role(774987300420583475)
        embed.add_field(name = '`Aランク`', value = len(role_A.members), inline = False)
        role_Am = guild.get_role(774988863378030603)
        embed.add_field(name = '`A-ランク`', value = len(role_Am.members), inline = False)
        role_Bp = guild.get_role(774988447676235797)
        embed.add_field(name = '`B+ランク`', value = len(role_Bp.members), inline = False)
        role_B = guild.get_role(774988378596835339)
        embed.add_field(name = '`Bランク`', value = len(role_B.members), inline = False)
        role_Bm = guild.get_role(774988334509326337)
        embed.add_field(name = '`B-ランク`', value = len(role_Bm.members), inline = False)
        role_Cp = guild.get_role(774988120100700211)
        embed.add_field(name = '`C+ランク`', value = len(role_Cp.members), inline = False)
        role_C = guild.get_role(774988030590058526)
        embed.add_field(name = '`Cランク`', value = len(role_C.members), inline = False)
        role_Cm = guild.get_role(774987915004477470)
        embed.add_field(name = '`C-ランク`', value = len(role_Cm.members), inline = False)
        await message.channel.send(embed = embed)
    if message.content.startswith('#ebons'):
        guild = message.guild
        ebr_all = guild.member_count
        ebr_user = sum(1 for member in guild.members if not member.bot)
        ebr_bot = sum(1 for member in guild.members if member.bot)
        ebr_alls = f'メンバー数：{ebr_all}'
        ebr_users = f'人数：{ebr_user}'
        ebr_bots = f'bot数：{ebr_bot}'
        new_channel = await create_channel(message, channel_name = ebr_alls)
        new_channel = await create_channel(message, channel_name = ebr_users)
        new_channel = await create_channel(message, channel_name = ebr_bots)
    if '#fjk' in message.content:
        await message.channel.send('くぁwせdrftgyふじこlp')
    if client.user in message.mentions:
        await reply(message)
    if '#zikan' in message.content:
        await zikan(message)
    if '#wiki'in message.content:
        wiki1 = message.content[6:]
        wikipedia.set_lang('ja')
        try:
            page_title = wikipedia.page(wiki1)
            embed = discord.Embed(title = wiki1, url = f'https://ja.wikipedia.org/wiki/{wiki1}')
            page_summary = wikipedia.summary(wiki1)
            embed.add_field(name = page_title, value = page_summary, inline = False)
            await message.channel.send(embed = embed)
        except wikipedia.exceptions.DisambiguationError:
            page_search = wikipedia.search(wiki1, results = 11)
            page_search_url = f'https://ja.wikipedia.org/wiki/{page_search}'
            embed = discord.Embed()
            for page in page_search:
                page_int = page_search.index(page)
                page_url = f'https://ja.wikipedia.org/wiki/{page}'
                embed.add_field(name = page, value = f'「{page}」で再検索', inline = False)
            await message.channel.send(embed = embed)
        except wikipedia.exceptions.PageError:
            await message.channel.send('ページが見つからん！')
    if nowtime == '00:00':
        await timer()
    if '#ngadd' in message.content:
        await NG(message)
    if '#nglist' in message.content:
        embed = discord.Embed(title = 'NGワード一覧', description = 'このリスト内のワードは言っちゃだめだよ！')
        with open('NG') as ng:
            ngl = ng.read()
        fs = ngl.splitlines()
        for f in fs:
            embed.add_field(name = f, value = f, inline = False)
        await message.channel.send(embed = embed)
    if '#wach' in message.content:
        re.sub('#wiki', '', message.content)
        wikipedia.set_lang('ja')
        page_ach = wikipedia.search(message.content, results = 11)
        page_search_url = f'https://ja.wikipedia.org/wiki/{page_ach}'
        embed = discord.Embed()
        for pages in page_ach:
            pages_int = page_ach.index(pages)
            pages_url = f'https://ja.wikipedia.org/wiki/{pages}'
            embed.add_field(name = pages, value = f'「{pages}」で再検索', inline = False)
        await message.channel.send(embed = embed)
    if message.channel.name == '自己紹介':
        yorosiku = "<:yorosiku:884506700126752828>"
        ok = "<:OK:884506700126752828>"
        await message.add_reaction(yorosiku)
        await message.add_reaction(ok)
    if message.content == "#hb":
        embed = discord.Embed(title = 'Hit&Browの遊び方', description = '相手の思っている数字を推理して当てるゲームだよ！\n数字と場所があってたら「Hit」、\n数字があっていても場所が違っていたら「Brow」でカウントするよ！\n最終的に3Hitにすれば勝ちだよ！')
        embed.add_field(name = '#hs', value = 'ゲームを始めるよ！', inline = False)
        embed.add_field(name = '#hc', value = 'あってるか確認するよ！', inline = False)
        embed.add_field(name = '#hd', value = 'どうしてもわからないときに使ってね！（答えが出るよ）', inline = False)
        await message.channel.send(embed = embed)
    if message.content == '#hs':
        if message.channel.id in rooms:
            await message.channel.send('使用中なう')
            return
        rooms[message.channel.id] = Room()
        await message.channel.send('スタート！')    
    if(message.content[0:3]=="#hc") and message.channel.id in rooms:
        req=message.content[3:]
        req=req.replace(" ","")
        if len(req)!=4:
            await message.channel.send('４桁の番号だよ！')
            return
        hit, brow = rooms[message.channel.id].step(req)
        rooms[message.channel.id].history.append({'request':req, 'hit':hit, 'brow':brow})
        await message.channel.send('リクエスト：'+ req + '\n結果：{}ヒット {}ブロー'.format(hit, brow))
        if req == rooms[message.channel.id].ans:
            await message.channel.send('正解！')
            say = '今までの記録だよ！\n質問回数：{}回| 数字 | ヒット | ブロー |\n'.format(len(rooms[message.channel.id].history))
            for i in rooms[message.channel.id].history:
                say = say + '| {} |  {}  |  {}  |\n'.format(i['request'],i['hit'],i['brow'])
            await message.channel.send(say)
            del rooms[message.chanenl.id]
    if message.content == '#hd' and message.channel.id in rooms:
        await message.channel.send('ゲーム終了！答え：' + rooms[message.channel.id].ans)
        del rooms[message.channel.id]
    if message.content == '#hy' and message.channel.id in rooms:
        say = '今までの記録だよ！\n質問回数：{}回| 数字 | ヒット |  ブロー |\n'.format(len(rooms[message.channel.id].history))
        for i in rooms[message.channel.id].history:
            say = say + '| {} |  {}  |  {}  |\n'.format(i['request'], i['hit'], i['brow'])
        await message.channel.send(say)
    if message.content == '#join':
        if message.author.voice is None:
            await message.channel.send("おーっと、ボイスチャンネルにいないからできないようだ！")
            return
        await message.author.voice.channel.connect()
    elif message.content == '#leave':
        if message.guild.voice_client is None:
            await message.channel.send("おーっと、ボイスチャンネルにいないからできないようだ！")
            return
        await message.guild.voice_client.disconnect()
        await message.channel.send("バイバイ！")
    elif message.content.startswith('#p'):
        if message.guild.voice_client is None:
            await message.channel.send("接続していません。")
            return
        if message.guild.voice_client.is_playing():
            await message.channel.send("再生中だよ！")
            return
        url = message.content[3:]
        player = await YTDLSource.from_url(url, loop=client.loop)
        await message.guild.voice_client.play(player)
        await message.channel.send('{} を再生するよ！'.format(player.title))
    elif message.content == "!stop":
        if message.guild.voice_client is None:
            await message.channel.send("おーっと、ボイスチャンネルにいないからできないようだ！")
            return
        if not message.guild.voice_client.is_playing():
            await message.channel.send("おーっと、再生してないからできないようだ！")
            return
        message.guild.voice_client.stop()
        await message.channel.send("停止...")
    if reg_res:
      if reg_res.group(1) in citycodes.keys():
        citycode = citycodes[reg_res.group(1)]
        resp = urllib.request.urlopen(f"https://weather.tsukumijima.net/api/forecast/city/{citycode}").read()
        resp = json.loads(resp.decode("utf-8"))
        msg = "__【お天気情報：**" + resp["location"]["city"] + "**" + f["temperature"] + "：**" + f.int(["max"]["celsius"]) + f.int(["min"]["celsius"]) + "**\n"
        for f in resp["forecasts"]:
          msg += f["dateLabel"] + "：**" + f["telop"] + "**\n"
        msg += "```" + resp["description"]["bodyText"] + "```"
        await message.channel.send(msg)
      else:
        await message.channel.send("そこの天気はわかりません...")
        
        
async def on_member_join(member):
    guild = member.guild
    channel = guild.get_channel(774679471809626124)
    await client.send_message(channel, 'よろしく！')


        


                                   
                                   
        
        
                            
                            
                        
                                                                                             
                                               
            


                                               
        
            
            
                                             
                                             
        
       
                   

client.run(token)
