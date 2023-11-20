import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_message(message):
    if message.content == "p!play low rider":
        try:
            await message.author.ban(reason="Prohibited phrase used")
            await message.channel.send(f"{message.author} has been violently dragged into the accursed forest")
        except discord.Forbidden:
            await message.channel.send("I do not have permissions to ban this user")
    elif message.content == "p!play lowrider":
        try:
            await message.author.ban(reason="Prohibited phrase used")
            await message.channel.send(f"{message.author} has been violently dragged into the accursed forest")
        except discord.Forbidden:
            await message.channel.send("I do not have permissions to ban this user")
    else:
        await bot.process_commands(message)

bot.run('Your_Token_Here...')