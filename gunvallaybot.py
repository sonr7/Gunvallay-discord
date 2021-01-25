import discord
import asyncio
import re
from discord.ext import commands
import math
from functools import reduce
from operator import mul
from fractions import Fraction

def inverse(f):
    return Fraction(f.denominator,f.numerator)

from decimal import Decimal

import logging

logging.basicConfig(level=logging.INFO)

token = os.environ.get('DISCORD_BOT_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('起動しました')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if '。' in message.content:
        return
    if message.content == 'いってきます':
        await message.channel.send('いってら！今日もがんばれ👍')
    if message.content == '勉強する':
        await message.channel.send('了解！勉強がんばれ👍')
    if message.content == 'おはよう' or message.content == 'おはす' or message.content == 'おはやう' or message.content == 'おはすー' or message.content == 'おはょ' or message.content == 'おはよ' or message.content == 'おはよー':
        await message.channel.send('おは！今日も一日がんばれ👍')
    if message.content == 'おやすみ' or message.content == 'おやすみー' or message.content == 'おやす' or message.content == 'おやすー' or message.content == 'good night' or message.content == 'おやすみぃ':
        await message.channel.send('おう！おやすみ！睡眠がんばれ👍')
    if message.content == 'こんにちは' or message.content == 'こんにちはー' or message.content == 'こんちゃ' or message.content == 'こんちゃす' or message.content == 'こんちゃすー' or message.content == 'Hi' or message.content == 'Hello':
        await message.channel.send('こんちゃ！頑張ってるかい？応援するぜ！がんばれ👍')
    if message.content == 'こんばんは' or message.content == 'こんばんはー':
        await message.channel.send('こんばんは！まだ今日は終わってないぞ！がんばれ👍')
    if message.content == 'ただいまー' or message.content == 'ただいま' or message.content == 'おかえり' or message.content == 'おかえりぃ':
        await message.channel.send('おかえりぃ！頑張れたかい？')
    if message.content == 'がんばる' or message.content == '頑張る' or message.content == 'がんばる！' or message.content == '頑張る！' or message.content == 'がんばろう！' or message.content == '頑張ろう！' or message.content == 'がんばろう' or message.content == '頑張ろう' or message.content == 'がんばれ👍':
        await message.channel.send('がんばれ👍！')
    if message.content == 'がんばれ君' :
        await message.channel.send('呼んだ？')
    if 'がんばれ' in message.content:
        await message.channel.send('おう！俺も応援するぜ！がんばれ👍')
    if message.content == 'がんばった' or message.content == 'がんばったよ':
        await message.channel.send('よく頑張った！今後もがんばれ👍')
    if message.content == 'ハハッ！':
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

client.run(token)
