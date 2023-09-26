import discord
import asyncio
import re
import os
from discord.ext import commands
from discord.ext import tasks
import math
from functools import reduce
from fractions import Fraction
from datetime import datetime
import time
import random
import sys
import json
import urllib
from discord_slash import SlashCommand, SlashContext
from dislash import slash_commands, Option, OptionType

bot = discord.Bot(
        intents=discord.Intents.all(), 
        activity=discord.Game("JPSをプレイ中"),
)

Notification_list = []

@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    if message.content == 'hello':
        await message.reply("Hello!")

@bot.command(name = "Register", discription = "告知メッセージの登録")
async def register(ctx: discord.ApplicationContext, Content: str):
    Notification_list.append(Content)
    await ctx.respond("告知メッセージの登録完了")
    NOW = datetime.now().strftime('%H%M%S')
    while Notification_list:
        if NOW == "103000":
            await ctx.respond(Notification_list.pop(0))

@bot.command(name = "list", discription = "告知メッセージのリストを確認")
async def list(ctx: discord.ApplicationContext):
    await ctx.respond(Notification_list)

@bot.command(name = "delete", discription = "最後に登録された告知メッセージの削除")
async def delete(ctx :discord.ApplicationContext):
    del Notification_list[-1]
    await ctx.respond(f'{int(len(Notification_list)) + 1}番目の告知メッセージを削除')



bot.run(token)
