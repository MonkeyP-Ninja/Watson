import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='-')


@bot.command()
async def join(ctx, arg):
    if ctx.author.voice is None:
        await ctx.send('pls connect to a voice channel')

    else:
        i = 0
        for x in bot.voice_clients:
            if x.is_connected:
                i = 1
                await x.move_to(ctx.author.voice.channel)
                break
        if i == 0:
            await ctx.author.voice.channel.connect()


@bot.command()
async def leave(ctx):
    for x in bot.voice_clients:
        if x.is_connected():
            await x.disconnect()
            break


@bot.command()
async def play(ctx):
    source = 'audio/test.mp3'
    for x in bot.voice_clients:
        if x.is_connected():
            x.play(discord.FFmpegPCMAudio(source), after=None)
            break


@bot.command()
async def test(ctx):
    await play(ctx)


@bot.command()
async def tts(ctx):
    await ctx.send(ctx.message.content[4:], tts=True)


bot.run('OTI3ODY2MjM0NDEyODkyMTYw.YdQcxQ.Zn-XHPjoZVpkjbNF9fmtemsgrt0')
