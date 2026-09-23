# Discord-bot
The goal of this project is to teach beginner-level programmers how to work on a group project repository and learn basic CS applications and tools. In this project specifically, we will be designing a Discord bot with various applications for the WSU Software Development Club Discord. 

## Setting Up Your Test Bot
### 1. Create the Bot
Before testing your bot code, you need a bot registered with Discord
- Go to the *Discord Developer Portal*. (https://discord.com/developers/applications)
- Click *New Application* in the top right, name your bot, and click *Create*.
- On the left menu, click *Bot*.
- Click Reset Token and copy the long string of characters. Keep this token secret. It is your bot’s password.
- Scroll down on the same page to *Privileged Gateway Intents*. Turn on *Presence Intent*, *Server Members Intent*, and *Message Content Intent*. Click *Save Changes*
### 2. Invite the Bot to Your Server
- While still in the Developer Portal, go to the *OAuth2* tab on the left menu, then select *URL Generator*.
- Under *Scopes*, check the box for *bot*.
- Under *Bot Permissions*, select the permissions your bot needs (e.g., Send Messages, Read Message History).
- Copy the generated URL at the bottom of the page. Paste it into your browser, choose your server, and authorize the bot.

## Installing Python
### Windows Python Install
- Go to the Official Python Downloads Page using your web browser.
- Click the download button for the latest Python 3 version to get the .exe installer file.
- Open your downloads folder and double-click the installer file to start the setup.
- Check the box at the bottom that says *Add python.exe to PATH*. (Adds Python to the system environment variables enabling `python` as a command.)
- Click Install Now and wait for the process to finish.
Unlike Linux, pip and venv are bundled with your Python install(s).

### Linux Python Install
By the nature of Linux, this will vary greatly from distribution or more importantly your package manager. 
This example is Debian/Ubuntu.
- Update Your Package Manager

```sudo apt update && sudo apt upgrade -y```
- Install Python 3, pip, and virtual environment utilities

```sudo apt install python3 python3-pip python3-venv -y```
- Start the Bot

```python bot.py```
