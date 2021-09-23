import os
import discord 
import requests
import json
import dotenv
import random


client = discord.Client()
dotenv.load_dotenv()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user: return

  if message.content.startswith('angkol help'):
    await message.channel.send('''
          Oh! Unsa may matabang nako?\nKabalo ko mo Trigonometry:\n   basic:\n    `?sin opposite hypotenuse`, `?cos adjacent hypotenuse`, `?tan opposite adjacent`,\n    `?sec hypotenuse adjacent`, `?cosec hypotenuse opposite`, `?cot adjacent opposite`
    '''+'\n   Reciprocal Identities: `angkol help reciprocal identities`\n   Trigonometry Table: `angkol trig table`\n   Periodicity Identities (in Radians): `angkol periodicity id r`\n   Periodicity Identities (in Degrees): `angkol periodicity id d`'+
    '\n   Co-function Identities (in Degrees): `angkol co func id d`,\n   Co-function Identities (in Radians): `angkol co func id r`\n   Sum & Difference Identities: `angkol sum diff id`\n   Double Angle Identities: `angkol dob ang id`\n   Triple Angle Identities: `angkol trip ang id`\n   Half Angle Identities: `angkol half ang id`\n   Product identities: `angkol prod id`\n   Sum to Product Identities: `sumtoprod id`\n   Inverse Trigonometry Formulas: `inv trig formulas`'
    )
  
  

client.run(os.getenv('myBotToken'))