import discord
import os
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="KudlimiCraft"))
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('vote'):
        await message.channel.send('**Votuj pro nas server zde:**\nhttps://minecraftpocket-servers.com/server/110325/vote/')

    if message.content.startswith('ip'):
        await message.channel.send('***IP:*** **168.119.146.55**\n***PORT:*** **19126**')

    if message.content.startswith('serverstatus'):
        await message.channel.send('Server status zatim **neni** podporovan.')

    if message.content.startswith('kudlimicraftblbost'):
        await client.change_presence(activity=discord.Game(name="KudlimiCraft je sracka"))
        await message.channel.send('**Koukni se na status bota :D**')

    if message.content.startswith('kc'):
        await client.change_presence(activity=discord.Game(name="KudlimiCraft"))
        await message.channel.send('**...**')

keep_alive()
client.run(os.getenv('TOKEN'))
