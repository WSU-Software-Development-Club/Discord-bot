import logging
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()  # loads .env locally; in Docker the env vars are passed in directly

TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise SystemExit("DISCORD_TOKEN is not set. Copy .env.example to .env and add your token.")

intents = discord.Intents.default()
intents.message_content = True  # enable this in the Developer Portal too

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    await bot.tree.sync()  # register slash commands
    logging.info("Logged in as %s (ID: %s)", bot.user, bot.user.id)


@bot.command(name="ping")
async def ping(ctx: commands.Context):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")


@bot.tree.command(name="hello", description="Say hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello, {interaction.user.mention}!")


if __name__ == "__main__":
    bot.run(TOKEN, log_level=logging.INFO)
