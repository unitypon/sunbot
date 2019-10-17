# sunbot.py
import requests

from discord.ext import commands
from markovchain.text import MarkovText

bot = commands.Bot(command_prefix='!')
token = open("key").read()


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command(name='markov', help='Generates a Markov chain based on a FimFiction story')
async def markov(ctx, id):
    url = "https://www.fimfiction.net/story/download/" + id + "/txt"
    markovgenerate = MarkovText()
    print('Getting story with id ${0}...'.format(id))
    markovgenerate.data(requests.get(url).content.decode(encoding="UTF-8"))
    print('Story received.')
    response = markovgenerate(max_length=5000)
    print('Markov chain response generated.')
    await ctx.send(response)


@bot.event
async def on_member_join(member):
    print('Member ${0} joined'.format(member))
    guild = member.guild
    if guild.system_channel is not None:
        to_send = '{0.mention}, I\'ll show you who\'s boss of this gym'.format(member)
        await guild.system_channel.send(to_send)


bot.run(token)
