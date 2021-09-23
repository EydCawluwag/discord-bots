import os
import discord 
import requests
import json
import dotenv
import random
from help import helps
from functions import driver

client = discord.Client()
dotenv.load_dotenv()
trig = '?sin ?cos ?tan ?sec ?cosec ?cot'.split(' ')

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user: return
  msg=message.content.split(' ')
  # print(msg)
  if 'help' in msg and 'angkol' in msg:
    if len(msg)==2: 
      await message.channel.send('ang commands sa trigonometry kay naa diri: `angkol help trig`')
    elif msg[2]=='trig': 
      await message.channel.send(helps.trigonometry()) 
  if msg[0].startswith('?') and msg[0] in trig:
    await message.channel.send('```'+str(driver(msg))+' '+ msg[1]+'/'+msg[2]+'```')
  
  

client.run(os.getenv('myBotToken'))