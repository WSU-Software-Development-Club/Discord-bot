# Discord Bot

A minimal Python (discord.py) bot, containerized with Docker.

## Setup

1. Create a bot at https://discord.com/developers/applications and copy its token.
2. Enable **Message Content Intent** under the bot's settings.
3. `cp .env.example .env` and paste your token into `.env`.

## Run with Docker Compose

```bash
docker compose up -d --build
docker compose logs -f
```

## Run with plain Docker

```bash
docker build -t discord-bot .
docker run -d --name discord-bot --env-file .env --restart unless-stopped discord-bot
```

## Run locally (no Docker)

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python bot.py
```

## Commands

- `!ping` – replies with latency
- `/hello` – slash command greeting

## GitHub notes

- `.env` is git-ignored, so your token is never pushed. Only `.env.example` is committed.
- The included workflow builds the image on every push and publishes it to
  `ghcr.io/<your-user>/<repo>:latest` from `main`.
- If your token ever leaks, reset it in the Developer Portal immediately.
