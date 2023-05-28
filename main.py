import discord
import os
import elo
import json
import random
  
# Opening JSON file
f = open('discordBot.json') 
# returns JSON object as 
# a dictionary
data = json.load(f)
# Closing file
f.close()

'''
# If you are coding the bot on a local machine, use the python-dotenv pakcage to get variables stored in .env file of your project
from dotenv import load_dotenv
load_dotenv()
'''
omedacity = elo.OmedaCityWeb()

intents = discord.Intents.default()
intents.all()
print(intents)

# instantiate discord client
client = discord.Client(intents=intents)


# discord event to check when the bot is online
@client.event
async def on_ready():
  print(f'{client.user} is now online!')


# get bot token from .env and run client
# has to be at the end of the file
#botToken = os.environ['TOKEN']


@client.event
async def on_message(message):
  # make sure bot doesn't respond to it's own messages to avoid infinite loop
  message = await message.channel.fetch_message(message.id)
  print(f'{message.content}')
  if message.author == client.user:
    return
  # lower case message
  #message_content = message.content.lower()

  if message.content.startswith(f'$hello'):
    await message.channel.send(
      "Hello there! I\'m the fidgeting bot from Casual's server")
  if message.content.startswith(f'$darky'):
    about = random.choice(list(data["darky"].items())) 
    messageToSend = (random.choice(about[1]))
    await message.channel.send(messageToSend)
  if message.content.startswith(f'$lezduit'):
    about = random.choice(list(data["lezduit"].items())) 
    messageToSend = (random.choice(about[1]))
    await message.channel.send(messageToSend)
  if message.content.startswith(f'$ridwaano'):
    about = random.choice(list(data["ridwaano"].items())) 
    messageToSend = (random.choice(about[1]))
    await message.channel.send(messageToSend)
  if message.content.startswith(f'$mikey'):
    about = random.choice(list(data["mikey"].items())) 
    messageToSend = (random.choice(about[1]))
    await message.channel.send(messageToSend)
  if message.content.startswith(f'$knives'):
    await message.channel.send("feng mao obssessed lad")
  if message.content.startswith(f'$nilchay'):
    about = random.choice(list(data["nilchay"].items())) 
    messageToSend = (random.choice(about[1]))
    await message.channel.send(messageToSend)
  if message.content.startswith(f'$elodarky'):
    div = omedacity.search('darky1125')
    await message.channel.send(div)  
  if message.content.startswith(f'$elolezduit'):
    div = omedacity.search('lezduit')
    await message.channel.send(div)  
  if message.content.startswith(f'$eloridwaano'):
    div = omedacity.search('Ridwaano')
    await message.channel.send(div)
  if message.content.startswith(f'$eloknives'):
    div = omedacity.search('naughtyknives')
    await message.channel.send(div)
  if message.content.startswith(f'$elomikey'):
    div = omedacity.search('michaeledp')
    await message.channel.send(div)
  if message.content.startswith(f'$elonilchay'):
    div = omedacity.search('nilchay')
    await message.channel.send(div)

client.run(os.getenv('TOKEN'))
