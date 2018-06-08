import discord
from discord.ext.commands import bot
from discord.ext import commands
import random
import asyncio
import time
from threading import Thread
from random import randint
import datetime
import os
import aiohttp
import sys
import traceback
import json
from discord.utils import get



bot = commands.Bot(command_prefix='!')
                                                 
@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='New Koya!! Full Feature'))
    print("BOT ACTIVATED!")
	
@bot.event
async def on_message(message):
    if message.content == "ganteng":
        await bot.send_message(message.channel, 'Iya kamu ganteng.')

 

bot.run ("NDU0NDc3NzAxOTAzMDI0MTM4.DfuA5w.uwEJOROZ4Y1fIvF7-IfoMqQ8Kkk")