import os
import discord 
import requests
import json
import dotenv

client = discord.Client()
dotenv.load_dotenv()

def get_quote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data=json.loads(response.text)
  quote=json_data[0]['q'] + ' \n-'+json_data[0]['a']+'-'
  return quote

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

client.run(os.getenv('myBotToken'))