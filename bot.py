import discord
import responses
import os
from keep_alive import keep_alive

async def send_message(message, user_message, is_private):
  try:
    response = responses.handle_response(user_message)
    await message.channel.send(response)
    #await message.author.send(response) if is_private else await message.channel.send(response)

  except Exception as e:
    print(e)
    
intentz = discord.Intents.default()
intentz.message_content = True
client = discord.Client(intents=intentz)

@client.event
async def on_ready():
    print('is now running')

@client.event
async def on_message(message):
  # Make sure bot doesn't get stuck in an infinite loop
  if message.author == client.user:
      return

  # Get data about the user
  username = str(message.author)
  user_message = str(message.content)
  channel = str(message.channel)

  # Debug printing
  print(f"{username} said: '{user_message}' ({channel})")

    # If the user message contains a '?' in front of the text, it becomes a private message
  
  await send_message(message, user_message, is_private=False) 


TOKEN = os.environ['TOKEN']
# Remember to run your bot with your personal TOKEN
def run_discord_bot():
  keep_alive()
  client.run(TOKEN)