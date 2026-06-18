# MyFirstTGBot

A working Telegram bot built with **python-telegram-bot v21** (async).
Supports commands, an inline keyboard menu, and a simple echo handler.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat&logo=python&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram%20Bot-API-2CA5E0?style=flat&logo=telegram&logoColor=white)

---

## Features

| Command | What it does |
|---------|-------------|
| `/start` | Welcome message with the user's first name |
| `/help` | List of all available commands |
| `/about` | Info about the bot and a link to the source |
| `/roll` | Roll a six-sided die 🎲 |
| `/menu` | Open an inline keyboard with quick-action buttons |
| _(any text)_ | Echo the message back |

The inline `/menu` keyboard lets users roll the die, view the about text, or
read the help — without typing commands.

---

## Project structure

```
MyFirstTGBot/
├── bot/
│   ├── __init__.py
│   ├── app.py          # application factory (registers all handlers)
│   ├── config.py       # reads BOT_TOKEN from the environment
│   └── handlers/
│       ├── __init__.py
│       ├── core.py     # /start, /help, /about
│       ├── fun.py      # /roll, /menu, inline keyboard callbacks
│       └── echo.py     # plain-text echo handler
├── main.py             # entry point
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## Setup

### 1. Get a bot token

Open Telegram, start a chat with [@BotFather](https://t.me/BotFather), and
run `/newbot`. Copy the token it gives you.

### 2. Clone and create a virtual environment

```bash
git clone https://github.com/Adilforest/MyFirstTGBot.git
cd MyFirstTGBot

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set the bot token

**Option A — `.env` file (recommended for local development):**

```bash
cp .env.example .env
# open .env and fill in your token:
# BOT_TOKEN=123456:ABC-...
```

**Option B — environment variable:**

```bash
export BOT_TOKEN="123456:ABC-..."
```

> `.env` is listed in `.gitignore` and will never be committed.

### 5. Run

```bash
python main.py
```

The bot starts polling Telegram and logs activity to stdout. Stop it with
**Ctrl-C**.

---

## Requirements

- Python 3.10+
- `python-telegram-bot` 21.x
- `python-dotenv` 1.x

---

Adil Ormanov — [GitHub](https://github.com/Adilforest)
