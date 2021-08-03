import discord
import asyncio
import re
import os
from discord.ext import commands
import math
from functools import reduce
from operator import mul
from fractions import Fraction
import datetime
import time
import random


def inverse(f):
    return Fraction(f.denominator,f.numerator)

from decimal import Decimal

import logging

logging.basicConfig(level=logging.INFO)

token = os.environ.get('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print('起動しました')

@client.event
async def on_message(message):
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
    if '#p' in message.content:
        plus_list_str = message.content.split()
        plus_list_str.remove('#p')
        plus_list = map(float, plus_list_str)
        plus = sum(plus_list)
        await message.channel.send(plus)
    if '#m' in message.content:
        minus_list2_str = message.content.split()
        minus_list2_str.remove('#m')
        minus11 = float(minus_list2_str[0])
        minus1 = Decimal(minus11)
        minus_list2_str.remove(minus_list2_str[0])
        minus_list2 = map(float, minus_list2_str)
        minus_list = [i * -1 for i in minus_list2]
        minus22 = sum(minus_list)
        minus2 = Decimal(minus22)
        minus = minus1 + minus2
        await message.channel.send(minus)
    if '#t' in message.content:
        time_list_str = message.content.split()
        time_list_str.remove('#t')
        time_list = map(float, time_list_str)
        time = reduce(mul, time_list)
        await message.channel.send(time)
    if '#d' in message.content:
        divide_list_str = message.content.split()
        divide_list_str.remove('#d')
        divide11_str = divide_list_str[0]
        divide11 = float(divide11_str)
        divide1 = Decimal(divide11)
        divide_list = map(float, divide_list_str)
        divide22 = reduce(mul, divide_list)
        divide2 = Decimal(divide22)
        divide = (divide1 / divide2) * divide1
        await message.channel.send(divide)
    if '#o' in message.content:
        oio0, oio1_str, oio2_str = message.content.split( )
        oio1 = float(oio1_str)
        oio2 = float(oio2_str)
        oio = oio1 % oio2
        ii = oio1 // oio2
        iioio = f'{ii}あまり{oio}'
        await message.channel.send(iioio)
    if '#s' in message.content:
        square0, square1_str, square2_str = message.content.split()
        square1 = float(square1_str)
        square2 = float(square2_str)
        square = square1 ** square2
        await message.channel.send(square)
    if '#r' in message.content:
        root0, root1_str = message.content.split()
        root1 = float(root1_str)
        root2 = math.sqrt(root1)
        root = f'√{root1}, {root2}'
        await message.channel.send(root)
    if '今何時' in message.content:
        await message.channel.send(now)
    if '#help' in message.content:
        embed = discord.Embed(title = "がんばれ君が助けに来た！")
        embed.add_field(name = "応答", value = "たまに言葉で反応するときがあるよ！（「。」を使えば黙らせられるよー）", inline = False)
        embed.add_field(name = "#p x y", value = "足し算できるよ！3個以上の数値もできるよ！（この場合はx+yになるよー）", inline = False)
        embed.add_field(name = "#m x y", value = "引き算できるよ！3個以上の数値もできるよ！（この場合はx-yになるよー）", inline = False)
        embed.add_field(name = "#t x y", value = "掛け算できるよ！3個以上の数値もできるよ！（この場合はx×yになるよー）", inline = False)
        embed.add_field(name = "#d x y", value = "割り算できるよ！3個以上の数値もできるよ！（この場合はx÷yになるよー）", inline = False)
        embed.add_field(name = "#o x y", value = "割り算あまりできるよ！", inline = False)
        embed.add_field(name = "#s x y", value = "累乗できるよ！（この場合はxのy乗になるよー）", inline = False)
        embed.add_field(name = "#r x", value = "ルートの値求めてくれるよ！", inline = False)
        embed.add_field(name = "#llt x y z", value = "ルーレットできるよ！（この場合はx,y,z,のどれかが出るよ！", inline = False)
        embed.add_field(name = "#ebr", value = "鯖内のメンバー数、人数、BOT数がわかるよ！", inline = False)
        await message.channel.send(embed = embed)
    if '#llt' in message.content:
        rlt_list = message.content.split()
        rlt_list.remove('#llt')
        rlt_result = random.choice(rlt_list)
        await message.channel.send(rlt_result)
    if '#ebr' in message.content:
        guild = message.guild
        ebr_all = guild.member_count
        ebr_user = sum(1 for member in guild.members if not member.bot)
        ebr_bot = sum(1 for member in guild.members if member.bot)
        ebr = f'メンバー数:{ebr_all}　人数:{ebr_user}　bot数:{ebr_bot}'
        await message.channel.send(ebr)
    if '!d bumpe' in message.content:
        count = 0
        while count <= 5:
            try:
                def check(m):
                    return m.channel.id == message.channel.id
                bump_message = await client.wait_for("message", check = check, timeout = 5)
                if '!d bumpe!' in message.content:
                    await message.channel.send("まだ経ってないよ！")
            except asyncio.TimeoutError:
                await message.channel.send('bumpできるよ！')
            return
            
                    
                
     


            

        
        
        
@client.event
async def reply(message):
    reply = f'{message.author.mention} ん？どした？' 
    await message.channel.send(reply) 

client.run(token)
