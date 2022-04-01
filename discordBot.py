import discord
import os
import json
import requests


client = discord.Client()


@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-'):
        text = message.content.replace("- ", "")
        await message.channel.send(text)



client.run('OTI3ODY2MjM0NDEyODkyMTYw.YdQcxQ.Zn-XHPjoZVpkjbNF9fmtemsgrt0')
