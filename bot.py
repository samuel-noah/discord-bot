from http import client
import discord
import random

//insert your own token 

TOKEN =""

client = discord.Client()

@client.event 
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')


    if message.author == client.user:
        return
    
    if message.channel == 'general':
        if user_message.lower() == '!hello':
            await message.channel.send(f'Hello{username}!')
            return
        elif user_message.lower() == '!help':
            await message.channel.send('!hello - say hello\n!roll - roll a dice\n!flip - flip a coin\n!choose - choose between two options\n!8ball - ask the magic 8ball a question')
            return
        elif user_message.lower() == '!roll':
            await message.channel.send(random.randint(1,6))
            return
        elif user_message.lower() == '!flip':
            await message.channel.send(random.choice(['heads', 'tails']))
            return
        elif user_message.lower() == '!choose':
            await message.channel.send(random.choice(['option 1', 'option 2']))
            return

    if user_message.lower() == '!anywhere':
        await message.channel.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        return 


        
client.run(TOKEN)
