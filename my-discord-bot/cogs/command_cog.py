import discord
from discord import app_commands
from discord.ext import commands

class CommandCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="supersecret")
    async def supersecret(self, ctx: commands.Context) -> None:
        await ctx.message.delete()
        if hasattr(self, "spoilsport") and self.spoilsport is ctx.author.id:
            await ctx.send("Now you're just doing it on purpose...")
        else:
            await ctx.send("Shhhh!!! You're going to spoil the secret!")
            self.spoilsport = ctx.author.id

    @app_commands.command(name="hello", description="Say hello to our new friend! If you value your soul.")
    async def hello(self, integration: discord.Integration) -> None:
        await integration.response.send_message("Hello!")

    @commands.hybrid_command(name="sync", description="Sync commands to your guild.")
    async def sync(self, ctx: commands.Context) -> None:
        if ctx.guild is None:
            ctx.send("This command is only for server slash-command syncing.")
            return

        await ctx.defer(ephemeral=True)

        self.bot.tree.copy_global_to(guild=ctx.guild)
        synced = await self.bot.tree.sync(guild=ctx.guild)

        await ctx.send(f"Synced {len(synced)} command(s).", ephemeral=True)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(CommandCog(bot))