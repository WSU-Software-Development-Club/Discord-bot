# Discord-bot
the goal of this project is to teach beginner level programmer how to work on a group project an learn basic CS applications and tools. In this project specifically we will be designing discord bots with various applications. 

# Step 1: Create Your Bot on the Discord Portal
Before writing code, you need to register your bot with Discord
- Go to the *Discord Developer Portal*. (https://discord.com/developers/applications)
- Click *New Application* in the top right, name your bot, and click *Create*.
- On the left menu, click *Bot*.
- Click Reset Token and copy the long string of characters. Keep this token secret—it is your bot’s password.
- Scroll down on the same page to *Privileged Gateway Intents*. Turn on *Presence Intent*, *Server Members Intent*, and *Message Content Intent*. Click *Save Changes*

# Step 2: Invite the Bot to Your Server
- While still in the Developer Portal, go to the *OAuth2* tab on the left menu, then select *URL Generator*.
- Under *Scopes*, check the box for *bot*.
- Under *Bot Permissions*, select the permissions your bot needs (e.g., Send Messages, Read Message History).
- Copy the generated URL at the bottom of the page. Paste it into your browser, choose your server, and authorize the bot.

# Start the Bot: 
- python bot.py