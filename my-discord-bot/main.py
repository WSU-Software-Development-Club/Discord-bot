import datetime, logging, os, traceback, typing

import aiohttp, discord
from discord.ext import commands

# Library for .env files. You'll need a .env right beside this script with: BOT_TOKEN="<yourtokenhere>" inside it.
# We should already have it setup so that when you do git commits, you will not accidentally share your .env.
# Regardless, be careful with your bot token and do not put it in the repository.
# If you do, go to https://discord.com/developers/applications and go reset your bot token.
from dotenv import load_dotenv


class WSUBot(commands.Bot):
    client: aiohttp.ClientSession  # NOTE: Not actually in use! Commenting this out lets the bot run so I don't think it's running on HTTP yet.
    _uptime: datetime.datetime = datetime.datetime.now(datetime.UTC)

    def __init__(
        self, prefix: str, ext_dir: str, *args: typing.Any, **kwargs: typing.Any
    ) -> None:
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True
        super().__init__(
            *args,
            **kwargs,
            command_prefix=commands.when_mentioned_or(prefix),
            intents=intents,
        )
        self.logger = logging.getLogger(self.__class__.__name__)
        self.ext_dir = ext_dir
        self.synced = False

    async def _load_extensions(self) -> None:  # Load our 'modules' we make in /cogs.
        if not os.path.isdir(self.ext_dir):
            self.logger.error(f"Extension directory '{self.ext_dir}' does not exist.")
            return
        for filename in os.listdir(self.ext_dir):
            if filename.endswith(".py") and not filename.startswith("_"):
                try:
                    await self.load_extension(
                        f"cogs.{filename[:-3]}"
                    )  # They need to be, for example, `cogs.command_cog`.
                    self.logger.info(f"Loaded extension {filename[:-3]}")
                except commands.ExtensionError:
                    self.logger.error(
                        f"Failed to load extension {filename[:-3]}\n{traceback.format_exc()}"
                    )

    async def on_error(self, event_method, *args, **kwargs) -> None:
        self.logger.exception(
            f"An error occurred in {event_method}.\n{traceback.format_exc()}"
        )

    async def on_ready(self) -> None:
        self.logger.info(f"Logged in as {self.user} (ID: {self.user.id})")

    async def setup_hook(self) -> None:
        self.client = aiohttp.ClientSession()
        await self._load_extensions()
        # if not self.synced:
        #     await self.tree.sync()
        #     self.synced = not self.synced
        #     self.logger.info("Synced command tree.")

    # [IMPORTANT:] These are important for production. Although command_cog has the sync command,
    # that's server-specific and only for live testing commands for development.
    # This section tells Discord globally what commands this bot has, no matter where the bot is, even in DMs.
    # It just takes longer since it's Discord global, making it suboptimal for development.

    async def close(self) -> None:
        await super().close()
        await self.client.close()

    def run(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        load_dotenv()
        try:
            super().run(str(os.getenv("BOT_TOKEN")), *args, **kwargs)
        except (discord.LoginFailure, KeyboardInterrupt):
            self.logger.info("Exiting...")
            exit()

    @property
    def user(self) -> discord.ClientUser:
        assert super().user, "Bot is not ready yet."
        return typing.cast(discord.ClientUser, super().user)

    @property
    def uptime(self) -> datetime.timedelta:
        return datetime.datetime.now(datetime.UTC) - self._uptime


def main() -> None:
    bot = WSUBot(
        prefix="$", ext_dir="my-discord-bot/cogs"
    )  # ext_dir begins at root ie Discord-bot/.
    bot.run()


if (
    __name__ == "__main__"
):  # If supposed to be running main, run our defined main function.
    # Gives us more control over things like exiting main.
    main()
