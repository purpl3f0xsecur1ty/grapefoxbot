import random
import time
import discord

from discord.ext import commands

description = 'Test Bot'
bot_prefix = 'fox!'

client = commands.Bot(description=description, command_prefix=bot_prefix)

# Reactions for the magicball command
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

# Prints info to the command line
# Verifies successful connection to Discord
@client.event
async def on_ready():
    print('Logged in')
    print('Name : {}'.format(client.user.name))
    print('ID : {}'.format(client.user.id))
    print(discord.__version__)
    for server in client.servers:  # List connected servers
        print('Joined: {}'.format(server.name))


#Commands starting with fox! go here

@client.command(pass_context=True)
async def info(ctx):
    await client.say("I am grape fox!\n"
                     "Author: **Zepher-Tensho**\n"
                     "Written in **Python 3.6**\n"
                     "For a list of current commands type `!commands`"
                     "Note: This bot is experimental and is often offline.")

@client.command(pass_context=True)
async def boop(ctx):
    await client.say('*Sneezes*')

@client.command(pass_context=True)
async def commands(ctx):
    await client.say("Current commands:\n"
                     "fox!info - Prints info about the bot\n"
                     "fox!boop - Boop the snoot!\n"
                     "fox!dice - Roll between 1 and 6 grapes~!\n"
                     "fox!magicball - Ask the grape foxy a question~\n"
                     "Say `Come here grape foxy!` if you want grapes!\n")

@client.command(pass_context=True)
async def dice(ctx):
    dice = random.randint(1,12)
    if dice == 1:
        await client.say("Grape foxy drops " + str(dice) + " grape")
    else:
        await client.say("Grape foxy drops " + str(dice) + " grapes")

@client.command(pass_context=True)
async def magicball(ctx):
    await client.say("🍇*Shaking magic tail...*✨")
    time.sleep(1)
    await client.say("🍇*Wiggling nose...*🦊")
    time.sleep(1)
    await client.say("🍇*Checking grapes...*🍇")
    time.sleep(2)
    await client.say(random.choice(choices))

#Checks for a string and reacts
@client.event
async def on_message(message):
    
    if "grape" in message.content.lower():
        await client.add_reaction(message, "🍇")

    if "fox" in message.content.lower():
        await client.add_reaction(message, "🦊")
    await client.process_commands(message) # Without this command the bot will not carry out any commands!!

# Token for bot login
# Note that this line must come LAST!
client.run('YOUR TOKEN HERE')
