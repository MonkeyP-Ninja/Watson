import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='-')


@bot.command()
async def join(ctx, arg):
    if ctx.author.voice is None:
        await ctx.send('pls connect to a voice channel')

    if ctx.author.voice != None and bot.voice_clients.count(ctx.author.voice.channel) == 0:
        voice_channel = ctx.author.voice.channel
        await voice_channel.connect()
    else:
        voice_channel = ctx.author.voice.channel
        await voice_channel.move_to(voice_channel)


bot.run('OTI3ODY2MjM0NDEyODkyMTYw.YdQcxQ.Zn-XHPjoZVpkjbNF9fmtemsgrt0')
