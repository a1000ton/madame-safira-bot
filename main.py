import os
import discord
from random import randrange
from api import keep_alive

client = discord.Client()
bot_key = os.environ['bot_key']

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$madame'):
    card = check_card()

    await message.channel.send("Vamos olhar suas cartas, " + message.author.name + "...")

    with open('tarot_' + card + '.jpeg', 'rb') as f:
      picture = discord.File(f)
    await message.channel.send(file=picture)

    if card == 'fool':
      await message.channel.send("kkkkk.... é o troxa....")
    elif message.author.name == "Rodrigo Harkuna":
      await message.channel.send("Harkuna..... inevitável....")
    else:
      await message.channel.send("putz.... é morte então....")
      

def check_card():
  num = randrange(10)
  if num < 1:
    return "fool"
  else:
    return "death"

keep_alive()
client.run(bot_key)