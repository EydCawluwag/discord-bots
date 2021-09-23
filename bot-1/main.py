import os
import discord 
import requests
import json
import dotenv
from replit import db
import random

sad_words = ['sad',
  'depressed',
  'unhappy',
  'angry',
  'depressing',
  'miserable'
]

starter_encourage=[
  'Cheer up',
  'Cheer up! bitch',
  'bitch',
  'emo',
  'hang in ther'
]

client = discord.Client()
dotenv.load_dotenv()

def get_quote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data=json.loads(response.text)
  quote=json_data[0]['q'] + ' \n-'+json_data[0]['a']+'-'
  return quote

def update_encouragements(message):
  if 'encouragements' in db.keys():
    db['encouragements']=db['encouragements'].append(message)
  else:
    db['encouragements']=[message]

def delete_encouragement(ind):
  enc=db['encouragements']
  if len(enc)>ind:
    del enc[ind]
    db['encouragements']=enc

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user: return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello bitch')
  if message.content.startswith('$how r u bitch'):
    await message.channel.send('im good bitch! how bout u!?')
  if message.content.startswith('$shutup'):
    await message.channel.send('duh, you shut up! im busy, tsk')
  if message.content.startswith('$inspire'):
    await message.channel.send(get_quote())
  msg=message.content
  
  options=['u can do it!'] + starter_encourage

  if 'encouragements' in db.keys():
    options+=db['encouragements']

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(options))

  if message.content.startswith('$new'):
    enc=msg.split('$new ',1)[1]
    update_encouragements(enc)
    await message.channel.send('new encouraging message... added  \n thank u \n bitch')

  if message.content.startswith('$del'):
    enc=[]
    if 'encouragements' in db.keys():
      ind = msg.split('$del',1)[1]
      delete_encouragement(ind)
      enc = db['encouragements']
    await message.channel.send('new encouraging message... added \n thank u \n bitch')
  

client.run(os.getenv('myBotToken'))