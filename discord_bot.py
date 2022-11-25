import discord
import os
import random
from discord.ext import commands

# CONSTANTS
PLANETS = ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter",
           "Saturn", "Uranus", "Neptune", "Pluto", "Fortune", "Chiron",
           "North-Node", "Vertex"]
SIGNS = ["Ares", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra",
         "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
TOKEN = os.getenv('BOT_TOKEN')
GUILD = os.getenv('GUILD_NAME')
INTENTS = discord.Intents.all()


# Bot commands that are prefixed with !
bot = commands.Bot(command_prefix='!', intents=INTENTS)
@bot.command(name='ascendant', help="Generate the Ascendant pair of House/Degree.")
async def get_ascendant(ctx):
    house = random.choice(SIGNS)
    ascendant = random.choice(range(1, 31))
    response = f"House:   {house}\nAscendant:   {ascendant}"
    await ctx.send(response)


@bot.command(name='planets', help="Generate Ascendant/Degree pair for all planets.")
async def run_planets(ctx):
    response = ""
    for planet in PLANETS:
        degree = random.choice(range(0, 30))
        sign = random.choice(SIGNS)
        pair = f"{planet}:   {sign}  /    {degree}\n"
        response += pair
    await ctx.send(response)


@bot.command(name='thanksgiving', help="It's Thanksgiving!")
async def thanksgiving(ctx):
    response = "🎉 🦃 🍗 🍖 🥧 ✨ 🍗 🦃 🎉"
    await ctx.send(response)


# Using this on_message func prevents the other bot commands from working.
# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return
#     if message.content == "apple":
#         response = "🍎🍎🍎🍎🍎"
#         await message.channel.send(response)

# Function calls when bot joins server
@bot.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, bot.guilds)
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    print("Guild Members: ")
    for member in guild.members:
        print(member.name)


# Run the bot
bot.run(TOKEN)
