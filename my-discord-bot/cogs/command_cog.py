import discord
from discord import app_commands
from discord.ext import commands

class CommandCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    # Primarily here to demonstrate prefix-only commands. This command only works with `$supersecret` or `@<botname> supersecret` 
    # and doesn't appear as a slash-command, hence the premise of it being the supersecret.
    @commands.command(name="supersecret")
    async def supersecret(self, ctx: commands.Context) -> None:
        await ctx.message.delete()
        if hasattr(self, "spoilsport") and self.spoilsport is ctx.author.id:
            await ctx.send("Now you're just doing it on purpose...")
        else:
            await ctx.send("Shhhh!!! You're going to spoil the secret!")
            self.spoilsport = ctx.author.id

    # A basic example command. This is a slash-only command where `/hello` gets you the response "Hello!"
    @app_commands.command(name="hello", description="Say hello to our new friend! If you value your soul.")
    async def hello(self, integration: discord.Integration) -> None:
        await integration.response.send_message("Hello!")

    # Hybrid commands combine the two above things. They're not longer to make, it just happens that
    # this command is actually made for something important whilst demonstrating hybrid commands.
    @commands.hybrid_command(name="sync", description="Sync commands to your guild.")
    async def sync(self, ctx: commands.Context) -> None:
    # Specifically, this command can be called with `$sync`, `@<botname> sync`, and `/sync`. The command takes all
    # of our defined commands we've made, which discord.ext commands library tracks, and it tells the
    # guild which `sync` is called from that we want to deploy our created commands into the guild instance of the bot.
    # This ALSO requires that you set up commands permissions for the bot. In the Dev Portal under Installation,
    # add application.commands to Guild Install Scopes and Use Slash Commands in Guild Install Permissions. 
        if ctx.guild is None:
            ctx.send("This command is only for server slash-command syncing.")
            return

        await ctx.defer(ephemeral=True)

        self.bot.tree.copy_global_to(guild=ctx.guild)
        synced = await self.bot.tree.sync(guild=ctx.guild)

        await ctx.send(f"Synced {len(synced)} command(s).", ephemeral=True)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(CommandCog(bot))