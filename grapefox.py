# Import the required libraries

import random
import time
import discord

from discord.ext import commands

description = 'Test Bot'
bot_prefix = 'fox!'

client = commands.Bot(description=description, command_prefix=bot_prefix, help_command=None)

# String arrays for reactions
gay_strings = ['gay', 'thats gay', 'that\'s gay','you\'re gay']
choices = [
    "💜**Definitely!**💜",
    "🦊**Maybe**🦊",
    "🚫**No**🚫",
    "❔**I don't know**🦊",
    "⛔**Never**⛔",
    "🍇**Grapes**🍇",
    "🔥**Hell no**🛑",
    "🍇**Fuck yea!**🦊",
    "🕳*Fox stuck in hole, try again later*🦊",
    "👍**Very likely~**🦊",
    "💖**Oh yea baby~**✨",
    "🛑**I don't think so**🛑"
]

# Array for fact command
facts = [
    "Foxes are without a doubt the sneakiest little fuckers in the entire animal kingdom.",
    "Foxes skulk around doing all kinds of dodgy shit far more than any other species.",
    "Foxes are quick to recognize lewdness.",
    "A female fox is called a vixen, and a male fox is called a dog fox or a tod.",
    "Foxes are loners except during mating season.",
    "Like cats, foxes are most active at night, and their eyes narrow into vertical slits.",
    "Foxes harness the earth's magnetic field to hunt.",
    "Foxes are good parents, caring for their pups for 7 months and going to great lengths to protect them.",
    "Having pet foxes is legal in certain states, some of which require permits.",
    "Arctic foxes don't feel cold until -94F/-70C.",
    "Foxes make 40 different sounds, the most startling of which is its scream.",
    "Foxes have understood the universe for many years.",
    "Foxes eat nothing but grapes.🍇",
    "Foxes will inherit the earth after puny fur-less humans die off in the next ice age.",
    "Foxes are not amused by 'What Does The Fox Say' so don't make that joke around them.",
    "Foxes are prone to pinching the booty.",
    "Foxes will drink your pepsi and call you a bitch.",
    "Foxes fancy the color purple the most."
]

# Prints info to the command line
# Verifies successful connection to Discord

@client.event
async def on_ready():
    print('Logged in')
    print('Name : {}'.format(client.user.name))
    print('ID : {}'.format(client.user.id))
    print(discord.__version__)
    for guild in client.guilds:  # List connected servers
        print('Joined: {}'.format(guild.name))


# Commands starting with fox! go here

@client.command(pass_context=True)
async def info(ctx):
    await ctx.send("I am grape fox!\n"
                     "Author: **Zephy FOxy**\n"
                     "Written in **Python 3.6**\n"
                     "For a list of current commands type `!commands`"
                     "Note: This bot is experimental and is often offline.")

@client.command(pass_context=True)
async def boop(ctx):
    await ctx.send('*Sneezes*')

@client.command(pass_context=True)
async def program(ctx):
    await ctx.send('Program me daddy uwu')

@client.command(pass_context=True)
async def commands(ctx):
    await ctx.send("Current commands:\n"
                     "fox!info - Prints info about the bot\n"
                     "fox!boop - Boop the snoot!\n"
                     "fox!dice - Roll between 1 and 6 grapes~!\n"
                     "fox!magicball - Ask the grape foxy a question~\n"
                     "fox!fact - Random facts about foxes.")

@client.command(pass_context=True)
async def dice(ctx):
    dice = random.randint(1,12)
    if dice == 1:
        await ctx.send("Grape foxy drops " + str(dice) + " grape")
    else:
        await ctx.send("Grape foxy drops " + str(dice) + " grapes")

@client.command(pass_context=True)
async def fact(ctx):
    await ctx.send(random.choice(facts))

@client.command(pass_context=True)
async def magicball(ctx):
    await ctx.send("🍇*Shaking magic tail...*✨")
    time.sleep(1)
    await ctx.send("🍇*Wiggling nose...*🦊")
    time.sleep(1)
    await ctx.send("🍇*Checking grapes...*🍇")
    time.sleep(1)
    await ctx.send(random.choice(choices))

# Checks for a string and reacts
@client.event
async def on_message(message):

    if message.content.lower() in gay_strings:
        await message.add_reaction('🌈')

    if "grape" in message.content.lower():
        await message.add_reaction("🍇")

    if "fox" in message.content.lower():
        await message.add_reaction("🦊")

    if "mika" in message.content.lower():
        await message.add_reaction("💜")

    await client.process_commands(message) # Without this command, no other commands will be processed!

client.run()
