import discord
import os
import elo
import json
import random
from dotenv import load_dotenv


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
    embed = discord.Embed(
      colour=discord.Colour.random(),
      description="Hello there! I\'m the fidgeting bot from Casual's server",
      title="ELO Bot")
    await message.channel.send(embed=embed)

  if message.content.startswith(f'$darky'):
    about = random.choice(list(data["darky"].items()))
    messageToSend = (random.choice(about[1]))
    embed = discord.Embed(colour=discord.Colour.random(),
                          description=messageToSend,
                          title="Darky's " + about[0])
    embed.set_author(
      name="Darky aka Naif",
      url="https://omeda.city/players/283b6f54-3f1a-45ac-aa53-b3710b818f14")
    await message.channel.send(embed=embed)

  if message.content.startswith(f'$lezduit'):
    about = random.choice(list(data["lezduit"].items()))
    messageToSend = (random.choice(about[1]))
    embed = discord.Embed(colour=discord.Colour.random(),
                          description=messageToSend,
                          title="Lezduit's " + about[0])
    embed.set_author(
      name="Lezduit aka Yousef",
      url="https://omeda.city/players/efeba818-1e50-4867-8889-09f961c17671")
    await message.channel.send(embed=embed)

  if message.content.startswith(f'$ridwaano'):
    about = random.choice(list(data["ridwaano"].items()))
    messageToSend = (random.choice(about[1]))
    embed = discord.Embed(colour=discord.Colour.random(),
                          description=messageToSend,
                          title="Ridwaano's " + about[0])
    embed.set_author(
      name="Ridwaano aka Steel",
      url="https://omeda.city/players/d4a83e7d-659e-4f9d-958a-054696da8771")
    await message.channel.send(embed=embed)

  if message.content.startswith(f'$mikey'):
    about = random.choice(list(data["mikey"].items()))
    messageToSend = (random.choice(about[1]))
    embed = discord.Embed(colour=discord.Colour.random(),
                          description=messageToSend,
                          title="Mikey's " + about[0])
    embed.set_author(
      name="Mikey aka Michael E DP",
      url="https://omeda.city/players/761ae8a5-e4c2-4ac6-9a24-2b976ae435b0")
    await message.channel.send(embed=embed)
  if message.content.startswith(f'$knives'):
    await message.channel.send("feng mao obssessed lad")

  if message.content.startswith(f'$nilchay'):
    about = random.choice(list(data["nilchay"].items()))
    messageToSend = (random.choice(about[1]))
    embed = discord.Embed(colour=discord.Colour.random(),
                          description=messageToSend,
                          title="Nilchay's " + about[0])
    embed.set_author(
      name="Nilchay aka Crunch",
      url="https://omeda.city/players/5146b439-a586-4bd8-8354-a92ba1708681")
    await message.channel.send(embed=embed)

  if message.content.startswith(f'$elodarky'):
    div = omedacity.search('darky1125')
    embed = discord.Embed(colour=discord.Colour.random(),
                          description=div,
                          title="Darky's Elo")
    embed.set_author(
      name="Darky aka Naif",
      url="https://omeda.city/players/283b6f54-3f1a-45ac-aa53-b3710b818f14")
    await message.channel.send(embed=embed)

  if message.content.startswith(f'$elolezduit'):
    div = omedacity.search('lezduit')
    embed = discord.Embed(colour=discord.Colour.random(),
                          description=div,
                          title="Lezduit's Elo")
    embed.set_author(
      name="Lezduit aka Yousef",
      url="https://omeda.city/players/efeba818-1e50-4867-8889-09f961c17671")
    await message.channel.send(embed=embed)

  if message.content.startswith(f'$eloridwaano'):
    div = omedacity.search('Ridwaano')
    embed = discord.Embed(colour=discord.Colour.random(),
                          description=div,
                          title="Ridwaano's Elo")
    embed.set_author(
      name="Ridwaano aka Steel",
      url="https://omeda.city/players/d4a83e7d-659e-4f9d-958a-054696da8771")
    await message.channel.send(embed=embed)

  if message.content.startswith(f'$eloknives'):
    div = omedacity.search('naughtyknives')
    await message.channel.send(div)

  if message.content.startswith(f'$elomikey'):
    div = omedacity.search('michaeledp')
    embed = discord.Embed(colour=discord.Colour.random(),
                          description=div,
                          title="Mikey's Elo")
    embed.set_author(
      name="Mikey aka Michael E DP",
      url="https://omeda.city/players/761ae8a5-e4c2-4ac6-9a24-2b976ae435b0")
    await message.channel.send(embed=embed)

  if message.content.startswith(f'$elonilchay'):
    div = omedacity.search('nilchay')
    embed = discord.Embed(colour=discord.Colour.random(),
                          description=div,
                          title="Nilchay's Elo")
    embed.set_author(
      name="Nilchay aka Crunch",
      url="https://omeda.city/players/5146b439-a586-4bd8-8354-a92ba1708681")
    await message.channel.send(embed=embed)

  if message.content.startswith(f'$elowesamsous'):
    div = omedacity.search('wesamsous')
    embed = discord.Embed(colour=discord.Colour.random(),
                          description=div,
                          title="Wesamsous's Elo")
    embed.set_author(
      name="Wesamsous",
      url="https://omeda.city/players/8647f25d-b864-4aad-ae9c-bc8782613d38")
    await message.channel.send(embed=embed)

load_dotenv()
client.run(os.getenv('TOKEN'))
