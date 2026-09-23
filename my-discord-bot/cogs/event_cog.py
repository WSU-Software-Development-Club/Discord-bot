import discord
from discord.ext import commands


class EventCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        if message.author.bot:
            return

        # Catches prefix-initiated commands. I think.
        await self.bot.process_commands(message)

        if "swear" in message.content.lower():
            await message.channel.send("Hey, you can't say the swear word.")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(EventCog(bot))