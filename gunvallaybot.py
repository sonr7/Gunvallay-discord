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
import collections
from discord_slash import SlashCommand, SlashContext
from dislash import slash_commands, Option, OptionType

Notification_list = []

@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    if message.content == 'hello':
        await message.reply("Hello!")

@bot.command(name = "Register", discription = "告知メッセージの登録")
async def register(ctx: discord.ApplicationContext, Content: str):
    Notifivation_list.append(str)
    await ctx.respond("告知メッセージの登録完了")
    
    
                                                                                             
                                               
            


                                               
        
            
            
                                             
                                             
        
       
                   

client.run(token)
clients.run(token)
