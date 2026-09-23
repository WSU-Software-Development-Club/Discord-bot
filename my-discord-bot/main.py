import discord, os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'), intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

@bot.tree.command()
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hello {interaction.user.name}!')

bot.run(BOT_TOKEN)